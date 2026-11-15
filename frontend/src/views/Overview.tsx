import { useEffect, useState } from 'react'

import { fetchJson } from '@/api/client'

type Overview = {
  cards: { label: string; value: number }[]
  modules: { name: string; created: number; pending: number; abnormal: number }[]
}

const fallbackCards = [{"label": "业务模块", "value": 0}, {"label": "今日新增", "value": 0}]
const fallbackModules = [{"name": "分层策略", "created": 0, "pending": 0, "abnormal": 0}, {"name": "归档任务", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据回温", "created": 0, "pending": 0, "abnormal": 0}, {"name": "生命周期", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据回收", "created": 0, "pending": 0, "abnormal": 0}, {"name": "成本计量", "created": 0, "pending": 0, "abnormal": 0}, {"name": "访问统计", "created": 0, "pending": 0, "abnormal": 0}, {"name": "归档检索", "created": 0, "pending": 0, "abnormal": 0}, {"name": "分区治理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "压缩管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "回收快照", "created": 0, "pending": 0, "abnormal": 0}, {"name": "数据搬迁", "created": 0, "pending": 0, "abnormal": 0}, {"name": "归档监控", "created": 0, "pending": 0, "abnormal": 0}, {"name": "调度管理", "created": 0, "pending": 0, "abnormal": 0}, {"name": "版本追溯", "created": 0, "pending": 0, "abnormal": 0}, {"name": "事件通知", "created": 0, "pending": 0, "abnormal": 0}, {"name": "操作审计", "created": 0, "pending": 0, "abnormal": 0}, {"name": "统计报告", "created": 0, "pending": 0, "abnormal": 0}]

export default function Overview() {
  const [cards, setCards] = useState<Overview['cards']>(fallbackCards)
  const [moduleRows, setModuleRows] = useState<Overview['modules']>(fallbackModules)

  useEffect(() => {
    fetchJson<Overview>('/api/overview')
      .then((payload) => {
        setCards(payload.cards)
        setModuleRows(payload.modules)
      })
      .catch(() => undefined)
  }, [])

  return (
    <section className="page">
      <header className="page-head">
        <div>
          <h2>运营概览</h2>
          <p className="page-desc">汇总各业务模块的关键指标，先看总量再看异常。</p>
        </div>
      </header>
      <div className="stat-row">
        {cards.map((card) => (
          <article key={card.label} className="stat-card">
            <span className="stat-label">{card.label}</span>
            <strong className="stat-value">{card.value}</strong>
          </article>
        ))}
      </div>
      <table className="data-table">
        <thead>
          <tr><th>业务模块</th><th>今日新增</th><th>待处理</th><th>异常量</th></tr>
        </thead>
        <tbody>
          {moduleRows.map((row) => (
            <tr key={row.name}>
              <td>{row.name}</td>
              <td>{row.created}</td>
              <td>{row.pending}</td>
              <td>{row.abnormal}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  )
}
