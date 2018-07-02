# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:56:15 2018

第八题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
f=open('./cq.csv','w')
f.write('商品名称，售价，付款人数，店铺名称，店铺地址\n')
for i in range(100):
    url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%87%8D%E5%BA%86&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(i*44)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data) 
    for m in range(len(data['mods']['itemlist']['data']['auctions'])):
        a=data['mods']['itemlist']['data']['auctions'][m]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][m]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][m]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][m]['nick']
        e=data['mods']['itemlist']['data']['auctions'][m]['item_loc'] 
        f.write("{},{},{},{},{}\n".format(a,b,c,d,e))

f.close()#关闭文件，保存文件

    
 ###########      
 
from scipy.stats import mode
ls=[]
for i in range(100):
    url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%87%8D%E5%BA%86&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(i*44)
    data=r.urlopen(url).read().decode('utf-8')
    if data=='':
        continue
    import json
    data=json.loads(data) 
    for m in range(len(data['mods']['itemlist']['data']['auctions'])):
        b=data['mods']['itemlist']['data']['auctions'][m]['view_price']  
        f=float(b)
        ls.append(f)
mode(ls)

##max(ls.count(x) for x in set(ls))


import numpy as np
np.mean(ls)##平均数
np.median(ls)##中位数



