# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:07:10 2018

题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例

@author: Administrator
"""

import urllib.request as r
import re
url='file:./全国招生计划表0206C正确.txt'
data=r.urlopen(url).read().decode('utf-8','ignore')
ls=re.compile('"plan":"(.*?)","uniname"').findall(data)
sum=0
for i in ls:
    sum+=int(i)
print('全国招生人数是：{}'.format(sum))


area={'黑龙江':'东北','吉林':'东北','辽宁':'东北','福建':'华东','江西':'华东','山东':'华东','上海':'华东','江苏':'华东','浙江':'华东','安徽':'华东','河南':'华中','湖北':'华中','湖南':'华中','广东':'华南','广西':'华南','海南':'华南','四川':'西南','贵州':'西南','云南':'西南','重庆':'西南','西藏':'西南','陕西':'西北','甘肃':'西北','青海':'西北','宁夏':'西北','新疆':'西北','北京':'华北','天津':'华北','山西':'华北','河北':'华北','内蒙古':'华北'}
areaplan={'东北':0,'华东':0,'华中':0,'华南':0,'西南':0,'西北':0,'华北':0}
sum=0
b={}
ls=[]
f=open('C:/Users/Administrator/全国招生计划表0206C正确.txt')
a=f.readlines()#将文本中的每行数据读入列表
import json
for i in range(len(a)):
    b[i]=json.loads(a[i])
for q in range(len(b)):
    if b[q]['status']==1:
        ls.append(b[q])
for m in range(59033):
    for k in range(len(ls[m]['data'])):
        city=ls[m]['data'][k]['city']
        areaplan[area[city]]=areaplan[area[city]]+int(ls[m]['data'][k]['plan'])
a=areaplan['东北']+areaplan['华北']+areaplan['华中']+areaplan['华南']+areaplan['华东']+areaplan['西北']+areaplan['西南']        
print('全国2300所学校：\n在东北招生:{}人\n在华东招生：{}人\n在华中招生:{}人\n在华南招生:{}\n在西南招生:{}人\n在西北招生:{}\n在华北招生:{}人\n全国招生人数：{}人'.format(areaplan['东北'],areaplan['华东'],areaplan['华中'],areaplan['华南'],areaplan['西南'],areaplan['西北'],areaplan['华北'],a))