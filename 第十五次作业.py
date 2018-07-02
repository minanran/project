# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:09:55 2018
题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
class Weather:
    #猴子对象产生的时候，会调用这个方法Monkey()
    def __init__(self,data,temp,description,pressure):#########系统固定的方法
        self.data=data
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):
        print("时间:"+self.data)
        print("温度:"+self.temp)
        print("天气情况:"+self.description)
        print("气压:"+self.pressure)
        print('\n')

for i in range(35):
    a=data['list'][i]['dt_txt']
    b=data['list'][i]['main']['temp']
    c=data['list'][i]['weather'][0]['description']
    d=data['list'][i]['main']['pressure']
    w=Weather(a,str(b),c,str(d))
    w.msg()
