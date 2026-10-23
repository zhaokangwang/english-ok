# 本地词库与学习数据：样本阶段

第五批更新：词库版本vocabulary-0.5.0，共345主词、680词义、635例句（474词义可学习）。第一单元165词、第二单元180词，均complete=true；这里的完整仅指主词条覆盖。第五批PDF59–74按单元边界提前结束；下一批从第三单元扉页PDF75及正文76的origin开始。学习库结构及用户记录不变，旧队列完成后显式追加新增词义。以下各批更新段落为历史记录。

第四批更新：词库版本vocabulary-0.4.0，共269主词、523词义、485例句（360词义可学习）。第一单元165词，第二单元104词且complete=false；学习库及用户记录结构不变。下一批从PDF59页avail开始。

第三批更新：第一单元PDF10–38的165个主词已导入；词库版本vocabulary-0.3.0。含335个拆分词义、292条主词例句（218个词义可学习），派生资料和疑点另存。单元complete仅指主要词条覆盖完成，不表示所有派生词都已有独立卡片或已完成外部词典复核。

更新：已导入batch-002，累计80主词、171词义、136例句。批次内容见import-rules.md及import-report.md；下文的20词描述是最初样本阶段记录。当前新增内容在旧队列完成后显式追加，保持原ID和个人记录。

词库呈现更新：vocabulary结构v2增加units、unit_words，单元归属来自content/units.json；学习库结构仍为v1，个人进度不变。当前80词均属于第一单元（尚未完整收录）。词库按单元展开双栏中英列表，点击可查看详情并返回原列表位置。

## 当前实现

网页为无构建依赖的存储验证页，不是完整背词产品。没有接入 AI、登录、服务器数据库或远程资源。Node 静态服务只提供 web/，不会暴露项目 PDF、源码目录或个人数据库。

词库为 SQLite 文件，使用 Python 标准 sqlite3 生成。网页通过本地 sql.js/WASM 打开。学习库在内存 SQLite 中执行事务，再将完整字节持久化到 IndexedDB。样本规模使用整库快照足够；大量历史记录后需重新评估写入开销。

写入只有 IndexedDB 事务完成后才提示成功。持久化失败回退内存状态；revision 检查阻止多个页面用旧快照覆盖新记录。浏览器数据以 origin（协议、主机、端口）隔离，换 IP/端口不是自动迁移。私密浏览和清理网站数据不保证保留记录。

## 迁移到 App

分层：页面 app.mjs → core.mjs（查询、进度、事务、备份）→ SQLite 与 BrowserStore。未来采用 Capacitor 原生 SQLite 插件时，保留 SQL 表结构、固定 ID、备份格式和复习规则；另实现异步 SQL 执行适配，替换当前同步 sql.js 调用。当前没有实现或验证原生插件，不声称业务代码可原样直接运行。

跨设备以版本化 JSON 备份为约定。词库和学习库独立，可导出 SQLite 学习库用于审计；当前页面仅导入 JSON，不导入任意 SQLite。导入为整库替换，不做跨设备合并。先校验再事务替换，持久化失败同样回滚。删除、合并词义尚未提供自动映射；遇到不存在的引用会拒绝导入，保留原记录。

## 表结构

- vocabulary：sources / words / senses / examples / related_words / metadata。
- learning：profiles / settings / progress / review_events / sessions / metadata。
- progress 的主键为 (profile_id, sense_id)；例句使用派生词时不自动归入主词。
- review_events 保存逐次反馈；sessions 保存队列和游标。一次反馈三者同事务更新。
- 时间采用 UTC ISO 字符串，设置另存 Asia/Shanghai；当前验证页不实现按日任务。
- schema v1、内容 sample-0.1.0、复习 interval-demo-v1、备份 v1 各自独立。
- 当前仅有 v1 初始化；不伪造未发生的升级。未来新增顺序 migration，事务升级 user_version；不支持的版本拒绝打开，不能重置已有数据。

## 内容质量边界

20个主要词条，39个编辑拆分词义，34条例句，另有派生/关联材料。并非5500完整词表。来源为PDF第10–13页（书内002–005）。直接看扫描图人工转录，没有安装或运行自动OCR。sample.json与seed_sample.py为编辑整理稿，不是原始OCR；原始证据是未修改PDF及tmp/pdfs中的页面渲染。

visual_checked 仅表示对照扫描图检查，不等于外部词典或真题出处验证。原书标签“真题”不附加未经核实年份。音标统一为IPA重音符号，需后续复核。e0004-01 保留原书 the resign，pending且不参与学习。conduct 多音按词性保留在 source_definition，phonetic 为空。关联材料文件目前作为人工审阅资料，未入主词学习队列。

## 尚需实际设备验证

- iPhone Safari 的 IndexedDB 保存、关闭重开、导入导出及存储空间不足。
- 安卓原生 SQLite 与数据迁移。
- 浏览器跨页竞争写入实际行为。
- HTTPS PWA离线启动（尚未实现）。局域网HTTP试用依赖电脑运行静态服务；App内置资源后才能摆脱电脑。
