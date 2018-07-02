# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:02:07 2018
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=python&rsv_pq=878faa350000a626&rsv_t=bd10Kodu3kpNLZRB8LXox7zVKXJ%2F1vfHhRE1a4CoHJcqNBN%2BZrbf%2Fg%2BMOHM&rqlang=cn&rsv_enter=1&rsv_sug3=1&rsv_sug1=1&rsv_sug7=001'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls1=re.compile('"title":"(.*?)"').findall(data)##爬取百度搜索标题
ls2=re.compile('<div class="c-abstract">(.*?)</div>').findall(data)##爬取标题下的描述
ls3=re.compile('style="text-decoration:none;">(.*?)&nbsp').findall(data)##搜索的标题的网站
for i in range(len(ls1)):
    print("第{}个网址标题是：{}\n".format(i,ls1[i]))    
#ls2=re.compile('class="c-abstract">"(.*?)"').findall(data)
for j in range(len(ls2)):
    print("第{}个标题下的描述是：{}\n".format(j,ls2[j]))
for m in range(len(ls3)):
    print("第{}个标题的网站是：{}\n".format(m,ls3[m]))