# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:31:42 2018
第三题：
1.通过复制联网代码获得天气(老家)字典数据
2.打印温度temp,天气情况description,天气气压pre

@author: Administrator
"""


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/weather?q=chongqing&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
print('桂林温度是:{}'.format(data['main']['temp']))
print('桂林气压是:'+str(data['main']['pressure']))
print('桂林天气情况是:'+str(data['weather'][0]['description']))
##或
d=data['weather']
print('桂林天气情况是:'+str(d[0]['description']))