"""接口出入参模型：列表分页、动作结果与各模块的明细结构。"""
from __future__ import annotations

from typing import Any, Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class PageResult(BaseModel, Generic[T]):
    items: list[T]
    total: int
    page: int = 1
    size: int = 20


class ActionResult(BaseModel):
    ok: bool
    message: str
    entry: dict[str, Any] | None = None


class EntryPayload(BaseModel):
    """登记或修改一条业务记录时提交的字段集合。"""

    values: dict[str, Any] = Field(default_factory=dict)
    remark: str | None = None



class PolicyEntry(BaseModel):
    """策略配置明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 冷热判定字段
    field_3: str | None = None  # 热存储天数
    field_4: str | None = None  # 温存储天数
    field_5: str | None = None  # 冷归档天数
    field_6: str | None = None  # 回收天数
    field_7: str | None = None  # 判定表达式

class ArchiveEntry(BaseModel):
    """归档作业明细结构。"""

    field_0: str | None = None  # 作业编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 分区范围
    field_3: str | None = None  # 归档介质
    field_4: str | None = None  # 压缩算法
    field_5: str | None = None  # 加密开关
    field_6: str | None = None  # 校验方式
    field_7: str | None = None  # 保留天数

class RecallEntry(BaseModel):
    """回温请求明细结构。"""

    field_0: str | None = None  # 请求编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 分区条件
    field_3: str | None = None  # 回温优先级
    field_4: str | None = None  # 期望完成时间
    field_5: str | None = None  # 回温介质
    field_6: str | None = None  # 索引重建
    field_7: str | None = None  # 通知策略

class LifecycleEntry(BaseModel):
    """生命周期规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 创建天数
    field_3: str | None = None  # 活跃判定
    field_4: str | None = None  # 静默天数
    field_5: str | None = None  # 降冷触发
    field_6: str | None = None  # 归档触发
    field_7: str | None = None  # 回收触发

class RecycleEntry(BaseModel):
    """回收策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 回收条件
    field_3: str | None = None  # 保留快照
    field_4: str | None = None  # 快照份数
    field_5: str | None = None  # 删除确认
    field_6: str | None = None  # 恢复窗口
    field_7: str | None = None  # 执行频率

class CostEntry(BaseModel):
    """计量记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 表名
    field_2: str | None = None  # 存储类型
    field_3: str | None = None  # 占用字节
    field_4: str | None = None  # 存储单价
    field_5: str | None = None  # 周期费用
    field_6: str | None = None  # 计费区间
    field_7: str | None = None  # 优化建议

class StatisticsEntry(BaseModel):
    """统计指标明细结构。"""

    field_0: str | None = None  # 指标编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 访问次数
    field_3: str | None = None  # 查询次数
    field_4: str | None = None  # 扫描行数
    field_5: str | None = None  # 时间粒度
    field_6: str | None = None  # 最近访问
    field_7: str | None = None  # 统计周期

class SearchEntry(BaseModel):
    """检索请求明细结构。"""

    field_0: str | None = None  # 请求编号
    field_1: str | None = None  # 关键字
    field_2: str | None = None  # 文件范围
    field_3: str | None = None  # 时间范围
    field_4: str | None = None  # 排序条件
    field_5: str | None = None  # 返回最大条数
    field_6: str | None = None  # 检索超时
    field_7: str | None = None  # 结果格式

class PartitionEntry(BaseModel):
    """分区方案明细结构。"""

    field_0: str | None = None  # 方案编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 分区字段
    field_3: str | None = None  # 分区粒度
    field_4: str | None = None  # 分区范围
    field_5: str | None = None  # 桶数量
    field_6: str | None = None  # 小文件合并
    field_7: str | None = None  # 过期淘汰

class CompressEntry(BaseModel):
    """压缩策略明细结构。"""

    field_0: str | None = None  # 策略编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 压缩算法
    field_3: str | None = None  # 压缩级别
    field_4: str | None = None  # 触发阈值
    field_5: str | None = None  # 解压开销
    field_6: str | None = None  # 压缩时间窗
    field_7: str | None = None  # 重压缩策略

class SnapshotEntry(BaseModel):
    """快照记录明细结构。"""

    field_0: str | None = None  # 快照编号
    field_1: str | None = None  # 源表名
    field_2: str | None = None  # 分区范围
    field_3: str | None = None  # 快照时间
    field_4: str | None = None  # 快照大小
    field_5: str | None = None  # 存储介质
    field_6: str | None = None  # 过期时间
    field_7: str | None = None  # 恢复校验

class MigrateEntry(BaseModel):
    """搬迁任务明细结构。"""

    field_0: str | None = None  # 任务编号
    field_1: str | None = None  # 源存储
    field_2: str | None = None  # 目标存储
    field_3: str | None = None  # 表范围
    field_4: str | None = None  # 分区范围
    field_5: str | None = None  # 搬迁并发
    field_6: str | None = None  # 校验模式
    field_7: str | None = None  # 搬迁状态

class MonitorEntry(BaseModel):
    """监控指标明细结构。"""

    field_0: str | None = None  # 指标编号
    field_1: str | None = None  # 关联策略
    field_2: str | None = None  # 归档延迟
    field_3: str | None = None  # 回温延迟
    field_4: str | None = None  # 成功率
    field_5: str | None = None  # 错误率
    field_6: str | None = None  # 监控频率
    field_7: str | None = None  # 告警级别

class ScheduleEntry(BaseModel):
    """调度计划明细结构。"""

    field_0: str | None = None  # 计划编号
    field_1: str | None = None  # 关联任务
    field_2: str | None = None  # 调度表达式
    field_3: str | None = None  # 时区
    field_4: str | None = None  # 并发上限
    field_5: str | None = None  # 超时终止
    field_6: str | None = None  # 依赖检查
    field_7: str | None = None  # 通知策略

class LineageEntry(BaseModel):
    """版本记录明细结构。"""

    field_0: str | None = None  # 记录编号
    field_1: str | None = None  # 目标表名
    field_2: str | None = None  # 变更类型
    field_3: str | None = None  # 变更前
    field_4: str | None = None  # 变更后
    field_5: str | None = None  # 操作时间
    field_6: str | None = None  # 操作人
    field_7: str | None = None  # 回滚脚本

class NotifyEntry(BaseModel):
    """通知规则明细结构。"""

    field_0: str | None = None  # 规则编号
    field_1: str | None = None  # 触发事件
    field_2: str | None = None  # 通知渠道
    field_3: str | None = None  # 接收列表
    field_4: str | None = None  # 消息模板
    field_5: str | None = None  # 合并窗口
    field_6: str | None = None  # 重复抑制
    field_7: str | None = None  # 优先级

class AuditEntry(BaseModel):
    """审计日志明细结构。"""

    field_0: str | None = None  # 日志编号
    field_1: str | None = None  # 操作类型
    field_2: str | None = None  # 操作对象
    field_3: str | None = None  # 操作详情
    field_4: str | None = None  # 操作来源
    field_5: str | None = None  # 执行时间
    field_6: str | None = None  # 影响范围
    field_7: str | None = None  # 回滚能力

class ReportEntry(BaseModel):
    """报告模板明细结构。"""

    field_0: str | None = None  # 模板编号
    field_1: str | None = None  # 报告名称
    field_2: str | None = None  # 统计维度
    field_3: str | None = None  # 报告周期
    field_4: str | None = None  # 导出格式
    field_5: str | None = None  # 推送渠道
    field_6: str | None = None  # 水印设置
    field_7: str | None = None  # 自动生成
