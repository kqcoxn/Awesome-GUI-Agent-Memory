"""Render the bilingual reading catalogue from its public CSV; no retrieval.

Run with --check to verify that both Markdown views match the data.
"""
import argparse
import calendar
import csv
import datetime
import re
from collections import Counter
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
THEMES = {
    'visual': ('Visual history', '视觉历史'),
    'interface': ('Interface structure and navigation', '界面结构与导航'),
    'state': ('Task state and experience', '任务状态与经验'),
    'skill': ('Workflows and skills', '工作流与技能'),
    'user': ('User context and personalization', '用户上下文与个性化'),
    'evaluation': ('Benchmarks and evaluation', '基准与评测'),
    'security': ('Safety and reliability', '安全与可靠性'),
}


def cell(value):
    return value.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('|', '&#124;').replace('[', '&#91;').replace(']', '&#93;').replace('\n', ' ')


def render(rows, zh):
    counts = Counter(r['category'] for r in rows)
    if zh:
        lines = ['# GUI 智能体记忆分类目录', '', '[English](CATALOGUE.md) · **简体中文** · [精选阅读](README.zh-CN.md#shelves) · [CSV 数据](catalogue.csv)', '',
                 f"文献覆盖截止 **2026-09-20**；目录整理于 **2026-10-14**。按工作去重共 **{len(rows)} 项**：{counts['direct_memory']} 项直接记忆研究、{counts['memory_evaluation_security']} 项相关评测／安全研究。", '',
                 '收录范围为 LLM/VLM 参与 GUI 决策、操作或记忆处理的研究，依据原文中的保留对象及后续 GUI 用途选材。目录按框架贡献组织，允许存在覆盖遗漏。每项有原文分类依据；分类核验不代表所有效果数字或机制细节均已完成主张级审计。', '',
                 '下列主题用于阅读导航，每项只列一次；主题分区与直接记忆／评测安全类别是两种不同的组织口径。保留对象与用途是综述者综合描述。年份取首次公开日期，可能早于正式发表年份。CSV 保留稳定标识、类别、采用版本、双语描述和原文定位；原文定位沿用核验记录的语言。', '',
                 '[配套数据](README.zh-CN.md#evidence) 保存本目录、逐格赋值、统计汇总、实际检索式及筛选数量汇总。精选阅读还包含目录范围之外的背景综述。', '']
    else:
        lines = ['# GUI Agent Memory Catalogue', '', '**English** · [简体中文](CATALOGUE.zh-CN.md) · [Curated readings](README.md#shelves) · [CSV data](catalogue.csv)', '',
                 f"Publication cutoff: **2026-09-20**. Catalogue prepared: **2026-10-14**. **{len(rows)} distinct works**: {counts['direct_memory']} direct-memory studies and {counts['memory_evaluation_security']} related evaluation/security studies.", '',
                 'The scope covers research in which an LLM/VLM participates in GUI decisions, actions or memory processing. Selection uses original-source evidence of retained information and its subsequent GUI use, organized by contribution to the framework; coverage may be incomplete. Every entry has a source basis for classification. Classification checks do not establish that all effect sizes or mechanism details have undergone claim-level auditing.', '',
                 'Themes below are reading routes, with each work listed once; they are separate from the direct-memory versus evaluation/security categories. Retained objects and uses are reviewer syntheses. Years indicate first public availability and may precede formal publication. The CSV retains stable identifiers, categories, consulted versions, bilingual descriptions and source passages; passage locators preserve the language of the verification record.', '',
                 'The [companion data](README.md#evidence) provide this catalogue, explicit matrix assignments, corpus statistics, executed queries and selection totals. Curated readings also include background surveys outside the catalogue scope.', '']
    lines += [' | '.join(f'[{names[int(zh)]} ({sum(r["theme"] == theme for r in rows)})](#{theme})' for theme, names in THEMES.items()), '']
    years = Counter(r['first_public_date'][:4] for r in rows)
    lines += ['## 年度分布' if zh else '## Annual distribution', '',
              '| 首次公开年份 | 工作数 |' if zh else '| First public year | Works |',
              '|---|---:|']
    lines += [f'| {year}{"*" if year == "2026" else ""} | {count} |' for year, count in sorted(years.items())]
    lines += ['', '*2026 年截至 9 月 20 日。计数描述本目录选材的年份分布，每项工作只计一次；不能据此估计全领域增长率。' if zh else
              '*2026 covers publications through 20 September. Counts describe the selected catalogue, with each work counted once; they do not estimate field-wide growth.', '']
    for theme, names in THEMES.items():
        subset = sorted((r for r in rows if r['theme'] == theme), key=lambda r: r['title'].casefold())
        lines += [f'<a id="{theme}"></a>', '', f'## {names[int(zh)]} · {len(subset)}', '',
                  '| 年份 | 论文 | 保留／测量对象 | 后续 GUI 用途／评测终点 |' if zh else '| Year | Paper | Retained / measured object | Subsequent GUI use / evaluation endpoint |',
                  '|---|---|---|---|']
        for r in subset:
            obj, use = (r['object_zh'], r['use_zh']) if zh else (r['object_en'], r['use_en'])
            lines.append(f'| {r["first_public_date"][:4]} | <a id="{r["citation_key"]}"></a>[{cell(r["title"])}]({r["source_url"]}) | {cell(obj)} | {cell(use)} |')
        lines.append('')
    lines += ['## 数据维护' if zh else '## Data maintenance', '',
              '`catalogue.csv` 是本目录的数据源。修改记录后运行 `python scripts/build_catalogue.py`；使用 `python scripts/build_catalogue.py --check` 检查双语页面是否同步。' if zh else
              '`catalogue.csv` is the data source for these views. After editing records, run `python scripts/build_catalogue.py`; use `python scripts/build_catalogue.py --check` to verify both language versions.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    with (ROOT / 'catalogue.csv').open(encoding='utf-8', newline='') as f:
        rows = list(csv.DictReader(f))
    for field in ['work_id', 'citation_key']:
        if len({r[field] for r in rows}) != len(rows):
            raise ValueError(f'Duplicate {field}')
    for r in rows:
        if any(not value.strip() for value in r.values()):
            raise ValueError(f'Empty field: {r["work_id"]}')
        if r['theme'] not in THEMES or r['category'] not in {'direct_memory', 'memory_evaluation_security'}:
            raise ValueError(f'Unknown classification: {r["work_id"]}')
        if not re.fullmatch(r'[a-zA-Z0-9_-]+', r['citation_key']):
            raise ValueError('Unsafe anchor')
        url = urlparse(r['source_url'])
        if url.scheme != 'https' or not url.netloc:
            raise ValueError(f'Non-public source: {r["work_id"]}')
        date = r['first_public_date']
        if not re.fullmatch(r'\d{4}(?:-\d{2}){0,2}', date):
            raise ValueError(f'Invalid cutoff date: {r["work_id"]}')
        parts = [int(part) for part in date.split('-')]
        year, month = parts[0], parts[1] if len(parts) > 1 else 12
        day = parts[2] if len(parts) > 2 else calendar.monthrange(year, month)[1]
        if datetime.date(year, month, day) > datetime.date(2026, 9, 20):
            raise ValueError(f'Unresolved cutoff date: {r["work_id"]}')
        if re.search(r'\b[A-Za-z]:[/\\]|file://|fulltext_manifest|download_staging', ' '.join(r.values())):
            raise ValueError(f'Local path in public data: {r["work_id"]}')
    for zh, name in [(False, 'CATALOGUE.md'), (True, 'CATALOGUE.zh-CN.md')]:
        content = render(rows, zh)
        target = ROOT / name
        if args.check:
            if not target.exists() or target.read_text(encoding='utf-8') != content:
                raise SystemExit(f'Out of date: {name}')
        else:
            target.write_text(content, encoding='utf-8', newline='\n')
    print(f'{len(rows)} distinct works; bilingual catalogue {"verified" if args.check else "rendered"}.')


if __name__ == '__main__':
    main()
