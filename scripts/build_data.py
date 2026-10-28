"""Build reviewable sample databases; never overwrite a user's learning database."""
import hashlib
import json
import shutil
import sqlite3
import os
from pathlib import Path
from content_pipeline import load_content, identities, guard_identities

ROOT=Path(__file__).resolve().parents[1]
def validate(data):
    ids=set()
    def unique(value):
        if value in ids: raise ValueError(f'Duplicate ID: {value}')
        ids.add(value)
    spellings=set()
    for w in data['words']:
        unique(w['id'])
        normalized=w['spelling'].strip().casefold()
        if normalized in spellings: raise ValueError('Duplicate spelling')
        spellings.add(normalized)
        if w['review_status'] not in ['visual_checked','pending']:raise ValueError('Invalid review status')
        if not w['source_definition'] or not w['pdf_pages']: raise ValueError('Missing source')
        senses={s['id']:s for s in w['senses']}
        for s in w['senses']:
            unique(s['id'])
            if not s['pos'] or not s['gloss']: raise ValueError('Missing sense')
        for e in w['examples']:
            unique(e['id'])
            if e['review_status'] not in ['visual_checked','pending']:raise ValueError('Invalid example status')
            if e['sense_id'] not in senses: raise ValueError('Orphan example')
            if not e['translation'] or e['english'][e['target_start']:e['target_end']] != e['target']: raise ValueError('Invalid target/translation')
        for s in w['senses']:
            if s['ready'] and not any(e['sense_id']==s['id'] and e['review_status']=='visual_checked' for e in w['examples']): raise ValueError('Ready sense has no checked example')
        for r in w['related']: unique(r['id'])

def build():
    data,plan,batches=load_content()
    validate(data)
    units=json.loads((ROOT/'content/units.json').read_text(encoding='utf-8'))['units']
    assigned=[wid for unit in units for wid in unit['word_ids']]
    if len(assigned)!=len(set(assigned)) or set(assigned)!={w['id'] for w in data['words']}:raise ValueError('Each word must belong to exactly one explicit book unit')
    original=json.loads((ROOT/'content/source-manifest.json').read_text(encoding='utf-8'))
    pdf=ROOT/original['filename']
    with pdf.open('rb') as f:
        digest=hashlib.file_digest(f,'sha256').hexdigest()
    from pypdf import PdfReader
    page_count=len(PdfReader(pdf).pages)
    if digest!=plan['source_sha256'] or page_count!=plan['source_page_count']:raise ValueError('Source PDF fingerprint mismatch')
    pages=sorted({p for w in data['words'] for p in w['pdf_pages']})
    source=dict(id=data['source_id'], filename=pdf.name, sha256=digest, bytes=pdf.stat().st_size, page_count=page_count,
                sample_pdf_pages=pages, printed_pages=[f'{p-8:03}' for p in pages], method=data['method'],
                notes=['人工视觉转录；未运行自动 OCR。','按批次清单累计合并；不是逐页完整OCR。','扫描页仍以原 PDF 为准；音标需后续词典复核。'])
    out=ROOT/'web/data'; out.mkdir(parents=True,exist_ok=True)
    # Validate historical identity before replacing the published vocabulary.
    target=out/'vocabulary.sqlite'
    if target.exists():
        previous=sqlite3.connect(target)
        old={r[0]:['word',r[1]] for r in previous.execute('SELECT id,spelling FROM words')}
        old.update({r[0]:['sense',r[1]] for r in previous.execute('SELECT id,word_id FROM senses')})
        old.update({r[0]:['example',r[1],r[2]] for r in previous.execute('SELECT id,word_id,sense_id FROM examples')})
        old.update({r[0]:['related',r[1],r[2]] for r in previous.execute('SELECT id,parent_word_id,spelling FROM related_words')})
        previous.close();guard_identities(old,identities(data))
    # Construct in memory and publish SQLite with atomic replace, last in build.
    db=sqlite3.connect(':memory:'); db.executescript((ROOT/'schema/vocabulary.sql').read_text(encoding='utf-8'))
    db.executemany('INSERT INTO metadata VALUES (?,?)',[('schema_version','2'),('content_version',data['content_version']),('source_id',data['source_id'])])
    db.execute('INSERT INTO sources VALUES (?,?,?,?)',(source['id'],source['filename'],digest,page_count))
    for w in data['words']:
        db.execute('INSERT INTO words VALUES (?,?,?,?,?,?,?,?,?)',(w['id'],w['spelling'],w['phonetic'],w['source_definition'],w['mnemonic'],w['group_name'],json.dumps(w['pdf_pages']),json.dumps(w['printed_pages']),w['review_status']))
        for s in w['senses']: db.execute('INSERT INTO senses VALUES (?,?,?,?,?,?)',(s['id'],w['id'],s['pos'],s['gloss'],s['origin'],int(s['ready'])))
        for e in w['examples']: db.execute('INSERT INTO examples VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',(e['id'],w['id'],e['sense_id'],e['english'],e['translation'],e['target'],e['target_start'],e['target_end'],e['book_label'],e['pdf_page'],e['printed_page'],e['review_status'],e['note']))
        for r in w['related']: db.execute('INSERT INTO related_words VALUES (?,?,?,?,?,?,?)',(r['id'],w['id'],r['spelling'],r['definition'],r['relation'],r['pdf_page'],r['note']))
    for unit in units:
        db.execute('INSERT INTO units VALUES (?,?,?,?,?)',(unit['id'],unit['title'],unit['subtitle'],unit['sort_order'],int(unit['complete'])))
        for order,wid in enumerate(unit['word_ids']):db.execute('INSERT INTO unit_words VALUES (?,?,?)',(unit['id'],wid,order))
    assert not db.execute('PRAGMA foreign_key_check').fetchall()
    db.commit()
    binary=db.serialize(); db.close()
    learning=sqlite3.connect(':memory:'); learning.executescript((ROOT/'schema/learning.sql').read_text(encoding='utf-8')); learning.commit()
    (out/'learning.sqlite').write_bytes(learning.serialize()); learning.close()
    # Browser runs identical SQL schema, initialized only for a new local store.
    shutil.copyfile(ROOT/'schema/learning.sql',out/'learning.sql')
    has_ocr=any('ocr' in part.get('method','').lower() for _,part in batches)
    transcription_method='逐页视觉核对；部分批次使用本机OCR辅助提取。' if has_ocr else '人工视觉转录，并非自动 OCR。'
    summary=[f"# {len(data['words'])}词累计审阅稿",'',f"内容版本：{data['content_version']}。{transcription_method}",'',data['policy'],'']
    for w in data['words']:
        summary.extend([f"## {w['spelling']} · {w['id']}",'',f"PDF页 {w['pdf_pages']} / 书内页 {w['printed_pages']}",'',w['source_definition'],'',f"音标：{w['phonetic'] or '见释义字段，按词性区分'}",''])
        for s in w['senses']: summary.append(f"- {s['id']} {s['pos']} {s['gloss']}：{'可学习' if s['ready'] else '缺对应例句，暂不入队'}")
        for e in w['examples']: summary.extend(['',f"**{e['id']} · 原书标签：{e['book_label']} · {e['review_status']} · PDF {e['pdf_page']}**",'',e['english'],'',e['translation'],'',f"对应 {e['sense_id']}；目标词形：{e['target']}。{e['note']}"])
        if w['mnemonic']: summary.extend(['','原书记忆辅助：'+w['mnemonic']])
        for r in w['related']: summary.extend(['',f"关联词：{r['spelling']} — {r['definition']}。{r['note']}"])
        for note in w['notes']: summary.extend(['','待注意：'+note])
        summary.append('')
    (ROOT/'docs').mkdir(exist_ok=True)
    (ROOT/'docs/sample-review.md').write_text('\n'.join(summary),encoding='utf-8')
    missing=[f"- {w['spelling']} / {s['id']}：{s['gloss']}" for w in data['words'] for s in w['senses'] if not s['ready']]
    pending=[f"- {w['spelling']} / {e['id']}：{e['note']}" for w in data['words'] for e in w['examples'] if e['review_status']!='visual_checked']
    report=['# 累计质量清单','',f"范围：{len(data['words'])}个主要词条，不代表全书完整覆盖。",'',f'可学习词义：{sum(s["ready"] for w in data["words"] for s in w["senses"])} 个。',f'缺可用例句的词义：{len(missing)} 个。','','## 待核实例句','']+pending+['','## 暂不进入学习队列的词义','']+missing+['','## 全局复核项','','- 音标已按扫描页视觉转录，尚未做外部词典复核。','- 真题仅保留原书标签，年份题号未核实。','- 词义拆分为编辑判断，需要你确认拆分粒度。','- 派生例句在associated-material及批次associated文件中，暂未生成独立学习卡。','- 原始证据为项目PDF；transcripts保存各批核对初稿，OCR批次另有识别来源清单。' if has_ocr else '- 原始证据为项目PDF；transcripts内是人工转录初稿，不是OCR。','']
    (ROOT/'docs/quality-report.md').write_text('\n'.join(report),encoding='utf-8')
    isolated=[]
    for batch,_ in batches:
        associated=json.loads((ROOT/batch['associated_file']).read_text(encoding='utf-8'))
        for item in associated['items']:
            if item.get('status')=='quarantined':isolated.append(f"- {batch['id']} / {item['word']} / PDF {item['pdf_page']}：{item.get('reason','待核对')}")
    if isolated:
        with (ROOT/'docs/quality-report.md').open('a',encoding='utf-8') as f:f.write('\n## 关联素材中隔离的内容\n\n'+'\n'.join(isolated)+'\n')
    for batch,part in batches:
        headings={w['id'] for w in part['words']}
        # Reuse the complete cumulative review sections to avoid two inconsistent renderers.
        start=next((i for i,line in enumerate(summary) if line.startswith('## ')),len(summary))
        sections=[];include=False
        for line in summary[start:]:
            if line.startswith('## '):include=any(line.endswith('· '+wid) for wid in headings)
            if include:sections.append(line)
        (ROOT/f'docs/{batch["id"]}-review.md').write_text(f'# {batch["id"]} 审阅稿\n\n'+ '\n'.join(sections),encoding='utf-8')
    counts=lambda part:dict(words=len(part['words']),senses=sum(len(w['senses']) for w in part['words']),examples=sum(len(w['examples']) for w in part['words']),ready_senses=sum(s['ready'] for w in part['words'] for s in w['senses']),pending_examples=sum(e['review_status']=='pending' for w in part['words'] for e in w['examples']))
    audit=dict(content_version=data['content_version'],source_sha256=digest,totals=counts(data),batches=[dict(id=b['id'],file=b['file'],associated_items=len(json.loads((ROOT/b['associated_file']).read_text(encoding='utf-8'))['items']),**counts(p)) for b,p in batches],checks=['source fingerprint','unique IDs and normalized spellings','existing identity preservation','example-sense and word association','target substring offsets','ready sense has checked example','foreign_key_check'],notes=['学习数据库未读取或修改。','重复构建是幂等的累计发布，不重复插入。'])
    (ROOT/'docs/import-report.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    report_lines=['# 分批导入报告','',f"当前词库版本：{data['content_version']}。",'', '| 批次 | 主词 | 词义 | 例句 | 可学习词义 | 待核实例句 | 关联材料 |','|---|---:|---:|---:|---:|---:|---:|']
    for entry in audit['batches']:
        report_lines.append(f"| {entry['id']} | {entry['words']} | {entry['senses']} | {entry['examples']} | {entry['ready_senses']} | {entry['pending_examples']} | {entry['associated_items']} |")
    report_lines+=['',f"累计：{audit['totals']['words']}个主词、{audit['totals']['senses']}个词义、{audit['totals']['examples']}条例句，其中{audit['totals']['ready_senses']}个词义可学习。",'','## 各批范围与疑点','']
    for batch,_ in batches:
        report_lines.extend([f"### {batch['id']}",'',batch['coverage'],''])
        report_lines.extend('- '+note for note in batch.get('quality_notes',[]))
        report_lines.append('')
    report_lines+=['## 构建检查结果','','- 原PDF指纹、ID、拼写去重、页码、目标词形位置及外键检查通过。','- 所有原有词条身份保留；个人库不被内容构建修改。','- 当前学习轮次保留；结束后可追加新增的未学词义。','- '+transcription_method+'音标未外部词典复核。','- 自动测试和桌面浏览器验证另见verification.md，本构建报告不冒充测试结果。','- iPhone和安卓仍需真机验证。','']
    (ROOT/'docs/import-report.md').write_text('\n'.join(report_lines),encoding='utf-8')
    (ROOT/'content/id-registry.json').write_text(json.dumps(identities(data),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    # Keep a local rollback copy without exposing it from the HTTP root.
    if target.exists() and target.read_bytes()!=binary:
        (ROOT/'runtime').mkdir(exist_ok=True)
        shutil.copyfile(target,ROOT/'runtime/vocabulary.previous.sqlite')
    stage=out/'vocabulary.sqlite.staging'
    stage.write_bytes(binary)
    os.replace(stage,target)
    (out/'catalog.json').write_text(json.dumps(dict(content_version=data['content_version'],**counts(data)),ensure_ascii=False),encoding='utf-8')
    (ROOT/'content/source-manifest.json').write_text(json.dumps(source,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    write_ledger(plan)
    print(f"Built {len(data['words'])} words, {sum(len(w['senses']) for w in data['words'])} senses, {sum(len(w['examples']) for w in data['words'])} examples. SHA256 {digest}")

def write_ledger(plan):
    # Keep planned and unfinished batches when a later batch is imported first.
    ledger_path=ROOT/'content/batch-ledger.json'
    prior=json.loads(ledger_path.read_text(encoding='utf-8')) if ledger_path.exists() else {}
    by_id={b['id']:b for b in prior.get('batches',[])}
    by_id.update({b['id']:b for b in plan['approved_batches']})
    next_page=max(b['owner_pages'][1] for b in by_id.values())+1
    next_number=max(int(b['id'].split('-')[-1]) for b in by_id.values())+1
    for number,start in enumerate(range(next_page,333,20),next_number):
        end=min(start+19,332)
        by_id[f'batch-{number:03}']=dict(id=f'batch-{number:03}',owner_pages=[start,end],context_pages=[max(10,start-1),min(332,end+1)],status='planned_unreviewed',boundary='第39页为第二单元扉页；正文从40页agent开始。后续边界按单元核对。' if start==39 else '边界未查看，不能视为正文或完整词表。')
    ledger=dict(source_id=plan['source_id'],source_sha256=plan['source_sha256'],front_matter=dict(pages=[1,9],status='excluded_pending_final_inventory'),batches=[by_id[key] for key in sorted(by_id)])
    (ROOT/'content/batch-ledger.json').write_text(json.dumps(ledger,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    partial=sum(b['status']=='partially_imported' for b in plan['approved_batches'])
    lines=['# PDF批次清单','',f"页码均为PDF页码。已登记{len(plan['approved_batches'])}批，其中{partial}批仅部分导入；其余为草稿或规划范围，不代表已识别或核实。",'', '| 批次 | 主体页码 | 衔接查阅页 | 状态 |','|---|---|---|---|']
    for b in ledger['batches']:
        label={'imported':'已导入','partially_imported':'部分导入','draft':'草稿，未导入'}.get(b['status'],'待检查，边界暂定')
        lines.append(f"| {b['id']} | {b['owner_pages'][0]}–{b['owner_pages'][1]} | {b['context_pages'][0]}–{b['context_pages'][1]} | {label} |")
    lines+=['','- 1–9页：前置材料，最终目录核对时再检查是否有遗漏词汇。','- batch-001是20个主词样本，不声称完整收录所有派生词。','- batch-002额外补齐第13页recur，末词draft的两条例句来自第24页。','- batch-003从第24页sketch到第38页hasty；第39页第二单元扉页作为边界证据。','- batch-004从第二单元agent到prevail，末词续文至59页。batch-005从59页avail到74页stare，不重复导入prevailing素材，第二单元180个主词收尾；75页为第三单元扉页，batch-006从origin开始。','- 页范围是工作分配，真正归属按固定词条ID；关联素材另存，不算独立主词。','']
    for b in plan['approved_batches']:
        if b['status']=='partially_imported':lines.extend([f"- {b['id']}：{b['coverage']}",''])
    (ROOT/'docs/batch-plan.md').write_text('\n'.join(lines),encoding='utf-8')

if __name__=='__main__': build()
