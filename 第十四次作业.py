# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:04:27 2018
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定

@author: Administrator
"""

import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
###############################################1问
import urllib.request as r
url='file:///C:/Users/Administrator/all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
import re
ls=re.compile('daxue-jianjie-(.*?).html').findall(data)
ls1=re.compile('(.*?)\t.*\t').findall(data)
for i in range(len(ls1)):
    print('{}学校网址编号ID是：{}'.format(ls1[i],ls[i]))
###########################################################2问
import urllib.request as r
req=r.Request('http://www.gaokaopai.com/daxue-zhaosheng-477.html',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
myurl=r.urlopen(req)
#print(myurl.getcode())
data=myurl.read().decode('utf-8')
import re
pat="claimCity', (.*?)>(.*?)<"
ls1=re.compile(pat,re.S).findall(data)
for i in range(len(ls1)):
    print('{}的编号是：{}'.format(ls1[i][1],ls1[i][0][0:2]))
#####################################################################3问2300所大学在广西招的文科生
import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#f=open('./数据.txt','w',encoding='utf-8')
ls2=[]
for i in range(len(ls)):
    data='id={}&type=1&city=45&state=1'.format(ls[i]).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    ls2.append(d)
    #f.write('{}\n'.format(d))
    print('{}成功获取'.format(ls[i]))
#f.close()#关闭文件，保存文件

for j in range(2300):
    a=ls2[j]
    if a.startswith('<!DOCTYPE html>'):
        print('第{}存在错误'.format(i))    
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html '
        data='id={}&type=1&city=45&state=1'.format(ls[j])
        data=data.encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d2=r.urlopen(req).read().decode('utf-8','ignore')
        ls2[j]=d2


f=open('./tang.txt','w')
for i in ls2:
    f.write(i+"\n")
f.close()
