# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:42:11 2018
练习五:实现练习四，
1.使用函数写出来。定义函数，输出每一天6:00,12:00,18:00的天气信息
2.打印折线图,使用字符串的*号操作
10----------
5-----

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

def msg(A):
    a=data['list'][A]['dt_txt']
    b=data['list'][A]['main']['temp']
    c=data['list'][A]['weather'][0]['description']
    d=data['list'][A]['main']['pressure']
    e=data['list'][A]['main']['temp_max']
    f=data['list'][A]['main']['temp_min']
    print("时间:{},温度是:{},天气情况是{},气压为{},最高温度为{},最低温度为{}".format(a,b,c,d,e,f))

msg(1)
msg(2)
msg(6)
msg(8)
msg(10)
msg(14)
msg(16)
msg(18)
msg(22)
msg(24)
msg(26)
msg(30)
msg(32)
msg(34)

print("*"*int(26.12))
print("*"*int(22.91))
print("*"*int(27.52))
print("*"*int(26.12))
print("*"*int(24.31))
print("*"*int(27.91))
print("*"*int(26.11))
print("*"*int(24.2))
print("*"*int(27.38))
print("*"*int(25.57))
print("*"*int(25.12))
print("*"*int(25.79))
print("*"*int(25.57))
print("*"*int(24.6))