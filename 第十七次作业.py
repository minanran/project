# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:06:00 2018

第十七题

@author: Administrator
"""

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With': 'XMLHttpRequest'}
req=r.Request(url,headers=headers,data='id=477&type=2&city=23&state=1'.encode())
data=r.urlopen(req).read().decode('utf-8','ignore')

#东北
#黑龙江	吉林 	辽宁
area={'黑龙江':'东北','吉林':'东北','辽宁':'东北'}
areaplan={'东北':0}
areaplan['东北']=areaplan['东北']+8
###########通过下面定义多个变量赋值，计算出中国地区的人数
a=0
b=0
c=0
if '东北'==plan:
   a=a+1 

import json
data=json.loads(data)

for i in range(142600):
    if data['status']==1:
        ls=data['data']
    for school in ls:
        city=school['city']
        print(area[city])
        print(int(school['plan']))
        areaplan[area[city]]=areaplan[area[city]]+int(school['plan'])
        
#d='id=477&type=2&city=23&state=1'.encode()#bytes
#
#print(d)
#print(type(d))
###########################################        
f=open('./广西文科数据.txt')
ls=f.readlines()#将所有的文本中的每行读取到一个列表中去
for line in ls:
    print(line)
ls2=[]
import json
for i in ls:
    i=json.loads(i)
    ls2.append(i)

ls5=[]
for i in range(2300):
    if ls2[i]['status']==1:
        ls3=ls2[i]['data']
        for j in range(len(ls3)):
            school=ls3[j]['school']
            profess=ls3[j]['profess']
            renshu=ls3[j]['plan']
            renshu=int(renshu)
            print("{}的 {}专业在广西招文科生{}人：".format(school,profess,renshu))
            ls5.append(renshu)
 
sum=0
for i in ls5:
    sum+=i
print("全国2300所大学在广西共招文科生 {} 人".format(sum))