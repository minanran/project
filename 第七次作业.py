# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:51:06 2018
练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。
@author: Administrator
"""

data=json.loads(data)
#data 字典-》list 列表-》index 0 字典-》main 字典-》temp_max temp_min temp
temp_max=data['list'][0]['main']['temp_max']
temp_min=data['list'][0]['main']['temp_min']
temp=data['list'][0]['main']['temp']
dt_txt=data['list'][0]['dt_txt']
print("日期是：{},温度是：{}，最高温度是：{}，最低温度是：{}".format(dt_txt,temp,temp_max,temp_min))
#如果temp_max<20，适合穿冬装;temp_max>30,适合穿秋装
if True:
    print('冬装')
    
if temp_max<20:
    print('冬装')

if temp_max>20:
    print('秋装')
    
    
des='多云'
if des=='多云':
    print('xxxx')
if des=='小雨':
    print('请记得带伞哦')
if des=='龙卷风':
    print('适合待在防空洞')
    
print(int(10)*"-")
print(int(18)*"-")
print(int(20)*"-")
print(int(5)*"-")

#############################调试
for i in [1,2,3]:
    print(i)
    for j in [0.1,0.2,0.3]:
        print(j)
print('end')
###############################################闪屏
print('\n'.join([''.join([('weather'[(x-y) % len('weather')]if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(30, -30, -1)])) 
ls=['温馨提示：请每天观看天气预报']
for i in range(20):
    print('*'*20,ls,'*'*20)