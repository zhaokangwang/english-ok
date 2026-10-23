# PDF词库分批导入规则 v1

## 权威输入与范围

原始PDF不修改，SHA256固定在content/import-plan.json。正式构建用清单指定的文件名/来源，不从目录任意选第一份PDF。批次清单见batch-plan.md与content/batch-ledger.json。已批准的输入才放入import-plan.json；未审核候选不要注册成正式输入。

batch-001保留content/sample.json，batch-002使用独立JSON，不能把新数据直接追加进旧的人工转录脚本。普通构建不运行seed_sample.py或transcribe_batch002.py；它们是首次转录记录，重跑会覆盖相应编辑稿。

## 处理一批的操作顺序

1. 确定主体页与前后衔接页，按单词开始位置分配批次，跨页读到结束；查看跨栏和派生框。
2. 渲染页面并逐页核对。本轮使用人工视觉转录，没有自动OCR；以后若使用OCR，要保留未经编辑的输出并写明引擎及方法，不能冒充人工核对完成。
3. 为新主词分配未使用ID；拆出词义、例句、原译、记忆辅助、派生关系和页码。继续使用格式w0081等，正式分配后不随文本修改重算。
   同时在content/units.json中登记书本单元归属；单元不同于导入工作批次，每个主词必须且只能归属一个单元。未全部收录的单元标记complete=false，不按词条ID或工作批次猜测单元。
4. 先查累计词库：同词重复出现需要有明确的编辑合并记录，保留旧ID；当前导入器遇重复拼写会拒绝，不猜测自动合并。
5. 对照扫描页检查词形、音标、否定词、数字、译文归属、原书标签。例句实际使用的词形须能在英文的目标位置找到。
6. 匹配本句实际词义。缺句的词义ready=false；疑似错句review_status=pending；错挂词条、疑似错译留在associated文件标为quarantined，不自动修正或编补。
7. 输出批次审阅稿，确认页范围与疑点。加入批准清单，再运行build_data.py；失败停止，不覆盖已发布SQLite。
8. 检查import-report.json、quality-report.md、批次审阅稿并运行测试；刷新页面查看新增词条，确认旧学习轮次与记录保留。

## ID和校对约定

- id-registry.json记录已发布的身份关系。已有word的拼写、sense的所属词、example的所属词义以及related的关系对象不能复用或悄悄改挂。
- 同一ID的翻译和说明可以校正；词义语义实质变化、删除、合并要另做显式迁移，当前导入器不支持此类修改。
- 原书综合释义保存在source_definition；senses是编辑按语境拆分，不冒充原书原始分类。
- visual_checked只表示已对照扫描页，不代表外部词典或真题出处核实；音标仍需专项复核。
- 派生、短语、记忆联想分别记录。每批associated文件保留关联句/隔离句，不直接进入主词学习队列。
- 本书当前抽样范围PDF页与书内页相差8，仍要逐批查看；后续偏移变化应显式修改校验规则，不能沿用错误页码。

## 发布与学习进度

构建过程累计读取批准批次，在内存生成SQLite，并用foreign_key_check检查。对照已发布数据库和ID注册表确认没有删除/复用，再通过同目录staging文件原子替换词库。重复执行不会重复插入。runtime/vocabulary.previous.sqlite保留上一次不同版本，更新失败可手动恢复；报告和JSON并非多文件事务，SQLite文件为应用运行依据。跨版本正式回滚需要人工核对ID兼容，不自动降级。

learning.sqlite仍是空白模板；真实个人记录在浏览器IndexedDB。内容构建不会读写它。旧备份导入新词库时按引用ID校验，接受兼容的旧内容版本。

正在进行的队列保持不变，包括游标、原有词义顺序。完成后才显示“继续学习新增内容”，将尚未进入队列、尚无学习进度的可用词义追加；旧任务不重排。新用户初始队列读取当前全部可学习词义。这仍是试用队列，不是正式按日任务或到期复习系统。

## 本地命令

```powershell
python scripts/build_data.py
python -m unittest discover -s tests -p "test_*.py"
npm test
```

Python需pypdf。本机若python路径未配置，可使用Codex自带Python。脚本不下载模型，不向公网上传PDF或用户数据。
