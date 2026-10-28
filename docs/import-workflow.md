# OCR辅助导入流程

第十三批使用Windows自带OCR识别图片，再逐页视觉核对并拆分主词、词义、例句和派生材料。识别在本机运行，未安装额外OCR包或上传PDF。原识别文本存在错字、漏句和音标错误，不能直接写入正式词库。

## 提取与核对

先用Poppler按批渲染图片，再运行Windows PowerShell 5.1下的OCR脚本：

```powershell
pdftoppm -f 215 -l 235 -scale-to 1800 -png '27考研英语5500词汇-你还在背单词吗.pdf' tmp/pdfs/b13
powershell -NoProfile -ExecutionPolicy Bypass -File scripts/ocr_pages_windows.ps1 -InputPrefix tmp/pdfs/b13 -FirstPage 215 -LastPage 235
```

脚本输出每页`.ocr.txt`和包含文字坐标的`.ocr.json`；图片SHA256及语言匹配时复用缓存。需要Windows安装相应OCR语言。本批来源记录见`content/transcripts/batch-013-ocr-manifest.json`，临时图片及识别缓存未纳入Git。

转录模块使用`transcription_helpers.Transcription`，每完成一页落盘。只收录归属页起始的主词，跨页续文完整保留；派生资料另存associated。语法、原译或词义映射疑点保留原文并设pending。分工时仅传入当前页范围、输入路径、字段约定和必要边界信息，减少重复上下文。

## 合并与发布

后续批次新增配置和转录模块，复用同一个导入器及审计工具；不要重新运行已发布批次的merge或publish。

```powershell
python -X utf8 scripts/import_batch.py merge --config scripts/batch013-config.json
python -X utf8 scripts/import_batch.py check --config scripts/batch013-config.json
python -X utf8 scripts/import_batch.py backup --config scripts/batch013-config.json
python -X utf8 scripts/import_batch.py publish --config scripts/batch013-config.json
python -X utf8 scripts/build_data.py
python -X utf8 -m unittest discover -s tests -p "test_*.py"
npm test
python -X utf8 scripts/audit_batch.py --config scripts/batch013-config.json
```

merge逐段保存草稿、关联资料及带SHA256的检查点；check验证ID连续性、页码、单元、旧身份和保留缺口。backup保留导入前文件，publish拒绝覆盖已注册批次或初始快照；build生成正式数据库。多文件注册若被中断，需先与备份比对再恢复，不能假定整个发布跨文件原子完成。

测试通过且审计确认旧数据不变后，将检查点标为imported，记录测试结果、版本及下一词。通用迁移测试根据最新批配置验证旧队列、进度、备份和新增内容仅追加一次，无需每批复制测试。个人学习记录位于浏览器IndexedDB，构建与审计不读取该记录。

第十三批已完成215–234页，最后instrument233/w2427，下一批basis235/w2428。第六批23词和第九批153–154页缺口仍保留。
