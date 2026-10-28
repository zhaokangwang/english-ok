# English OK · 第一步数据样本

当前词库版本 vocabulary-0.13.0：1165个主要词条、2512个拆分词义、2175条例句，其中1607个词义可学习。第一单元165词、第二单元180词、第四单元189词、第六单元165词、第七单元182词主词已完整；第三单元164词仍缺第六批23词；第五单元120词仍缺第九批153–154页。第十三批PDF215 ease至233 instrument新增114词，234为第八单元扉页；下一批从235页basis开始。第九批续接断点compatible153/w1309保留。派生资料和待核实内容另存，音标未作外部词典复核。

## 先看内容

- [累计审阅稿](docs/sample-review.md)：单词、词义、例句、翻译、页码和疑点。
- [第二批审阅稿](docs/batch-002-review.md)：本轮新增60个主词。
- [第三批审阅稿](docs/batch-003-review.md)：sketch至hasty，新增85个主词，第一单元收尾。
- [第四批审阅稿](docs/batch-004-review.md)：第二单元agent至prevail，新增104个主词。
- [第五批审阅稿](docs/batch-005-review.md)：avail至stare，新增76个主词，第二单元收尾。
- [第六批审阅稿](docs/batch-006-review.md)：本次部分导入83词；[缺口清单](content/drafts/batch-006-missing.json)记录尚未导入的23词。
- [第七批审阅稿](docs/batch-007-review.md)：PDF95 coordinate至114 detect共105词，末词续至115页。
- [第八批审阅稿](docs/batch-008-review.md)：PDF115 spot至134 temper共111词，新增146项学习内容。
- [第九批审阅稿](docs/batch-009-review.md)：PDF135 personality至152 pioneer部分导入93词；[未完成页记录](content/drafts/batch-009-unprocessed.json)与[中断定位](docs/batch-009-interruption.md)。
- [第十批审阅稿](docs/batch-010-review.md)：PDF155 upset至174 occasion共104词，新增143项学习内容；170为第六单元扉页。
- [第十一批审阅稿](docs/batch-011-review.md)：PDF175 opportunity至194 confuse共109词，新增157项学习内容，均属第六单元。
- [第十二批审阅稿](docs/batch-012-review.md)：PDF195 refuse至214 alleviate共101词，新增139项学习内容；202为第七单元扉页。
- [第十三批审阅稿](docs/batch-013-review.md)：PDF215 ease至233 instrument共114词，新增151项学习内容，第七单元收尾；使用本机OCR辅助并逐页视觉核对。
- [批次清单](docs/batch-plan.md)、[导入规则](docs/import-rules.md)、[导入报告](docs/import-report.md)。
- 结构化输入：[第一批](content/sample.json)、[第二批](content/batches/batch-002.json)、[第三批](content/batches/batch-003.json)、[第四批](content/batches/batch-004.json)，由[批准清单](content/import-plan.json)累计合并。
- [来源清单](content/source-manifest.json)：原文件SHA256、页数、抽样范围。
- [关联素材](content/associated-material.json)：派生词例句，未混进主词学习任务。
- [质量清单](docs/quality-report.md)：待核实内容和缺例句的词义。
- [架构与限制](docs/architecture.md)：存储实现、迁移和未验证事项。
- [验证记录](docs/verification.md)：自动检查和桌面浏览器验证范围。

## 本地打开

依赖：Node.js 18+。运行资源已放在 web/vendor，无需公网即可启动：

```powershell
npm run dev
```

电脑打开 http://127.0.0.1:5173 。手机同一Wi-Fi测试使用：

```powershell
npm run dev:lan
```

打开终端显示的 Phone 地址。如防火墙拦截，仅允许需要的专用网络。按 Ctrl+C 停止。不要同时运行两个同端口服务。

上述命令是普通开发预览，不启用离线缓存。PWA 使用独立的构建目录和端口：

```powershell
npm run prepare:pwa
npm run preview:pwa
```

电脑打开 http://127.0.0.1:5174 ，在“设置 → 安装与离线使用”确认“离线资源已准备好”。之后可以停止服务，再从原地址打开检查离线使用。修改程序或词库后需重新运行 prepare:pwa；旧版本不会在学习过程中强制更新，结束学习并关闭所有同网址窗口后再打开。

iPhone 安装需要部署后的 HTTPS 网址，普通局域网 HTTP 不能替代 PWA 离线测试。手机首次缓存、主屏幕安装及系统分享均需真机验收；电脑测试不代替 iPhone 结果。当前数据仍保存在浏览器，程序不上传学习记录。没有发音音频。

实施步骤见 [PWA 方案](docs/pwa-implementation-plan.md)，当前验收进度见 [PWA 验收记录](docs/pwa-verification.md)，安装和发布操作见 [PWA 使用说明](docs/pwa-guide.md)。

## 数据文件

- web/data/vocabulary.sqlite：可重复生成的累计词库，当前1165词。
- web/data/learning.sqlite：空白模板，不能当成用户正在使用的数据库。
- 实际个人记录：浏览器IndexedDB english-ok-sqlite，页面可导出JSON或SQLite。
- 不要清除网站数据；换网址或换设备前先导出JSON，再在新环境导入。
- 导入会替换本地学习记录；不会合并两个设备的记录。

## 重建与检查

首次准备或依赖更新需要联网安装；正常运行无CDN请求：

```powershell
npm ci
npm run prepare:web
```

Python 3.11+与pypdf用于从现有PDF重新生成来源清单和数据库：

```powershell
python scripts/build_data.py
npm test
```

build_data.py读取批准清单中的输入，验证身份和关联后发布累计词库，不会覆盖浏览器个人进度。seed_sample.py与transcribe_batch*.py是最初转录脚本，通常不重新运行，以免覆盖后续人工修改的JSON。原PDF保持不变；渲染图片在tmp/pdfs。

第十三批起复用[通用导入工具](scripts/import_batch.py)和[批次配置](scripts/batch013-config.json)。本机OCR使用Windows自带简体中文识别，文字与坐标缓存在tmp/pdfs，缓存按图片SHA256和语言校验；音标、词义映射和跨页内容仍需视觉核对。完整步骤见[导入流程](docs/import-workflow.md)。

正在学习的旧队列不会自动重排，完成后可点击“继续学习新增内容”。新用户会读取当前全部可学习词义。仍未实现正式按日任务。

导入检查：

```powershell
python -m unittest discover -s tests -p "test_*.py"
```

当前测试覆盖SQLite字节重开、事务回滚、备份恢复、坏备份拒绝、内容更新不覆盖进度、演示复习间隔。iPhone和安卓真机需另外验证，不以桌面测试替代。
