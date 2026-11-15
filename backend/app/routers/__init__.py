"""业务模块路由汇总。

这里统一按别名导入再暴露 ROUTERS：模块名有可能和内置名撞车（某个业务模块就叫 dict、list
这种名字时），按名字直接 import 会把内置类型覆盖掉，函数注解在运行时求值就会报
'module' object is not subscriptable。
"""
from __future__ import annotations

from app.routers import policy as router_policy
from app.routers import archive as router_archive
from app.routers import recall as router_recall
from app.routers import lifecycle as router_lifecycle
from app.routers import recycle as router_recycle
from app.routers import cost as router_cost
from app.routers import statistics as router_statistics
from app.routers import search as router_search
from app.routers import partition as router_partition
from app.routers import compress as router_compress
from app.routers import snapshot as router_snapshot
from app.routers import migrate as router_migrate
from app.routers import monitor as router_monitor
from app.routers import schedule as router_schedule
from app.routers import lineage as router_lineage
from app.routers import notify as router_notify
from app.routers import audit as router_audit
from app.routers import report as router_report

ROUTERS = [router_policy, router_archive, router_recall, router_lifecycle, router_recycle, router_cost, router_statistics, router_search, router_partition, router_compress, router_snapshot, router_migrate, router_monitor, router_schedule, router_lineage, router_notify, router_audit, router_report]
