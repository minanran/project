# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:11:17 2018

@author: Administrator
"""

ls=[]
ls1=[]
ls2=[]
ls3=[]
import re
import urllib.request as r
for i in range(10):
    url='https://movie.douban.com/top250?start={}&filter= '.format(25*i)
    data='start={}&filter='.format(25*i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    pat='class="">\n\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s\s<span class="title">(.*?)</span>'
    pat1='<a href="https://movie.douban.com/subject/(.*?)/" class="">'
    #pat1='https://movie.douban.com/subject/(.*?)/" '
    ls=re.compile(pat,re.S).findall(d)##电影名字
    ls2=re.compile(pat1,re.S).findall(d)###电影ID
    for i in ls2:
        ls3.append(i[0:7]) #######ID切片     
    for j in range(25):
        ls1.append(ls[j])
for ln in range(len(ls1)):
    print('{}————电影:{}---{}'.format(ln,ls1[ln],ls3[ln]))



##########################################

ls5=[] 
ls8=[]   
import urllib.request as r#导入联网工具包，命令为r
import re
for i in ls3:
    url1='http://movie.douban.com/subject/{}/'
    url=url1.format(i)
    req=r.Request(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    data=r.urlopen(req).read().decode('utf-8')
    pat2='<span class="pl">类型:</span> <span property="v:genre">(.*?)</span> / <span property="v:genre">(.*?)</span> / <span property="v:genre">(.*?)</span> / <span property="v:genre">(.*?)</span><br/>'
    ls4=re.compile(pat2,re.S).findall(data)
    ls6=str(ls4).replace('(','').replace(')','')
    ls7=ls6.split(',')
    ls8.append(ls7[1])
    for i in ls8:
        ls5.append(i)
#<span class="pl">类型:</span> <span property="v:genre">爱情</span> / <span property="v:genre">科幻</span> / <span property="v:genre">动画</span> / <span property="v:genre">冒险</span><br/>    


          
f=open('./mm.txt','w')#csv表格文件，以逗号分割
for i in range(250):
    f.write("{}--电影名称：{}\n".format(i,ls1[i]))
f.close()#关闭文件，保存文件       
               
f=open('./mm.txt','r')
ls=f.readlines() 
def xuhao(s):
    ls=open('./mm.txt','r').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split('--')[0]:
            abc=i.split('--')[1]
            break
    return abc
shuzi=input("以下APP为您推荐的人生必看一百部电影，请您输入您感兴趣电影的序号：")    
xuhao=xuhao(shuzi)
print(xuhao)      