# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:00:53 2018
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序

@author: Administrator
"""

def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#北京
from_station=hanzi_to_pin(from_station)
to_station=input('到达站')#成都
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)









#将火车站三字码替换成城市名map{}
ls=open('C:/Users/Administrator/火车站编码.csv','r',encoding='utf-8').readlines()
def bianma(s):
    ls=open('C:/Users/Administrator/火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc
import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日')
from_station=input('出发站')#北京
from_station=bianma(from_station)
to_station=input('到达站')#成都
to_station=bianma(to_station)
print(date,from_station,to_station)
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')#网址不换行
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

p='  '
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
orderls=[]
for i in title:
    print(i.center(13),end='')
for i in range(len(data['data']['result'])):
    s=data['data']['result'][i]
    ls=s.split('|')
    ls[6]=data['data']['map'].get('{}'.format(ls[6]))
    ls[7]=data['data']['map'].get('{}'.format(ls[7]))
    ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--',ls[23],'--',ls[36],'--',ls[29],ls[26],'--',ls[1]]
    orderls.append(ls)
#车次   车发站，到达站 出发时间,到达时间 历时间

    for i in ls:
        print(str(i).center(15).replace('[','').replace(']',''),end='')#第一小问
##历时排序
x=lambda item:int(item[3].split(':')[0])*60+int(item[3].split(':')[1])
orderls.sort(key=x)   

