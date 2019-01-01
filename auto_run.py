#!/usr/bin/env python
# encoding: utf-8
import os
import random
import pandas as pd
from datetime import datetime, timedelta, timezone

dd = pd.date_range('2019-01-01', '2019-01-05')
date_list = [pd.Timestamp(x).strftime("%Y-%m-%d") for x in dd.values]
for date in date_list:
	hour, minu, sec = random.randint(9,24), random.randint(0,60), random.randint(0,60)
	time = "{}T{}:{}:{}+08:00".format(date, str(hour), str(minu), str(sec))
	number = random.randint(0,10)
	os.system("echo {} >> README.md".format(time))
	os.system("echo {} >> README.md".format(str(number)))
	os.system("echo. >> README.md")
	for i in range(number):
		os.system("git add . && git commit -m 'update' --date={}".format(time))
		os.system('git push')
exit(0)




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
