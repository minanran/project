# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 11:03:14 2018
############题目
题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
（3.下载图片。想做就做）

@author: Administrator
"""
import urllib.request as r#导入URL工具包 并且命令为r
myconn=r.urlopen('http://www.baidu.com')
if myconn.getcode()==200:
    data=myconn.read().decode('utf-8')
    print(data)
else:
    print('无法访问此网站')
myconn.close()

"""
raise RemoteDisconnected("Remote end closed connection without"
RemoteDisconnected: Remote end closed connection without response
爬虫里面非常关键的：反爬虫
1.直接屏蔽程序爬取数据
2.如果访问对方服务器次数过大，对方会屏蔽你的IP/屏蔽十分钟....
"""
import urllib.request as r#导入URL工具包 并且命令为r
req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')
pat='<div class="content">(.*?)</div>'
import re
ls=re.compile(pat,re.S).findall(data)

url='https://pic.qiushibaike.com/system/pictures/11292/112920206/medium/app112920206.jpg'
r.urlretrieve(url,'./tmp.jpg')#retrieve下载文件

#############################
import urllib.request as r#导入URL工具包 并且命令为r
for i in range(13):
    req=r.Request('https://www.qiushibaike.com/8hr/page/{}/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
            #req=r.Request('https://www.qiushibaike.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'})
    nur=r.urlopen(req)
    print(nur.getcode())
    data=nur.read().decode('utf-8')
    pat1='alt="(.*?)"'
    pat2='<div class="content">\n<span>\n\n(.*?)</span>\n\n</div>\n</a>\n<!-- 图片或gif -->'
    import re
    ls1=re.compile(pat1,re.S).findall(data)
    ls2=re.compile(pat2,re.S).findall(data)
    for j in range(len(ls2)):
        print('作者名：{}\n糗事：{}'.format(ls1[j],ls2[j]).replace('<span>',''))
