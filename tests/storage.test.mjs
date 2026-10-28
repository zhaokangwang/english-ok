import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import initSqlJs from 'sql.js';
import {rows,session,answer,backup,restore,schedule,newContent,appendNewContent} from '../web/core.mjs';
const SQL=await initSqlJs();
function databases(){return {v:new SQL.Database(readFileSync('web/data/vocabulary.sqlite')),d:new SQL.Database(readFileSync('web/data/learning.sqlite'))};}
const now=new Date('2026-10-23T02:00:00.000Z');
test('sample integrity, pending wording excluded, inflected forms retained',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w2313','vocabulary-0.12.0');
  assert.equal(rows(v,'SELECT count(*) n FROM words')[0].n,1051);
  assert.equal(rows(v,'SELECT count(*) n FROM senses')[0].n,2281);
  assert.equal(rows(v,'SELECT count(*) n FROM examples')[0].n,1972);
  assert.equal(rows(v,'SELECT count(*) n FROM senses WHERE ready=1')[0].n,1456);
  assert.equal(rows(v,"SELECT count(*) n FROM examples WHERE review_status='pending'")[0].n,86);
  assert.deepEqual(rows(v,'PRAGMA foreign_key_check'),[]);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-001'")[0].n,165);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-001'")[0].complete,1);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-002'")[0].n,180);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-002'")[0].complete,1);
  const q=session(d,v).queue;
  assert(!q.some(x=>x.example_id==='e0004-01'));
  assert(q.some(x=>x.example_id==='e0004-02'));
  assert.equal(rows(v,"SELECT target FROM examples WHERE id='e0002-01'")[0].target,'activated');
});
function throughWord(v,last,version) {
  // A historical slice cannot retain a later unit-completion claim when it removes that unit's words.
  v.run('UPDATE units SET complete=0 WHERE id IN (SELECT unit_id FROM unit_words WHERE word_id>?)',[last]);
  for(const [table,column] of [['unit_words','word_id'],['examples','word_id'],['related_words','parent_word_id'],['senses','word_id'],['words','id']])v.run(`DELETE FROM ${table} WHERE ${column}>?`,[last]);
  v.run("UPDATE metadata SET value=? WHERE key='content_version'",[version]);
  return v;
}
function firstBatchOnly(v){return throughWord(v,'w0020','sample-0.1.0');}
function beforeSixthBatch(v) {
  // Version 0.5.1 published the seventh-batch sample before the sixth batch.
  // A numeric ID cutoff would accidentally keep the newly filled sixth batch.
  v.run('UPDATE units SET complete=0 WHERE id IN (SELECT unit_id FROM unit_words WHERE word_id>? AND word_id NOT IN (?,?))',['w0345','w1000','w1001']);
  for(const [table,column] of [['unit_words','word_id'],['examples','word_id'],['related_words','parent_word_id'],['senses','word_id'],['words','id']]) {
    v.run(`DELETE FROM ${table} WHERE ${column}>? AND ${column} NOT IN (?,?)`,['w0345','w1000','w1001']);
  }
  v.run("UPDATE metadata SET value=? WHERE key='content_version'",['vocabulary-0.5.1']);
  return v;
}
test('latest approved batch matches source totals and preserves learning state when appended',()=>{
  const plan=JSON.parse(readFileSync('content/import-plan.json','utf8'));
  const parts=plan.approved_batches.map(batch=>JSON.parse(readFileSync(batch.file,'utf8')));
  const all=parts.flatMap(part=>part.words),latest=parts.at(-1).words;
  const {v,d}=databases(),old=databases().v;
  assert.equal(rows(v,"SELECT value FROM metadata WHERE key='content_version'")[0].value,plan.content_version);
  for(const [table,count] of [['words',all.length],['senses',all.reduce((n,w)=>n+w.senses.length,0)],
      ['examples',all.reduce((n,w)=>n+w.examples.length,0)]])assert.equal(rows(v,`SELECT count(*) n FROM ${table}`)[0].n,count);
  assert.deepEqual(rows(v,'PRAGMA foreign_key_check'),[]);
  assert.deepEqual(rows(v,'SELECT id,spelling FROM words ORDER BY id'),
    all.map(({id,spelling})=>({id,spelling})).sort((a,b)=>a.id.localeCompare(b.id)));
  old.run('CREATE TEMP TABLE latest_words(id TEXT PRIMARY KEY)');
  for(const word of latest)old.run('INSERT INTO latest_words VALUES (?)',[word.id]);
  old.run('UPDATE units SET complete=0 WHERE id IN (SELECT unit_id FROM unit_words WHERE word_id IN (SELECT id FROM latest_words))');
  for(const [table,column] of [['unit_words','word_id'],['examples','word_id'],['related_words','parent_word_id'],['senses','word_id'],['words','id']]) {
    old.run(`DELETE FROM ${table} WHERE ${column} IN (SELECT id FROM latest_words)`);
  }
  old.run('DROP TABLE latest_words');
  old.run("UPDATE metadata SET value=? WHERE key='content_version'",['before-'+plan.approved_batches.at(-1).id]);
  const oldQueue=session(d,old,now).queue;
  answer(d,old,'good','before-latest-batch',now);
  const saved=backup(d,old,now),before=rows(d,'SELECT * FROM progress ORDER BY sense_id');
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const expected=latest.flatMap(w=>w.senses.filter(s=>s.ready).map(s=>s.id)).sort();
  assert.deepEqual(newContent(d,v).map(item=>item.sense_id).sort(),expected);
  const pending=new Set(latest.flatMap(w=>w.examples.filter(e=>e.review_status==='pending').map(e=>e.id)));
  assert(!newContent(d,v).some(item=>pending.has(item.example_id)));
  assert.throws(()=>appendNewContent(d,v));
  const restored=databases().d;
  restore(restored,v,saved);
  assert.deepEqual(backup(restored,v,now).tables,saved.tables);
  for(let i=1;i<oldQueue.length;i++)answer(d,v,'good',`finish-before-latest-${i}`,now);
  const completed=rows(d,'SELECT * FROM progress ORDER BY sense_id');
  assert.equal(appendNewContent(d,v,now),expected.length);
  assert.deepEqual(session(d,v).queue.slice(0,oldQueue.length),oldQueue);
  assert.deepEqual(session(d,v).queue.slice(oldQueue.length).map(item=>item.sense_id).sort(),expected);
  assert(!session(d,v).queue.slice(oldQueue.length).some(item=>pending.has(item.example_id)));
  assert.deepEqual(rows(d,'SELECT * FROM progress ORDER BY sense_id'),completed);
  assert.deepEqual(rows(restored,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(d,v).length,0);
  assert.throws(()=>appendNewContent(d,v));
});

test('published batch002 includes cross-page entries and isolates suspect text',()=>{
  const {v,d}=databases();
  assert.equal(rows(v,"SELECT pdf_page FROM examples WHERE word_id='w0080'")[0].pdf_page,24);
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0021'")[0].spelling,'recur');
  const q=session(d,v).queue;
  assert.equal(q.filter(x=>x.sense_id<'s0081').length,102);
  assert(!q.some(x=>x.example_id==='e0023-01'||x.example_id==='e0065-01'));
});
test('old unfinished queue and old backup remain compatible with new corpus',()=>{
  const old=firstBatchOnly(databases().v), {d}=databases(),v=throughWord(databases().v,'w2313','vocabulary-0.12.0');
  session(d,old,now);answer(d,old,'good','old-event',now);
  const oldBackup=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,23);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  assert.equal(newContent(d,v).length,1433);
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,oldBackup);
  assert.deepEqual(backup(fresh,v,now).tables,oldBackup.tables);
});
test('completed old queue appends new content once and preserves progress',()=>{
  const old=firstBatchOnly(databases().v),{d}=databases(),v=throughWord(databases().v,'w2313','vocabulary-0.12.0');
  session(d,old,now);
  for(let i=0;i<23;i++)answer(d,old,'good',`old-${i}`,now);
  const before=rows(d,'SELECT * FROM progress ORDER BY sense_id');
  assert.equal(appendNewContent(d,v,now),1433);
  assert.equal(session(d,v).cursor,23);
  assert.equal(session(d,v).queue.length,1456);
  assert.equal(newContent(d,v).length,0);
  assert.deepEqual(rows(d,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.throws(()=>appendNewContent(d,v));
});
test('third batch preserves the 80-word queue and backup with 116 additions',()=>{
  const old=throughWord(databases().v,'w0080','vocabulary-0.2.0'),{d}=databases(),v=throughWord(databases().v,'w0165','vocabulary-0.3.0');
  session(d,old,now);answer(d,old,'good','old-batch2',now);
  const before=backup(d,old,now);
  assert.equal(session(d,v).queue.length,102);
  assert.equal(session(d,v).cursor,1);
  assert.equal(newContent(d,v).length,116);
  const fresh=databases().d;restore(fresh,v,before);
  assert.deepEqual(backup(fresh,v,now).tables,before.tables);
  assert.throws(()=>appendNewContent(fresh,v));
  for(let i=1;i<102;i++)answer(fresh,v,'good',`complete-batch2-${i}`,now);
  assert.equal(appendNewContent(fresh,v,now),116);
  assert.equal(session(fresh,v).queue.length,218);
});
test('third batch boundary, continuations and suspect examples',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w0165','vocabulary-0.3.0');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0081'")[0].spelling,'sketch');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0165'")[0].spelling,'hasty');
  assert(!rows(v,"SELECT id FROM words WHERE spelling='agent'").length);
  const q=session(d,v).queue;
  for(const id of ['e0083-01','e0102-02','e0146-02','e0154-02'])assert(!q.some(x=>x.example_id===id));
  assert.equal(q.filter(x=>x.sense_id>='s0081').length,116);
  const w=rows(v,"SELECT pdf_pages FROM words WHERE spelling='humble'")[0];
  assert.deepEqual(JSON.parse(w.pdf_pages),[30,31]);
});
test('fourth batch keeps prior unit queue and backup, appends 142 after completion',()=>{
  const old=throughWord(databases().v,'w0165','vocabulary-0.3.0'),{d}=databases(),v=throughWord(databases().v,'w0269','vocabulary-0.4.0');
  session(d,old,now);answer(d,old,'good','old-unit1',now);
  const before=backup(d,old,now);
  assert.equal(session(d,v).queue.length,218);
  assert.equal(newContent(d,v).length,142);
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,before);
  assert.deepEqual(backup(fresh,v,now).tables,before.tables);
  for(let i=1;i<218;i++)answer(fresh,v,'good',`complete-unit1-${i}`,now);
  const progress=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert.equal(appendNewContent(fresh,v,now),142);
  assert.equal(session(fresh,v).queue.length,360);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),progress);
  assert.equal(newContent(fresh,v).length,0);
});
test('fourth batch boundaries, separate customs and pending material',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w0269','vocabulary-0.4.0');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0166'")[0].spelling,'agent');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0269'")[0].spelling,'prevail');
  assert(!rows(v,"SELECT id FROM words WHERE spelling='avail'").length);
  assert.equal(rows(v,"SELECT pdf_page FROM examples WHERE id='e0269-02'")[0].pdf_page,59);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling IN ('custom','customs')")[0].n,2);
  const q=session(d,v).queue;
  assert.equal(q.filter(x=>x.sense_id>='s0166').length,142);
  for(const id of ['e0215-02','e0219-02','e0241-01','e0247-02','e0259-02','e0261-02'])assert(!q.some(x=>x.example_id===id));
  assert(q.some(x=>x.example_id==='e0188-01'));
});

test('fifth batch preserves fourth queue and backup, appends 114 exactly once',()=>{
  const old=throughWord(databases().v,'w0269','vocabulary-0.4.0'),{d}=databases(),v=throughWord(databases().v,'w0345','vocabulary-0.5.0');
  session(d,old,now);answer(d,old,'good','old-batch4',now);
  const saved=backup(d,old,now), queue=session(d,old).queue;
  assert.equal(queue.length,360);
  assert.deepEqual(session(d,v).queue,queue);
  assert.equal(session(d,v).cursor,1);
  assert.equal(newContent(d,v).length,114);
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  for(let i=1;i<360;i++)answer(fresh,v,'good',`complete-batch4-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert.equal(appendNewContent(fresh,v,now),114);
  assert.equal(session(fresh,v).queue.length,474);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
});

test('fifth batch stops at unit boundary, records continuations and excludes pending',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w0345','vocabulary-0.5.0');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0270'")[0].spelling,'avail');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0345'")[0].spelling,'stare');
  assert(!rows(v,"SELECT id FROM words WHERE spelling='origin'").length);
  assert.equal(rows(v,"SELECT pdf_page FROM examples WHERE word_id='w0343'")[0].pdf_page,74);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE spelling='eager'")[0].pdf_pages),[71,72]);
  const q=session(d,v).queue;
  assert.equal(q.filter(x=>x.sense_id>='s0270').length,114);
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w0270' AND review_status='pending'");
  assert.equal(pending.length,6);
  for(const {id} of pending)assert(!q.some(x=>x.example_id===id));
  const blocked=rows(v,"SELECT s.id FROM senses s JOIN words w ON w.id=s.word_id WHERE w.spelling='investigate'").map(x=>x.id);
  assert(blocked.length>0);
  assert(!q.some(x=>blocked.includes(x.sense_id)));
});
test('seventh batch sample preserves fifth queue and backup, appends only four after completion',()=>{
  const old=throughWord(databases().v,'w0345','vocabulary-0.5.0'),{d}=databases(),v=beforeSixthBatch(databases().v);
  assert.equal(rows(v,'SELECT count(*) n FROM words')[0].n,347);
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id>'w0345' ORDER BY id"),[
    {id:'w1000',spelling:'coordinate'},{id:'w1001',spelling:'subordinate'}
  ]);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling='origin'")[0].n,0);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-003'")[0].complete,0);
  assert.deepEqual(rows(v,"SELECT word_id FROM unit_words WHERE unit_id='unit-003' ORDER BY word_id"),[
    {word_id:'w1000'},{word_id:'w1001'}
  ]);
  session(d,old,now);answer(d,old,'good','old-batch5',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,474);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  assert.equal(newContent(d,v).length,4);
  assert(newContent(d,v).every(x=>x.sense_id.startsWith('s1000-')||x.sense_id.startsWith('s1001-')));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<474;i++)answer(fresh,v,'good',`complete-batch5-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert.equal(appendNewContent(fresh,v,now),4);
  assert.equal(session(fresh,v).cursor,474);
  assert.equal(session(fresh,v).queue.length,478);
  assert.deepEqual(session(fresh,v).queue.slice(0,474),oldQueue);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});
test('sixth batch fills skipped IDs without replacing the seventh sample or old learning state',()=>{
  const old=beforeSixthBatch(databases().v),{d}=databases(),v=throughWord(databases().v,'w1001','vocabulary-0.6.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,347);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,686);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,639);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id IN ('w1000','w1001') ORDER BY id"),[
    {id:'w1000',spelling:'coordinate'},{id:'w1001',spelling:'subordinate'}
  ]);
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0346'")[0].spelling,'origin');
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0451'")[0].spelling,'senator');
  const sixthIds=[...Array.from({length:34},(_,i)=>`w${String(346+i).padStart(4,'0')}`),...Array.from({length:49},(_,i)=>`w${String(403+i).padStart(4,'0')}`)];
  assert.deepEqual(rows(v,"SELECT id FROM words WHERE id>'w0345' AND id<'w1000' ORDER BY id").map(item=>item.id),sixthIds);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling IN ('obstacle','hamper')")[0].n,0);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-003'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-003'")[0].n,85);
  const sixthReady=rows(v,"SELECT count(*) n FROM senses WHERE word_id>'w0345' AND word_id<'w1000' AND ready=1")[0].n;
  assert.equal(sixthReady,110);
  session(d,old,now);answer(d,old,'good','old-before-batch6',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,478);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  assert.equal(newContent(d,v).length,sixthReady);
  assert(newContent(d,v).every(item=>item.sense_id>'s0345'&&item.sense_id<'s1000'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>'w0345' AND word_id<'w1000' AND review_status='pending'");
  assert.equal(pending.length,3);
  for(const item of pending)assert(!newContent(d,v).some(extra=>extra.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<478;i++)answer(fresh,v,'good',`complete-before-batch6-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s1000-')));
  assert(before.some(item=>item.sense_id.startsWith('s1001-')));
  assert.equal(appendNewContent(fresh,v,now),sixthReady);
  assert.equal(session(fresh,v).cursor,478);
  assert.equal(session(fresh,v).queue.length,478+sixthReady);
  assert.deepEqual(session(fresh,v).queue.slice(0,478),oldQueue);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});
test('seventh batch continuation preserves 430-word corpus progress and appends 148 only once',()=>{
  const old=throughWord(databases().v,'w1001','vocabulary-0.6.0'),{d}=databases(),v=throughWord(databases().v,'w1104','vocabulary-0.7.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,430);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,855);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,789);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-003'")[0].n,164);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-003'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-004'")[0].n,24);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-004'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id BETWEEN 'w0380' AND 'w0402'")[0].n,0);
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id='w1104'"),[{id:'w1104',spelling:'detect'}]);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w1104'")[0].pdf_pages),[114,115]);
  assert.equal(rows(v,"SELECT count(*) n FROM examples WHERE word_id='w1104' AND pdf_page=115")[0].n,2);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling='spot'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>'w1001'")[0].n,103);
  session(d,old,now);answer(d,old,'good','old-before-batch7-continuation',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,588);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const extra=newContent(d,v);
  assert.equal(extra.length,148);
  assert(extra.every(item=>item.sense_id>='s1002'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w1002' AND review_status='pending'");
  assert.equal(pending.length,12);
  for(const item of pending)assert(!extra.some(itemInQueue=>itemInQueue.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<588;i++)answer(fresh,v,'good',`complete-before-batch7-continuation-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s1000-')));
  assert(before.some(item=>item.sense_id.startsWith('s1001-')));
  assert.equal(appendNewContent(fresh,v,now),148);
  assert.equal(session(fresh,v).cursor,588);
  assert.equal(session(fresh,v).queue.length,736);
  assert.deepEqual(session(fresh,v).queue.slice(0,588),oldQueue);
  assert.deepEqual(session(fresh,v).queue.slice(588),extra);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});
test('eighth batch preserves the 533-word corpus and 736-item queue, appending 146 exactly once',()=>{
  const old=throughWord(databases().v,'w1104','vocabulary-0.7.0'),{d}=databases(),v=throughWord(databases().v,'w1215','vocabulary-0.8.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,533);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,1078);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,989);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  session(d,old,now);answer(d,old,'good','old-before-batch8',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,736);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const extra=newContent(d,v);
  assert.equal(extra.length,146);
  assert(extra.every(item=>item.sense_id>='s1105'&&item.sense_id<'s1216'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w1105' AND review_status='pending'");
  assert.equal(pending.length,11);
  for(const item of pending)assert(!extra.some(queued=>queued.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<736;i++)answer(fresh,v,'good',`complete-before-batch8-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s1104-')));
  assert.equal(appendNewContent(fresh,v,now),146);
  assert.equal(session(fresh,v).cursor,736);
  assert.equal(session(fresh,v).queue.length,882);
  assert.deepEqual(session(fresh,v).queue.slice(0,736),oldQueue);
  assert.deepEqual(session(fresh,v).queue.slice(736),extra);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});
test('eighth batch keeps cross-page examples, unit ownership and the sixth-batch gap',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w1215','vocabulary-0.8.0');
  assert.equal(rows(v,"SELECT value FROM metadata WHERE key='content_version'")[0].value,'vocabulary-0.8.0');
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id IN ('w1104','w1105','w1215') ORDER BY id"),[
    {id:'w1104',spelling:'detect'},{id:'w1105',spelling:'spot'},{id:'w1215',spelling:'temper'}
  ]);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>='w1105'")[0].n,111);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling='personality'")[0].n,0);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w1132'")[0].pdf_pages),[119,120]);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w1191'")[0].pdf_pages),[129,130]);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w1210'")[0].pdf_pages),[133,134]);
  assert.equal(rows(v,"SELECT count(*) n FROM examples WHERE word_id='w1191' AND pdf_page=130")[0].n,1);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-003'")[0].n,164);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-003'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-004'")[0].n,135);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-004'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id>='w1105' AND unit_id<>'unit-004'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id BETWEEN 'w0380' AND 'w0402'")[0].n,0);
  const queue=session(d,v).queue;
  assert.equal(queue.length,882);
  for(const {id} of rows(v,"SELECT id FROM examples WHERE word_id>='w1105' AND review_status='pending'")) {
    assert(!queue.some(item=>item.example_id===id));
  }
  const excludedSenses=rows(v,"SELECT s.id FROM senses s JOIN words w ON w.id=s.word_id WHERE w.spelling IN ('release','vigorous')").map(item=>item.id);
  assert(excludedSenses.length>0);
  assert(!queue.some(item=>excludedSenses.includes(item.sense_id)));
});
test('ninth partial batch preserves the 644-word corpus and 882-item queue, appending 135 only once',()=>{
  const old=throughWord(databases().v,'w1215','vocabulary-0.8.0'),{d}=databases(),v=throughWord(databases().v,'w1308','vocabulary-0.9.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,644);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,1323);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,1195);
  assert.equal(rows(old,"SELECT complete FROM units WHERE id='unit-004'")[0].complete,0);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  session(d,old,now);answer(d,old,'good','old-before-batch9',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,882);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const extra=newContent(d,v);
  assert.equal(extra.length,135);
  assert(extra.every(item=>item.sense_id>='s1216'&&item.sense_id<'s1309'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w1216' AND review_status='pending'");
  assert.equal(pending.length,5);
  for(const item of pending)assert(!extra.some(queued=>queued.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<882;i++)answer(fresh,v,'good',`complete-before-batch9-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s1215-')));
  assert.equal(appendNewContent(fresh,v,now),135);
  assert.equal(session(fresh,v).cursor,882);
  assert.equal(session(fresh,v).queue.length,1017);
  assert.deepEqual(session(fresh,v).queue.slice(0,882),oldQueue);
  assert.deepEqual(session(fresh,v).queue.slice(882),extra);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});
test('ninth partial batch completes unit four, retains cross-page material and leaves both gaps open',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w1308','vocabulary-0.9.0');
  assert.equal(rows(v,"SELECT value FROM metadata WHERE key='content_version'")[0].value,'vocabulary-0.9.0');
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id IN ('w1216','w1269','w1270','w1308') ORDER BY id"),[
    {id:'w1216',spelling:'personality'},{id:'w1269',spelling:'strap'},
    {id:'w1270',spelling:'merit'},{id:'w1308',spelling:'pioneer'}
  ]);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>='w1216'")[0].n,93);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>='w1309' OR spelling IN ('compatible','upset')")[0].n,0);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w1290'")[0].pdf_pages),[149,150]);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w1308'")[0].pdf_pages),[152,153]);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-003'")[0].n,164);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-003'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-004'")[0].n,189);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-004'")[0].complete,1);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE unit_id='unit-005'")[0].n,39);
  assert.equal(rows(v,"SELECT complete FROM units WHERE id='unit-005'")[0].complete,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id BETWEEN 'w1216' AND 'w1269' AND unit_id<>'unit-004'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id BETWEEN 'w1270' AND 'w1308' AND unit_id<>'unit-005'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id BETWEEN 'w0380' AND 'w0402'")[0].n,0);
  const queue=session(d,v).queue;
  assert.equal(queue.length,1017);
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w1216' AND review_status='pending'");
  assert.deepEqual(pending.map(item=>item.id).sort(),['e1230-01','e1249-02','e1263-02','e1270-02','e1286-02']);
  for(const {id} of pending)assert(!queue.some(item=>item.example_id===id));
});
test('tenth batch preserves the 737-word corpus and 1017-item queue, appending 143 exactly once',()=>{
  const old=throughWord(databases().v,'w1308','vocabulary-0.9.0'),{d}=databases(),v=throughWord(databases().v,'w2103','vocabulary-0.10.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,737);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,1539);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,1376);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  session(d,old,now);answer(d,old,'good','old-before-batch10',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,1017);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const extra=newContent(d,v);
  assert.equal(extra.length,143);
  assert(extra.every(item=>item.sense_id>='s2000'&&item.sense_id<'s2104'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w2000' AND review_status='pending'");
  assert.equal(pending.length,9);
  for(const item of pending)assert(!extra.some(queued=>queued.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<1017;i++)answer(fresh,v,'good',`complete-before-batch10-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s1308-')));
  assert.equal(appendNewContent(fresh,v,now),143);
  assert.equal(session(fresh,v).cursor,1017);
  assert.equal(session(fresh,v).queue.length,1160);
  assert.deepEqual(session(fresh,v).queue.slice(0,1017),oldQueue);
  assert.deepEqual(session(fresh,v).queue.slice(1017),extra);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});

test('tenth batch preserves both gaps and keeps fifth and sixth units incomplete',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w2103','vocabulary-0.10.0');
  assert.equal(rows(v,"SELECT value FROM metadata WHERE key='content_version'")[0].value,'vocabulary-0.10.0');
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id IN ('w2000','w2080','w2081','w2103') ORDER BY id"),[
    {id:'w2000',spelling:'upset'},{id:'w2080',spelling:'cognitive'},
    {id:'w2081',spelling:'extinguish'},{id:'w2103',spelling:'occasion'}
  ]);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>='w2000'")[0].n,104);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling IN ('compatible','asset','opportunity')")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id BETWEEN 'w0380' AND 'w0402' OR (id>='w1309' AND id<'w2000')")[0].n,0);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w2033'")[0].pdf_pages),[160,161]);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w2053'")[0].pdf_pages),[164,165]);
  assert.deepEqual(JSON.parse(rows(v,"SELECT pdf_pages FROM words WHERE id='w2103'")[0].pdf_pages),[174,175]);
  assert(rows(v,"SELECT pdf_pages FROM words WHERE id>='w2000'").every(row=>!JSON.parse(row.pdf_pages).includes(170)));
  for(const [unit,count,complete] of [['unit-003',164,0],['unit-004',189,1],['unit-005',120,0],['unit-006',23,0]]) {
    assert.equal(rows(v,'SELECT count(*) n FROM unit_words WHERE unit_id=?',[unit])[0].n,count);
    assert.equal(rows(v,'SELECT complete FROM units WHERE id=?',[unit])[0].complete,complete);
  }
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id BETWEEN 'w2000' AND 'w2080' AND unit_id<>'unit-005'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id BETWEEN 'w2081' AND 'w2103' AND unit_id<>'unit-006'")[0].n,0);
  const queue=session(d,v).queue;
  assert.equal(queue.length,1160);
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w2000' AND review_status='pending'");
  assert.deepEqual(pending.map(item=>item.id).sort(),['e2015-01','e2027-02','e2056-01','e2063-01','e2064-02','e2066-02','e2071-02','e2097-02','e2101-02']);
  for(const {id} of pending)assert(!queue.some(item=>item.example_id===id));
  assert.equal(rows(v,"SELECT count(*) n FROM examples WHERE word_id='w2028'")[0].n,1);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling='disapprove'")[0].n,0);
});

test('eleventh batch preserves the 841-word corpus and 1160-item queue, appending 157 once',()=>{
  const old=throughWord(databases().v,'w2103','vocabulary-0.10.0'),{d}=databases(),v=throughWord(databases().v,'w2212','vocabulary-0.11.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,841);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,1764);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,1567);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  session(d,old,now);answer(d,old,'good','old-before-batch11',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,1160);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const extra=newContent(d,v);
  assert.equal(extra.length,157);
  assert(extra.every(item=>item.sense_id>='s2104'&&item.sense_id<'s2213'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w2104' AND review_status='pending'");
  assert.equal(pending.length,12);
  for(const item of pending)assert(!extra.some(queued=>queued.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<1160;i++)answer(fresh,v,'good',`complete-before-batch11-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s2103-')));
  assert.equal(appendNewContent(fresh,v,now),157);
  assert.equal(session(fresh,v).cursor,1160);
  assert.equal(session(fresh,v).queue.length,1317);
  assert.deepEqual(session(fresh,v).queue.slice(0,1160),oldQueue);
  assert.deepEqual(session(fresh,v).queue.slice(1160),extra);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});

test('eleventh batch keeps cross-page sources, both gaps and pending examples out of the queue',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w2212','vocabulary-0.11.0');
  assert.equal(rows(v,"SELECT value FROM metadata WHERE key='content_version'")[0].value,'vocabulary-0.11.0');
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id IN ('w2104','w2212') ORDER BY id"),[
    {id:'w2104',spelling:'opportunity'},{id:'w2212',spelling:'confuse'}
  ]);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>='w2104'")[0].n,109);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling IN ('compatible','asset','refuse')")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id BETWEEN 'w0380' AND 'w0402' OR (id>='w1309' AND id<'w2000')")[0].n,0);
  for(const [word,pages] of [['severe',[175,176]],['grip',[177,178]],['heighten',[179,180]],
       ['nourish',[184,185]],['illuminate',[185,186]],['flatter',[189,190]],
       ['fiction',[190,191]],['ascertain',[192,193]],['compound',[193,194]]]) {
    assert.deepEqual(JSON.parse(rows(v,'SELECT pdf_pages FROM words WHERE spelling=?',[word])[0].pdf_pages),pages);
  }
  for(const [unit,count,complete] of [['unit-003',164,0],['unit-004',189,1],['unit-005',120,0],['unit-006',132,0]]) {
    assert.equal(rows(v,'SELECT count(*) n FROM unit_words WHERE unit_id=?',[unit])[0].n,count);
    assert.equal(rows(v,'SELECT complete FROM units WHERE id=?',[unit])[0].complete,complete);
  }
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id>='w2104' AND unit_id<>'unit-006'")[0].n,0);
  const queue=session(d,v).queue;
  assert.equal(queue.length,1317);
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w2104' AND review_status='pending'");
  assert.deepEqual(pending.map(item=>item.id).sort(),['e2120-02','e2125-01','e2129-01','e2132-02',
    'e2151-01','e2151-02','e2153-02','e2177-01','e2177-02','e2182-02','e2184-02','e2192-01']);
  for(const {id} of pending)assert(!queue.some(item=>item.example_id===id));
  const excluded=rows(v,"SELECT s.id FROM senses s JOIN words w ON w.id=s.word_id WHERE w.spelling IN ('pollute','orient')").map(item=>item.id);
  assert(excluded.length>0);
  assert(!queue.some(item=>excluded.includes(item.sense_id)));
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling='non-durable'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM examples e JOIN words w ON w.id=e.word_id WHERE w.spelling='durable' AND e.english LIKE '%non-durable%'")[0].n,0);
});

test('twelfth batch preserves the 950-word corpus and 1317-item queue, appending 139 once',()=>{
  const old=throughWord(databases().v,'w2212','vocabulary-0.11.0'),{d}=databases(),v=throughWord(databases().v,'w2313','vocabulary-0.12.0');
  assert.equal(rows(old,'SELECT count(*) n FROM words')[0].n,950);
  assert.equal(rows(old,'SELECT count(*) n FROM senses')[0].n,2031);
  assert.equal(rows(old,'SELECT count(*) n FROM examples')[0].n,1779);
  for(const [table,columns] of [['words','id,spelling'],['senses','id,word_id'],['examples','id,word_id,sense_id'],['related_words','id,parent_word_id,spelling']]) {
    const prior=rows(old,`SELECT ${columns} FROM ${table} ORDER BY id`);
    const current=new Map(rows(v,`SELECT ${columns} FROM ${table} ORDER BY id`).map(item=>[item.id,item]));
    for(const item of prior)assert.deepEqual(current.get(item.id),item);
  }
  session(d,old,now);answer(d,old,'good','old-before-batch12',now);
  const saved=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,1317);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  const extra=newContent(d,v);
  assert.equal(extra.length,139);
  assert(extra.every(item=>item.sense_id>='s2213'&&item.sense_id<'s2314'));
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w2213' AND review_status='pending'");
  assert.equal(pending.length,15);
  for(const item of pending)assert(!extra.some(queued=>queued.example_id===item.id));
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,saved);
  assert.deepEqual(backup(fresh,v,now).tables,saved.tables);
  assert.deepEqual(session(fresh,v).queue,oldQueue);
  for(let i=1;i<1317;i++)answer(fresh,v,'good',`complete-before-batch12-${i}`,now);
  const before=rows(fresh,'SELECT * FROM progress ORDER BY sense_id');
  assert(before.some(item=>item.sense_id.startsWith('s2212-')));
  assert.equal(appendNewContent(fresh,v,now),139);
  assert.equal(session(fresh,v).cursor,1317);
  assert.equal(session(fresh,v).queue.length,1456);
  assert.deepEqual(session(fresh,v).queue.slice(0,1317),oldQueue);
  assert.deepEqual(session(fresh,v).queue.slice(1317),extra);
  assert.deepEqual(rows(fresh,'SELECT * FROM progress ORDER BY sense_id'),before);
  assert.equal(newContent(fresh,v).length,0);
  assert.throws(()=>appendNewContent(fresh,v));
  const migrated=backup(fresh,v,now),reopened=databases().d;
  restore(reopened,v,migrated);
  assert.deepEqual(backup(reopened,v,now),migrated);
});

test('twelfth batch completes unit six, keeps both gaps and excludes pending examples',()=>{
  const {d}=databases(),v=throughWord(databases().v,'w2313','vocabulary-0.12.0');
  assert.equal(rows(v,"SELECT value FROM metadata WHERE key='content_version'")[0].value,'vocabulary-0.12.0');
  assert.deepEqual(rows(v,"SELECT id,spelling FROM words WHERE id IN ('w2213','w2245','w2246','w2313') ORDER BY id"),[
    {id:'w2213',spelling:'refuse'},{id:'w2245',spelling:'policy'},
    {id:'w2246',spelling:'facility'},{id:'w2313',spelling:'alleviate'}
  ]);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id>='w2213'")[0].n,101);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE spelling IN ('compatible','asset','ease')")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM words WHERE id BETWEEN 'w0380' AND 'w0402' OR (id>='w1309' AND id<'w2000')")[0].n,0);
  for(const [word,pages] of [['contemporary',[195,196]],['hammer',[199,200]],['artifact',[203,204]],
       ['infect',[204,205]],['handicap',[205,206]],['paralyse',[208,209]],
       ['utmost',[209,210]],['survive',[211,212]],['alleviate',[214,215]]]) {
    assert.deepEqual(JSON.parse(rows(v,'SELECT pdf_pages FROM words WHERE spelling=?',[word])[0].pdf_pages),pages);
  }
  assert(rows(v,"SELECT pdf_pages FROM words WHERE id>='w2213'").every(row=>!JSON.parse(row.pdf_pages).includes(202)));
  for(const [unit,count,complete] of [['unit-003',164,0],['unit-004',189,1],['unit-005',120,0],
       ['unit-006',165,1],['unit-007',68,0]]) {
    assert.equal(rows(v,'SELECT count(*) n FROM unit_words WHERE unit_id=?',[unit])[0].n,count);
    assert.equal(rows(v,'SELECT complete FROM units WHERE id=?',[unit])[0].complete,complete);
  }
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id BETWEEN 'w2213' AND 'w2245' AND unit_id<>'unit-006'")[0].n,0);
  assert.equal(rows(v,"SELECT count(*) n FROM unit_words WHERE word_id BETWEEN 'w2246' AND 'w2313' AND unit_id<>'unit-007'")[0].n,0);
  const queue=session(d,v).queue;
  assert.equal(queue.length,1456);
  const pending=rows(v,"SELECT id FROM examples WHERE word_id>='w2213' AND review_status='pending'");
  assert.deepEqual(pending.map(item=>item.id).sort(),['e2214-02','e2216-01','e2241-02','e2243-01','e2245-02',
    'e2251-02','e2264-02','e2279-02','e2284-02','e2286-02','e2290-01','e2295-02','e2296-02','e2306-02','e2312-02']);
  for(const {id} of pending)assert(!queue.some(item=>item.example_id===id));
});

test('feedback and unfinished session survive SQLite byte reopen',()=>{
  const {v,d}=databases(); session(d,v,now);answer(d,v,'good','event-1',now);
  const reopened=new SQL.Database(d.export());
  assert.equal(session(reopened,v).cursor,1);
  assert.equal(rows(reopened,'SELECT review_count FROM progress')[0].review_count,1);
  assert.equal(rows(reopened,'SELECT due_at FROM progress')[0].due_at,'2026-10-24T02:00:00.000Z');
});
test('failed feedback rolls back all three writes',()=>{
  const {v,d}=databases(); session(d,v);answer(d,v,'good','event-1',now);
  const before=backup(d,v,now);
  assert.throws(()=>answer(d,v,'hard','event-1',now));
  assert.deepEqual(backup(d,v,now),before);
});
test('backup restores exactly in fresh database and rejects bad input atomically',()=>{
  const {v,d}=databases();session(d,v);answer(d,v,'hard','event-1',now);answer(d,v,'again','event-2',now);
  const payload=backup(d,v,now), other=databases().d;
  restore(other,v,JSON.parse(JSON.stringify(payload)));
  assert.deepEqual(backup(other,v,now),payload);
  const cases=[p=>p.backup_version=99,p=>p.tables.progress[0].sense_id='missing',p=>p.tables.progress[0].review_count=99,p=>p.tables.sessions[0].cursor=9999,p=>p.tables.review_events[0].rating='bad',p=>p.tables.profiles[0].unexpected=true];
  for(const change of cases){const bad=structuredClone(payload);change(bad);assert.throws(()=>restore(other,v,bad));assert.deepEqual(backup(other,v,now),payload);}
});
test('correcting content or adding words leaves progress unchanged',()=>{
  const {v,d}=databases();session(d,v);answer(d,v,'good','event-1',now);const before=backup(d,v,now);
  v.run("UPDATE examples SET translation='校对后的翻译' WHERE id='e0001-01'");
  v.run("INSERT INTO words SELECT 'new-word','test',NULL,'n. 测试','','新增','[13]','[\"005\"]','pending'");
  assert.deepEqual(backup(d,v,now),before);
});
test('interval boundaries and invalid feedback',()=>{
  assert.equal(schedule({stage:6,review_count:2},'good',now).stage,6);
  assert.equal(schedule({stage:4,review_count:2},'again',now).due_at,'2026-10-23T02:10:00.000Z');
  assert.equal(schedule(null,'hard',now).stage,0);
  assert.throws(()=>schedule(null,'invalid',now));
});
