# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:02:44 2018
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=guilin,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#print(data)
import re
ls1=re.compile('"description":"(.*?)"').findall(data)##天气描述
ls2=re.compile('"temp":(.*?)"').findall(data)##天气温度
ls3=re.compile('"pressure":(.*?)"').findall(data)##天气气压
print("桂林未来5天的天气描述是：{}".format(ls1))
print("桂林未来5天的天气温度是：{}".format(ls2))
print("桂林未来5天的天气气压是：{}".format(ls3))