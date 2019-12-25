#!/usr/bin/env python
# encoding: utf-8
import os
import random
import pandas as pd
from datetime import datetime, timedelta, timezone

dd = pd.date_range('2019-12-23', '2019-12-25')
date_list = [pd.Timestamp(x).strftime("%Y-%m-%d") for x in dd.values]
for date in date_list:
	number = random.randint(0,5)
	os.system("echo {} commit {} times >> README.md".format(str(number)))
	hours = sorted([random.randint(8,23) for _ in range(number)])
	for hour in hours:
		minu, sec = random.randint(0,60), random.randint(0,60)
		time = "{}T{}:{}:{}+08:00".format(date, str(hour), str(minu), str(sec))
		os.system("echo {} >> README.md".format(time))

		os.system("git add . && git commit -m 'update' --date={}".format(time))
		os.system('git push')

exit(0)

# crontab命令: 0 */1 * * * cd /path/to/auto-commit && python3 auto_run.py
