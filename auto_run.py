#!/usr/bin/env python
# encoding: utf-8
import os
from datetime import datetime, timedelta, timezone

# 删除最后一行
os.system("sed -i '$d' README.md")

# 添加日期
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
os.system('echo "Last update : {}" >> README.md'.format(bj_dt.strftime('%Y-%m-%d %H:%M:%S')))

# git相关操作
os.system('git add README.md')
os.system('git commit -m "update"')
os.system('git push')

# crontab命令: 0 */1 * * * cd /path/to/auto-commit && python3 auto_run.py
