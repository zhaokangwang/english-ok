// SQLite bytes live in IndexedDB on Web. Native can implement this same load/save contract.
export class BrowserStore {
  async open() {
    this.db=await new Promise((resolve,reject)=>{
      const r=indexedDB.open('english-ok-sqlite',1);
      r.onupgradeneeded=()=>r.result.createObjectStore('databases');
      r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);
    });
    return this;
  }
  async load() {
    return new Promise((resolve,reject)=>{
      const tx=this.db.transaction('databases','readonly');
      const r=tx.objectStore('databases').get('learning');
      tx.oncomplete=()=>resolve(r.result);tx.onerror=()=>reject(tx.error);tx.onabort=()=>reject(tx.error);
    });
  }
  async save(bytes,expectedRevision) {
    return new Promise((resolve,reject)=>{
      const tx=this.db.transaction('databases','readwrite'), store=tx.objectStore('databases');
      let conflict=false;
      const r=store.get('learning');
      r.onsuccess=()=>{
        if((r.result?.revision??0)!==expectedRevision){conflict=true;tx.abort();return;}
        store.put({bytes,revision:expectedRevision+1},'learning');
      };
      tx.oncomplete=()=>resolve(expectedRevision+1);
      tx.onabort=()=>reject(conflict?Error('另一个页面已修改数据，请刷新后继续。'):tx.error??Error('保存失败'));
      tx.onerror=()=>reject(tx.error);
    });
  }
}
