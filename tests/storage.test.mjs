import test from 'node:test';
import assert from 'node:assert/strict';
import {readFileSync} from 'node:fs';
import initSqlJs from 'sql.js';
import {rows,session,answer,backup,restore,schedule,newContent,appendNewContent} from '../web/core.mjs';
const SQL=await initSqlJs();
function databases(){return {v:new SQL.Database(readFileSync('web/data/vocabulary.sqlite')),d:new SQL.Database(readFileSync('web/data/learning.sqlite'))};}
const now=new Date('2026-10-23T02:00:00.000Z');
test('sample integrity, pending wording excluded, inflected forms retained',()=>{
  const {v,d}=databases();
  assert.equal(rows(v,'SELECT count(*) n FROM words')[0].n,347);
  assert.equal(rows(v,'SELECT count(*) n FROM senses')[0].n,686);
  assert.equal(rows(v,'SELECT count(*) n FROM examples')[0].n,639);
  assert.equal(rows(v,'SELECT count(*) n FROM senses WHERE ready=1')[0].n,478);
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
  for(const [table,column] of [['unit_words','word_id'],['examples','word_id'],['related_words','parent_word_id'],['senses','word_id'],['words','id']])v.run(`DELETE FROM ${table} WHERE ${column}>?`,[last]);
  v.run("UPDATE metadata SET value=? WHERE key='content_version'",[version]);
  return v;
}
function firstBatchOnly(v){return throughWord(v,'w0020','sample-0.1.0');}
test('published batch002 includes cross-page entries and isolates suspect text',()=>{
  const {v,d}=databases();
  assert.equal(rows(v,"SELECT pdf_page FROM examples WHERE word_id='w0080'")[0].pdf_page,24);
  assert.equal(rows(v,"SELECT spelling FROM words WHERE id='w0021'")[0].spelling,'recur');
  const q=session(d,v).queue;
  assert.equal(q.filter(x=>x.sense_id<'s0081').length,102);
  assert(!q.some(x=>x.example_id==='e0023-01'||x.example_id==='e0065-01'));
});
test('old unfinished queue and old backup remain compatible with new corpus',()=>{
  const old=firstBatchOnly(databases().v), {v,d}=databases();
  session(d,old,now);answer(d,old,'good','old-event',now);
  const oldBackup=backup(d,old,now),oldQueue=session(d,old).queue;
  assert.equal(oldQueue.length,23);
  assert.deepEqual(session(d,v).queue,oldQueue);
  assert.equal(session(d,v).cursor,1);
  assert.equal(newContent(d,v).length,455);
  assert.throws(()=>appendNewContent(d,v));
  const fresh=databases().d;restore(fresh,v,oldBackup);
  assert.deepEqual(backup(fresh,v,now).tables,oldBackup.tables);
});
test('completed old queue appends new content once and preserves progress',()=>{
  const old=firstBatchOnly(databases().v),{v,d}=databases();
  session(d,old,now);
  for(let i=0;i<23;i++)answer(d,old,'good',`old-${i}`,now);
  const before=rows(d,'SELECT * FROM progress ORDER BY sense_id');
  assert.equal(appendNewContent(d,v,now),455);
  assert.equal(session(d,v).cursor,23);
  assert.equal(session(d,v).queue.length,478);
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
  const old=throughWord(databases().v,'w0345','vocabulary-0.5.0'),{v,d}=databases();
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
