# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:40:58 2018
第四题：求出未来5天天气
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
4.根据温度打印出问题折线图
    28——————————————————————————————
    30——————————————————————————————————
    10——————————————————
5.打印出其他10个城市的天气，计算出天气排名，按着大到小的顺序。

@author: Administrator
"""


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》list列表-》index 0 字典-》main字典-》temp变量
#data字典-》list列表-》index 0 字典-》main字典-》temp_max变量

print('桂林6.21 温度是',data['list'][0]['main']['temp'])
print('重庆6.21 温度是',data['list'][0]['main']['temp'])
print('长沙6.21 温度是',data['list'][0]['main']['temp'])
print('上海6.21 温度是',data['list'][0]['main']['temp'])
print('深圳6.21 温度是',data['list'][0]['main']['temp'])
print('广州6.21 温度是',data['list'][0]['main']['temp'])
print('汉口6.21 温度是',data['list'][0]['main']['temp'])
print('北京6.21 温度是',data['list'][0]['main']['temp'])
print('青岛6.21 温度是',data['list'][0]['main']['temp'])
print('河南6.21 温度是',data['list'][0]['main']['temp'])
ls=[]
a=sorted(ls)
ls=[26.12,26.42,23.16,28.85,30.29,32.17,22.44,34.67,32.84,16.19]
sorted(ls)
sorted(ls,reverse=True)

name=data['city']['name']
print('城市{}:'.format(name))
dt_txt=data['list'][0]['dt_txt']
temp=data['list'][0]['main']['temp']
description=data['list'][0]['weather'][0]['description']
pressure=data['list'][0]['main']['pressure']
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
#q11=data['list'][0]['weather'][0]['main']
#print("时间:{},的温度是:{},天气情况是{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,pressure,temp_max,temp_min))#英文版
dt_txt=data['list'][2]['dt_txt']
temp=data['list'][2]['main']['temp']
description=data['list'][2]['weather'][0]['description']
pressure=data['list'][2]['main']['pressure']
temp_max=data['list'][2]['main']['temp_max']
temp_min=data['list'][2]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
print("-" * 100)
dt_txt=data['list'][6]['dt_txt']
temp=data['list'][6]['main']['temp']
description=data['list'][6]['weather'][0]['description']
pressure=data['list'][6]['main']['pressure']
temp_max=data['list'][6]['main']['temp_max']
temp_min=data['list'][6]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][8]['dt_txt']
temp=data['list'][8]['main']['temp']
description=data['list'][8]['weather'][0]['description']
pressure=data['list'][8]['main']['pressure']
temp_max=data['list'][8]['main']['temp_max']
temp_min=data['list'][8]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][10]['dt_txt']
temp=data['list'][10]['main']['temp']
description=data['list'][10]['weather'][0]['description']
pressure=data['list'][10]['main']['pressure']
temp_max=data['list'][10]['main']['temp_max']
temp_min=data['list'][10]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
print("-" * 100)
dt_txt=data['list'][14]['dt_txt']
temp=data['list'][14]['main']['temp']
description=data['list'][14]['weather'][0]['description']
pressure=data['list'][14]['main']['pressure']
temp_max=data['list'][14]['main']['temp_max']
temp_min=data['list'][14]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][16]['dt_txt']
temp=data['list'][16]['main']['temp']
description=data['list'][16]['weather'][0]['description']
pressure=data['list'][16]['main']['pressure']
temp_max=data['list'][16]['main']['temp_max']
temp_min=data['list'][16]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][18]['dt_txt']
temp=data['list'][18]['main']['temp']
description=data['list'][18]['weather'][0]['description']
pressure=data['list'][18]['main']['pressure']
temp_max=data['list'][18]['main']['temp_max']
temp_min=data['list'][18]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
print("-" * 30)
dt_txt=data['list'][22]['dt_txt']
temp=data['list'][22]['main']['temp']
description=data['list'][22]['weather'][0]['description']
pressure=data['list'][22]['main']['pressure']
temp_max=data['list'][22]['main']['temp_max']
temp_min=data['list'][22]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][24]['dt_txt']
temp=data['list'][24]['main']['temp']
description=data['list'][24]['weather'][0]['description']
pressure=data['list'][24]['main']['pressure']
temp_max=data['list'][24]['main']['temp_max']
temp_min=data['list'][24]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][26]['dt_txt']
temp=data['list'][26]['main']['temp']
description=data['list'][26]['weather'][0]['description']
pressure=data['list'][26]['main']['pressure']
temp_max=data['list'][26]['main']['temp_max']
temp_min=data['list'][26]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
print("-" * 100)
dt_txt=data['list'][30]['dt_txt']
temp=data['list'][30]['main']['temp']
description=data['list'][30]['weather'][0]['description']
pressure=data['list'][30]['main']['pressure']
temp_max=data['list'][30]['main']['temp_max']
temp_min=data['list'][30]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][32]['dt_txt']
temp=data['list'][32]['main']['temp']
description=data['list'][32]['weather'][0]['description']
pressure=data['list'][32]['main']['pressure']
temp_max=data['list'][32]['main']['temp_max']
temp_min=data['list'][32]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
dt_txt=data['list'][34]['dt_txt']
temp=data['list'][34]['main']['temp']
description=data['list'][34]['weather'][0]['description']
pressure=data['list'][34]['main']['pressure']
temp_max=data['list'][34]['main']['temp_max']
temp_min=data['list'][34]['main']['temp_min']
des=data['list'][0]['weather'][0]['main']
print("时间:{},的温度是:{},天气情况是{},英文描述{},气压为{},最高温度为{},最低温度为{}".format(dt_txt,temp,description,des,pressure,temp_max,temp_min))
print("*"*int(temp))
if temp_max > 26:
    print('合适穿夏装T恤或裙子，多喝水')
if temp_max < 26:
    print('合适穿秋装长袖，建议备外套')
    
if description=="多云":
    print("合适外出，合适晾衣服")
if description=="小雨":
    print("建议外出小雨带雨伞")
if description=="中雨":
    print("建议不外出或有事外出带雨伞")
if description=="阴":
    print("比较合适出门游玩")
print("-" * 100)