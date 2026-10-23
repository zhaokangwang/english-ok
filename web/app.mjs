import {rows,session,answer,backup,restore,newContent,appendNewContent} from './core.mjs';
import {BrowserStore} from './storage.mjs';
const $=s=>document.querySelector(s);
const escape=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
let SQL,vocab,learning,store,revision=0,busy=true,revealed=false,activeExample=null,entryFromStudy=false,selectedWord=null,listScroll=0;
const status=(message,error=false)=>{$('#status').textContent=message;$('#status').classList.toggle('error',error);};
const controls=()=>{
  document.querySelectorAll('button,select').forEach(x=>x.disabled=busy);
  document.querySelectorAll('[data-rating]').forEach(x=>x.disabled=busy||!revealed||!activeExample);
  $('#reveal').disabled=busy||!activeExample;
  $('#full-entry').disabled=busy||!activeExample;
  $('#more-content').disabled=busy;
};
async function mutate(fn) {
  if(busy)return;
  busy=true;controls();const before=learning.export();
  try {fn();revision=await store.save(learning.export(),revision);revealed=false;status('');render();$('#study-scroll').scrollTop=0;}
  catch(e){learning.close();learning=new SQL.Database(before);learning.run('PRAGMA foreign_keys=ON');status(`未保存：${e.message}`,true);render();}
  finally{busy=false;controls();}
}
function marked(e){return escape(e.english.slice(0,e.target_start))+'<mark>'+escape(e.english.slice(e.target_start,e.target_end))+'</mark>'+escape(e.english.slice(e.target_end));}
function renderWord() {
  $('#vocab-list').hidden=!!selectedWord;
  $('#vocab-detail').hidden=!selectedWord;
  if(!selectedWord)return;
  const w=rows(vocab,'SELECT * FROM words WHERE id=?',[selectedWord])[0];
  if(!w)return;
  const senses=rows(vocab,'SELECT * FROM senses WHERE word_id=? ORDER BY id',[w.id]);
  $('#word').innerHTML=`<h2 style="margin-top:22px">${escape(w.spelling)} <span class="meta">${escape(w.phonetic??'按词性区分读音')}</span></h2><p>${escape(w.source_definition)}</p><p class="meta">PDF ${escape(w.pdf_pages)} / 书内页 ${escape(w.printed_pages)} · ${escape(w.id)}</p>`+senses.map(s=>`<div class="sense"><strong>${escape(s.pos)} ${escape(s.gloss)}</strong> <span class="badge">${s.ready?'有学习例句':'待补例句'}</span>`+rows(vocab,'SELECT * FROM examples WHERE sense_id=? ORDER BY id',[s.id]).map(e=>`<p class="english">${marked(e)}</p><p>${escape(e.translation)}</p><p class="meta">原书标签：${escape(e.book_label)} · PDF ${e.pdf_page} / 书内页 ${escape(e.printed_page)} · ${escape(e.note)} ${e.review_status==='pending'?'【待核实，不入队】':''}</p>`).join('')+'</div>').join('')+(w.mnemonic?`<details><summary>原书记忆辅助</summary><p>${escape(w.mnemonic)}</p></details>`:'')+'<p class="meta">词义拆分为编辑按语境整理；音标未作外部词典复核。</p>';
}
function renderVocabulary(){
  $('#unit-list').innerHTML=rows(vocab,'SELECT * FROM units ORDER BY sort_order').map((unit,index)=>{
    const words=rows(vocab,'SELECT w.* FROM unit_words uw JOIN words w ON w.id=uw.word_id WHERE uw.unit_id=? ORDER BY uw.sort_order',[unit.id]);
    return `<details class="unit-group" ${index===0?'open':''}><summary class="unit-heading"><span><strong>${escape(unit.title)}</strong><small>${escape(unit.subtitle)}</small></span><span class="unit-count">${words.length} 词 <span class="unit-chevron">⌄</span></span></summary><p class="unit-note">${unit.complete?'本单元主词已导入 · 派生资料另行整理':'本单元持续补充中 · 以下为已导入词汇'}</p><div class="word-list">`+words.map(w=>{
      const gloss=[...new Set(rows(vocab,'SELECT gloss FROM senses WHERE word_id=? ORDER BY id',[w.id]).flatMap(s=>s.gloss.split(/[；;]/).map(x=>x.trim()).filter(Boolean)))].join('；');
      return `<button class="word-row" data-word="${escape(w.id)}" title="${escape(gloss)}"><span class="word-en" lang="en">${escape(w.spelling)}</span><span class="word-zh">${escape(gloss)}</span></button>`;
    }).join('')+'</div></details>';
  }).join('');
}
$('#unit-list').onclick=e=>{
  const row=e.target.closest('[data-word]');if(!row||busy)return;
  listScroll=$('#vocab-page').scrollTop;selectedWord=row.dataset.word;entryFromStudy=false;renderWord();route();$('#vocab-page').scrollTop=0;
};
$('#back-list').onclick=()=>{selectedWord=null;entryFromStudy=false;renderWord();route();$('#vocab-page').scrollTop=listScroll;};
function render(){
  renderWord();
  const s=session(learning,vocab),item=s.queue[s.cursor];
  $('#position').textContent=`${Math.min(s.cursor+1,s.queue.length)} / ${s.queue.length}`;
  activeExample=item?rows(vocab,'SELECT e.*,w.spelling,w.phonetic,s.pos,s.gloss FROM examples e JOIN words w ON w.id=e.word_id JOIN senses s ON s.id=e.sense_id WHERE e.id=?',[item.example_id])[0]:null;
  if(item){const e=rows(vocab,'SELECT * FROM examples WHERE id=?',[item.example_id])[0];
    $('#task').innerHTML=`<h2 class="headword">${escape(activeExample.spelling)}</h2><div class="phonetic">${escape(activeExample.phonetic??'')}</div><div class="sentence-label">在句子中理解</div><p class="english">${marked(e)}</p>`+(revealed?`<div class="explanation"><p class="meaning"><span class="meta">${escape(activeExample.pos)}</span> ${escape(activeExample.gloss)}</p><p class="translation">${escape(e.translation)}</p></div>`:'<p class="hint">先试着理解高亮单词在这里的含义。</p>');
  } else $('#task').innerHTML='<div class="complete"><span class="tag">本轮完成</span><h2>今天又多理解了一点。</h2><p class="muted">本轮已学完，记录已保存在本机。可以去词库回看，或继续学习更新的内容。</p></div>';
  const extra=item?[]:newContent(learning,vocab);
  $('#more-content').hidden=!!item||!extra.length;
  $('#more-content').textContent=`继续学习新增内容（${extra.length} 个词义）`;
  $('#reveal').hidden=revealed||!item;
  $('#ratings').hidden=!revealed||!item;
  $('#full-entry').hidden=!item;
  const count=rows(learning,'SELECT count(*) AS n FROM review_events')[0].n;
  $('#progress').textContent=`已记录 ${count} 次学习`;
  $('#history').textContent=JSON.stringify(rows(learning,'SELECT * FROM review_events ORDER BY rowid DESC LIMIT 8'),null,2);
}
function route(){
  const page=['study','vocab','settings'].includes(location.hash.slice(1))?location.hash.slice(1):'study';
  for(const name of ['study','vocab','settings'])$(`#${name}-page`).hidden=name!==page;
  $('#page-title').textContent={study:'语境学词',vocab:'我的词库',settings:'设置'}[page];
  document.querySelectorAll('[data-page]').forEach(a=>{if(a.dataset.page===page)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current');});
  $('#back-study').hidden=page!=='vocab'||!entryFromStudy;
}
window.addEventListener('hashchange',route);
document.querySelectorAll('[data-page]').forEach(a=>a.addEventListener('click',()=>{entryFromStudy=false;if(a.dataset.page==='vocab'&&vocab){selectedWord=null;renderWord();}route();}));
$('#reveal').onclick=()=>{revealed=true;render();controls();};
$('#full-entry').onclick=()=>{if(!activeExample)return;selectedWord=activeExample.word_id;renderWord();entryFromStudy=true;location.hash='vocab';route();$('#vocab-page').scrollTop=0;};
$('#back-study').onclick=()=>{location.hash='study';};
$('#more-content').onclick=()=>mutate(()=>appendNewContent(learning,vocab));
route();
function download(name,bytes,type){const url=URL.createObjectURL(new Blob([bytes],{type}));const a=document.createElement('a');a.href=url;a.download=name;a.click();setTimeout(()=>URL.revokeObjectURL(url),30000);}
document.querySelectorAll('[data-rating]').forEach(b=>b.onclick=()=>mutate(()=>answer(learning,vocab,b.dataset.rating,globalThis.crypto?.randomUUID?.()??`evt-${Date.now()}-${Math.random().toString(36).slice(2)}`)));
$('#export').onclick=()=>download(`english-ok-backup-${new Date().toISOString().slice(0,10)}.json`,JSON.stringify(backup(learning,vocab),null,2),'application/json');
$('#sqlite').onclick=()=>download('learning.sqlite',learning.export(),'application/vnd.sqlite3');
$('#import').onclick=()=>$('#file').click();
$('#file').onchange=async()=>{
  const file=$('#file').files[0];$('#file').value='';if(!file)return;
  try{
    if(file.size>20*1024*1024)throw Error('备份超过20MB，当前样本验证页不支持');
    const value=JSON.parse(await file.text());
    if(!confirm('导入会替换当前学习记录。请确认已导出需要保留的记录，是否继续？'))return;
    await mutate(()=>restore(learning,vocab,value));
  }catch(e){status(`导入失败，原记录保留：${e.message}`,true);}
};
try {
  SQL=await initSqlJs({locateFile:file=>`vendor/${file}`});
  const response=await fetch('data/vocabulary.sqlite');if(!response.ok)throw Error('词库加载失败');
  vocab=new SQL.Database(new Uint8Array(await response.arrayBuffer()));
  store=await new BrowserStore().open();const saved=await store.load();revision=saved?.revision??0;
  learning=new SQL.Database(saved?.bytes);
  if(!saved){const response=await fetch('data/learning.sql');if(!response.ok)throw Error('学习库结构加载失败');learning.run(await response.text());}
  if(rows(learning,'PRAGMA user_version')[0].user_version!==1)throw Error('学习数据库版本不支持，请保留备份并升级程序');
  learning.run('PRAGMA foreign_keys=ON');session(learning,vocab);
  revision=await store.save(learning.export(),revision);
  renderVocabulary();
  $('.local-label').textContent=`本地词库 · ${rows(vocab,'SELECT count(*) AS n FROM words')[0].n}词`;
  render();busy=false;controls();status('');
}catch(e){status(`无法打开本地数据：${e.message}。请勿使用隐私浏览；不要清除数据来重试。`,true);}
