# 冷热数据分层归档中心

面向海量数据存储成本优化、冷热分层判定、自动归档调度、归档检索回温与生命周期回收的冷热数据分层归档中心。

这是一个前后端分离的管理平台：前端 React + Vite + TypeScript，后端 FastAPI（Python）。
两边各自独立启动，前端 dev server 已关掉自动打开页面，启动后按终端打印的地址手工打开。

## 目录结构

```text
.
├── frontend/                 React + Vite + TypeScript 前端
│   ├── src/views/            每个业务模块一个页面
│   ├── src/api/              统一请求封装
│   ├── src/stores/           会话与筛选状态
│   └── vite.config.ts        dev server 配置（open: false）
├── backend/                  FastAPI（Python） 后端
│   ├── app/routers/          每个业务模块一组接口
│   ├── app/services/         业务规则与状态流转
│   └── app/store.py          内存数据仓库与示例数据
├── .gitignore
└── docker-compose.yml
```

## 启动

### 后端

```bash
cd backend
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
./run.sh
```

健康检查：`curl http://127.0.0.1:8000/api/health`

### 前端

```bash
cd frontend
npm install
npm run dev
```

前端默认监听 `http://127.0.0.1:5173/`，dev server 不会自动打开浏览器，
需要自己访问。`/api` 由 vite 代理到后端 `http://127.0.0.1:8000`。

## 业务模块

| 模块 | 目录 | 业务对象 | 主要字段 |
| --- | --- | --- | --- |
| 分层策略 | `policy` | 策略配置 | 策略编号、目标表名、冷热判定字段 |
| 归档任务 | `archive` | 归档作业 | 作业编号、目标表名、分区范围 |
| 数据回温 | `recall` | 回温请求 | 请求编号、目标表名、分区条件 |
| 生命周期 | `lifecycle` | 生命周期规则 | 规则编号、目标表名、创建天数 |
| 数据回收 | `recycle` | 回收策略 | 策略编号、目标表名、回收条件 |
| 成本计量 | `cost` | 计量记录 | 记录编号、表名、存储类型 |
| 访问统计 | `statistics` | 统计指标 | 指标编号、目标表名、访问次数 |
| 归档检索 | `search` | 检索请求 | 请求编号、关键字、文件范围 |
| 分区治理 | `partition` | 分区方案 | 方案编号、目标表名、分区字段 |
| 压缩管理 | `compress` | 压缩策略 | 策略编号、目标表名、压缩算法 |
| 回收快照 | `snapshot` | 快照记录 | 快照编号、源表名、分区范围 |
| 数据搬迁 | `migrate` | 搬迁任务 | 任务编号、源存储、目标存储 |
| 归档监控 | `monitor` | 监控指标 | 指标编号、关联策略、归档延迟 |
| 调度管理 | `schedule` | 调度计划 | 计划编号、关联任务、调度表达式 |
| 版本追溯 | `lineage` | 版本记录 | 记录编号、目标表名、变更类型 |
| 事件通知 | `notify` | 通知规则 | 规则编号、触发事件、通知渠道 |
| 操作审计 | `audit` | 审计日志 | 日志编号、操作类型、操作对象 |
| 统计报告 | `report` | 报告模板 | 模板编号、报告名称、统计维度 |

## 约定

- 每个模块的前端页面在 `frontend/src/views/<模块>/index.vue`，后端接口在
  `backend/app/routers/<模块>.py`，业务规则在 `backend/app/services/<模块>.py`。
- 列表接口统一返回 `{ items, total, page, size }`，动作接口统一返回 `{ ok, message }`。
- 状态流转只允许在 `app/services` 里改，路由层不做业务判断。

领域：数据工程
子方向：数仓与数据湖
