# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:43:57 2018
练习六：获取淘宝数据并且展示(只要第一页的商品44个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出11排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%A4%E5%AD%90&bcoffset=-3&ntoffset=-3&p4ppushleft=1%2C48&s=132&ajax=true'

data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
for i in range(44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][i]['nick']
    e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    print('商品名称：{}\n，售价：{}\n，付款人数：{}\n，店铺名称：{}]\n，店铺地址：{}\n '.format(a,b,c,d,e))
    
for i in range(11):
    for j in range(4):
        a=data['mods']['itemlist']['data']['auctions'][j+i*4]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][j+i*4]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][j+i*4]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][j+i*4]['nick']
        e=data['mods']['itemlist']['data']['auctions'][j+i*4]['item_loc']
        f=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
        print('商品名称：{}\n 售价：{}\n 付款人数：{}\n 店铺名称：{}\n 店铺地址：{}\n 邮费情况: {}\n'.format(a,b,c,d,e,f))     
    print('\n...................................................')

f=open('./c.csv','w')#csv表格文件，以逗号分割
for i in range(44):
    f.write('商品名称：{}\n 售价：{}\n 付款人数：{}\n 店铺名称：{}\n 店铺地址：{}\n 邮费情况: {}\n'.format(a,b,c,d,e,f))
f.close()#关闭文件，保存文件      
    

#ls=sorted(ls) #列表排序(默认是升序)
#ls1=reversed(ls) #列表的倒序(不是列表)
ls=[]
for i in range(44):
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    f=float(b)
    ls.append(f)
    l=sorted(ls,reverse=True)
print(l)

    
ls=[]
for i in range(44):
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    h=int(c[:-3])
    ls.append(h)
    ls1=sorted(ls)
print(ls1)


for i in range(44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    f=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if (f=='0.00'):
        print('商品名称：{} ，售价：{}======包邮'.format(a,b))