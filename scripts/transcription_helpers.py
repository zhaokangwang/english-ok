"""Build visually transcribed records without reading or rewriting previous batches."""
class Transcription:
    def __init__(self):self.words=[]
    def add(self,n,spelling,ipa,definition,page,group,meanings,examples,mnemonic='',related=(),notes=()):
        senses=[dict(id=f's{n:04}-{i+1:02}',pos=p,gloss=g,origin='editor_mapping',ready=False) for i,(p,g) in enumerate(meanings)]
        exs=[]
        for j,(si,en,zh,target,label,p) in enumerate(examples):
            start=en.index(target)
            exs.append(dict(id=f'e{n:04}-{j+1:02}',sense_id=senses[si]['id'],english=en,translation=zh,target=target,target_start=start,target_end=start+len(target),book_label=label,pdf_page=p,printed_page=f'{p-8:03}',review_status='visual_checked',note='真题标签仅据原书，年份题号未核实。' if label=='真题' else ''))
            senses[si]['ready']=True
        pages=sorted(set([page]+[e['pdf_page'] for e in exs]))
        self.words.append(dict(id=f'w{n:04}',spelling=spelling,phonetic=ipa,source_definition=definition,mnemonic=mnemonic,group_name=group,pdf_pages=pages,printed_pages=[f'{p-8:03}' for p in pages],review_status='visual_checked',senses=senses,examples=exs,related=[dict(id=f'r{n:04}-{i+1:02}',spelling=s,definition=d,relation='derived',pdf_page=p,note='关联资料，未自动计入主词进度。') for i,(s,d,p) in enumerate(related)],notes=list(notes)))
    def pending(self,spelling,index,note):
        w=next(w for w in self.words if w['spelling']==spelling)
        e=w['examples'][index];e['review_status']='pending';e['note']=note;w['notes'].append(note)
        for s in w['senses']:s['ready']=any(x['sense_id']==s['id'] and x['review_status']=='visual_checked' for x in w['examples'])
