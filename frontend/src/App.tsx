import { useState } from 'react'
import { Link, Route, Routes } from 'react-router-dom'

import Overview from './views/Overview'
import PolicyView from './views/policy'
import ArchiveView from './views/archive'
import RecallView from './views/recall'
import LifecycleView from './views/lifecycle'
import RecycleView from './views/recycle'
import CostView from './views/cost'
import StatisticsView from './views/statistics'
import SearchView from './views/search'
import PartitionView from './views/partition'
import CompressView from './views/compress'
import SnapshotView from './views/snapshot'
import MigrateView from './views/migrate'
import MonitorView from './views/monitor'
import ScheduleView from './views/schedule'
import LineageView from './views/lineage'
import NotifyView from './views/notify'
import AuditView from './views/audit'
import ReportView from './views/report'

const navItems = [{ label: "运营概览", path: "/" }, { label: "分层策略", path: "/policy" }, { label: "归档任务", path: "/archive" }, { label: "数据回温", path: "/recall" }, { label: "生命周期", path: "/lifecycle" }, { label: "数据回收", path: "/recycle" }, { label: "成本计量", path: "/cost" }, { label: "访问统计", path: "/statistics" }, { label: "归档检索", path: "/search" }, { label: "分区治理", path: "/partition" }, { label: "压缩管理", path: "/compress" }, { label: "回收快照", path: "/snapshot" }, { label: "数据搬迁", path: "/migrate" }, { label: "归档监控", path: "/monitor" }, { label: "调度管理", path: "/schedule" }, { label: "版本追溯", path: "/lineage" }, { label: "事件通知", path: "/notify" }, { label: "操作审计", path: "/audit" }, { label: "统计报告", path: "/report" }]

export default function App() {
  const [operator] = useState('值班管理员')

  return (
    <div className="app-shell">
      <aside className="app-side">
        <h1 className="app-title">冷热数据分层归档中心</h1>
        <nav className="nav-list">
          {navItems.map((item) => (
            <Link key={item.path} to={item.path} className="nav-item">
              {item.label}
            </Link>
          ))}
        </nav>
      </aside>
      <main className="app-main">
        <header className="app-head">
          <span className="head-desc">面向海量数据存储成本优化、冷热分层判定、自动归档调度、归档检索回温与生命周期回收的冷热数据分层归档中心。</span>
          <span className="head-user">当前值班：{operator}</span>
        </header>
        <Routes>
          <Route path="/" element={<Overview />} />
          <Route path="/policy" element={<PolicyView />} />
          <Route path="/archive" element={<ArchiveView />} />
          <Route path="/recall" element={<RecallView />} />
          <Route path="/lifecycle" element={<LifecycleView />} />
          <Route path="/recycle" element={<RecycleView />} />
          <Route path="/cost" element={<CostView />} />
          <Route path="/statistics" element={<StatisticsView />} />
          <Route path="/search" element={<SearchView />} />
          <Route path="/partition" element={<PartitionView />} />
          <Route path="/compress" element={<CompressView />} />
          <Route path="/snapshot" element={<SnapshotView />} />
          <Route path="/migrate" element={<MigrateView />} />
          <Route path="/monitor" element={<MonitorView />} />
          <Route path="/schedule" element={<ScheduleView />} />
          <Route path="/lineage" element={<LineageView />} />
          <Route path="/notify" element={<NotifyView />} />
          <Route path="/audit" element={<AuditView />} />
          <Route path="/report" element={<ReportView />} />
        </Routes>
      </main>
    </div>
  )
}
