#!/usr/bin/env python
# visit https://tool.lu/pyc/ for more information
# Version: Python 3.7

import sys
import os
import time
import datetime
import win32api
import win32con
print('使用说明：按要求输入关机时间')
curtime = datetime.datetime.now()
curtime_hour = curtime.hour
curtime_minute = curtime.minute
print(curtime_hour, ':', curtime_minute)
input_time_hourandoff = input('请输入小时(如果需要取消关机，输入 "cancel")：')
if input_time_hourandoff == 'cancel':
    if os.system('shutdown -a') == 1116:
        print('因为没有任何进行中的关机过程，所以无法中止系统关机。(1116)')
    else:
        print('取消成功')
else:
    input_time_hour = 23
    input_time_minute = 0
    hours = input_time_hour - curtime_hour
    if input_time_minute >= curtime_minute:
        minutes = input_time_minute - curtime_minute
        minutes += hours * 60
    else:
        minutes = input_time_minute + 60 - curtime_minute
        hours -= 1
        minutes += hours * 60
    seconds = minutes * 60
    print(seconds)
    print('距离关机还有%d分钟' % minutes)
    os.system('shutdown -s -t %d' % seconds)
    print("设置成功，如果想取消关机，打开程序输入：'cancel' 即可")
