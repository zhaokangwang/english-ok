export const ALGORITHM = 'interval-demo-v1';
export const BACKUP_VERSION = 1;
export const PROFILE = 'local-default';
export function rows(db, sql, params=[]) {
  const stmt=db.prepare(sql);
  try { stmt.bind(params); const out=[]; while(stmt.step()) out.push(stmt.getAsObject()); return out; }
  finally { stmt.free(); }
}
export function schedule(previous, rating, now=new Date()) {
  if (!['again','hard','good'].includes(rating) || !Number.isFinite(now.getTime())) throw Error('无效的反馈或时间');
  const stage=rating==='again'?0:rating==='hard'?Math.max(0,(previous?.stage??0)-1):Math.min(6,(previous?.stage??0)+1);
  const delay=rating==='again'?10*60_000:rating==='hard'?86400_000:[0,1,3,7,14,30,60][stage]*86400_000;
  return {stage, last_review_at:now.toISOString(), due_at:new Date(now.getTime()+delay).toISOString(), review_count:(previous?.review_count??0)+1,algorithm_version:ALGORITHM};
}
export function queue(vocab) {
  return rows(vocab,`SELECT e.id AS example_id,e.sense_id FROM examples e JOIN senses s ON s.id=e.sense_id WHERE s.ready=1 AND e.review_status='visual_checked' GROUP BY e.sense_id HAVING e.id=MIN(e.id) ORDER BY e.sense_id`);
}
export function session(db,vocab,now=new Date()) {
  const found=rows(db,'SELECT * FROM sessions WHERE id=?',['sample-session'])[0];
  if(found) return {...found,queue:JSON.parse(found.queue_json)};
  const q=queue(vocab);
  db.run('INSERT INTO sessions VALUES (?,?,?,?,?)',['sample-session',PROFILE,JSON.stringify(q),0,now.toISOString()]);
  return {id:'sample-session',profile_id:PROFILE,queue:q,cursor:0,updated_at:now.toISOString()};
}
// Existing queues remain frozen. Only after completing them may new content append.
export function newContent(db,vocab) {
  const current=session(db,vocab);
  const seen=new Set(current.queue.map(i=>i.sense_id));
  for(const p of rows(db,'SELECT sense_id FROM progress WHERE profile_id=?',[PROFILE]))seen.add(p.sense_id);
  return queue(vocab).filter(i=>!seen.has(i.sense_id));
}
export function appendNewContent(db,vocab,now=new Date()) {
  db.run('BEGIN');
  try {
    const current=session(db,vocab,now);
    if(current.cursor<current.queue.length)throw Error('请先完成当前这一轮');
    const extra=newContent(db,vocab);
    if(!extra.length)throw Error('没有新增的可学习内容');
    db.run('UPDATE sessions SET queue_json=?,updated_at=? WHERE id=?',[JSON.stringify([...current.queue,...extra]),now.toISOString(),current.id]);
    db.run('COMMIT');
    return extra.length;
  }catch(e){db.run('ROLLBACK');throw e;}
}
export function answer(db,vocab,rating,eventId,now=new Date()) {
  db.run('BEGIN');
  try {
    const current=session(db,vocab,now), item=current.queue[current.cursor];
    if(!item) throw Error('本轮样本已完成');
    const previous=rows(db,'SELECT * FROM progress WHERE profile_id=? AND sense_id=?',[PROFILE,item.sense_id])[0];
    const next=schedule(previous,rating,now);
    db.run('INSERT INTO review_events VALUES (?,?,?,?,?,?,?,?)',[eventId,PROFILE,item.sense_id,item.example_id,rating,next.last_review_at,next.due_at,ALGORITHM]);
    db.run(`INSERT INTO progress VALUES (?,?,?,?,?,?,?) ON CONFLICT(profile_id,sense_id) DO UPDATE SET stage=excluded.stage,last_review_at=excluded.last_review_at,due_at=excluded.due_at,review_count=excluded.review_count,algorithm_version=excluded.algorithm_version`,[PROFILE,item.sense_id,next.stage,next.last_review_at,next.due_at,next.review_count,ALGORITHM]);
    db.run('UPDATE sessions SET cursor=cursor+1, updated_at=? WHERE id=?',[next.last_review_at,current.id]);
    db.run('COMMIT');
  } catch(e) {db.run('ROLLBACK'); throw e;}
}
const TABLES=['profiles','settings','progress','review_events','sessions'];
export function backup(db,vocab,now=new Date()) {
  return {app:'english-ok',backup_version:BACKUP_VERSION,schema_version:1,content_version:rows(vocab,"SELECT value FROM metadata WHERE key='content_version'")[0].value,exported_at:now.toISOString(),tables:Object.fromEntries(TABLES.map(t=>[t,rows(db,`SELECT * FROM ${t}`)]))};
}
const date=(x)=>typeof x==='string' && /^\d{4}-\d\d-\d\dT/.test(x) && Number.isFinite(Date.parse(x));
const integer=(x,min,max)=>Number.isInteger(x)&&x>=min&&x<=max;
function requireThat(ok,message) {if(!ok) throw Error(`备份无效：${message}`);}
export function validateBackup(value,vocab) {
  requireThat(value?.app==='english-ok' && value.backup_version===1 && value.schema_version===1,'格式或版本不支持');
  requireThat(date(value.exported_at) && typeof value.content_version==='string','缺少版本或时间');
  const t=value.tables;
  requireThat(t && TABLES.every(k=>Array.isArray(t[k])&&t[k].length<=100000),'缺少数据表或记录过多');
  requireThat(Object.keys(t).sort().join()=== [...TABLES].sort().join(),'数据表不匹配');
  requireThat(t.profiles.length===1&&t.profiles[0].id===PROFILE&&typeof t.profiles[0].name==='string','仅支持默认本地用户');
  const senses=new Set(rows(vocab,'SELECT id FROM senses').map(x=>x.id));
  const examples=new Map(rows(vocab,'SELECT id,sense_id FROM examples').map(x=>[x.id,x.sense_id]));
  const unique=(list,key)=>new Set(list.map(key)).size===list.length;
  requireThat(unique(t.progress,x=>x.sense_id)&&unique(t.review_events,x=>x.id)&&unique(t.sessions,x=>x.id),'重复记录');
  requireThat(t.settings.length===1&&t.settings[0].profile_id===PROFILE&&integer(t.settings[0].daily_new,1,100)&&typeof t.settings[0].timezone==='string','设置错误');
  try {new Intl.DateTimeFormat('en',{timeZone:t.settings[0].timezone});} catch {throw Error('备份无效：时区');}
  for(const p of t.progress) requireThat(p.profile_id===PROFILE&&senses.has(p.sense_id)&&integer(p.stage,0,6)&&integer(p.review_count,1,1e9)&&date(p.last_review_at)&&date(p.due_at)&&p.algorithm_version===ALGORITHM,'进度记录或词义不兼容');
  for(const e of t.review_events) requireThat(e.profile_id===PROFILE&&typeof e.id==='string'&&e.id.length>0&&senses.has(e.sense_id)&&examples.get(e.example_id)===e.sense_id&&['again','hard','good'].includes(e.rating)&&date(e.reviewed_at)&&date(e.due_at)&&e.algorithm_version===ALGORITHM,'学习事件不兼容');
  for(const p of t.progress) {
    const events=t.review_events.filter(e=>e.sense_id===p.sense_id);
    requireThat(events.length===p.review_count&&events.some(e=>e.reviewed_at===p.last_review_at&&e.due_at===p.due_at),'进度与历史不一致');
  }
  requireThat(t.review_events.every(e=>t.progress.some(p=>p.sense_id===e.sense_id)),'历史没有对应进度');
  for(const s of t.sessions) {
    requireThat(s.id==='sample-session'&&s.profile_id===PROFILE&&date(s.updated_at)&&typeof s.queue_json==='string','任务格式');
    let q; try {q=JSON.parse(s.queue_json);} catch {throw Error('备份无效：任务队列');}
    requireThat(Array.isArray(q)&&q.length<=10000&&integer(s.cursor,0,q.length)&&q.every(i=>senses.has(i.sense_id)&&examples.get(i.example_id)===i.sense_id),'任务内容或位置');
  }
  return value;
}
export function restore(db,vocab,value) {
  validateBackup(value,vocab);
  const columns={profiles:['id','name'],settings:['profile_id','daily_new','timezone'],progress:['profile_id','sense_id','stage','last_review_at','due_at','review_count','algorithm_version'],review_events:['id','profile_id','sense_id','example_id','rating','reviewed_at','due_at','algorithm_version'],sessions:['id','profile_id','queue_json','cursor','updated_at']};
  db.run('BEGIN');
  try {
    for(const t of [...TABLES].reverse()) db.run(`DELETE FROM ${t}`);
    for(const t of TABLES) for(const item of value.tables[t]) {
      const keys=columns[t];
      requireThat(Object.keys(item).sort().join()=== [...keys].sort().join(),`字段不匹配 ${t}`);
      db.run(`INSERT INTO ${t} (${keys.join(',')}) VALUES (${keys.map(()=>'?').join(',')})`,keys.map(k=>item[k]));
    }
    db.run('COMMIT');
  } catch(e) {db.run('ROLLBACK'); throw e;}
}
