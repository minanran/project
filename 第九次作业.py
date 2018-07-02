# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:59:40 2018
题目九：余票查询组项目
1.查询某种火车的余票，动车，高铁，直达，特快....
2.组长将各组员功能汇总

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']

p='  '
s="v8hzesw92snv0p%2BXbBSYcvDvrkZJongII6gnHaa1K%2B5ZLSH2S1yiEmi5TocBRsVZ7KheRoWRj4s2%0AVRYp%2F1qQIXo6MxxZNB3giUuTVVn2qCjkK0zSOEIvJTiliIOKVW5rcQneIukZPdBmkyTOIosb%2FhFD%0AtpChpGqPNAY%2F29y3VTJO4Sh51LMePmFmF7Hv7THUyJDqN5VO5lYhnC611uP65vpluqQm243rAtJw%0AYiIa3SmEBr%2FXR331dZJkt7EmP3dw|预订|76000C630407|C6304|IXW|JFW|IVW|CNW|09:46|10:47|01:01|Y|NiY4S31uZETanTCgYyNeHA1zyfhqgCHmfzE%2B20yxLvYgcLOY|20180625|3|W1|02|06|1|0|||||||有||||无|无|||O0M0O0|OMO|0"
s=data[0]
ls=s.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(15).replace('[','').replace(']',''),end='')

#print('车次')
#print('ab')

s='N%2FySZswGXDqQPNR7KNqFwdBzvUwW%2Bl82FYFZ2hPdxUzg7dzpUdnAg2pq834pT2qxTxBpKYtUuHR0%0A%2FnW0SyuTkQBbT%2F4eQ77ZOW%2BtoKzu3wXAhd4uf4mUaXR1Yse3VS12QsN8ldXNn0NHYVwhbd7O2eW4%0AllD120G3NZiO%2FJsOiBpLp4zQ4QDtmRuAjMw9DdUyAs1m5xmrupP%2BsBCvBsljceSxMbjrmB2Pq2Gd%0ANnbvHm71zWRAdhG33ssxwkoMBNBU|预订|2400000G890B|G89|BXP|ICW|BXP|ICW|06:53|14:41|07:48|Y|I6f4%2F%2FVjmDh8FowzPFKFCfA38qy9Ynseatx1cYr0%2BTgDl0aA|20180626|3|P4|01|05|1|0|||||||||||有|19|1||O0M090|OM9|0'
ls2=s.split('|')

s='6nMecwwn%2FmtGuiPXKYxmT0FbbWWTvjF2UAaua033kdXVop408GE72Z0Fufh9%2BpIuEhIljbPBM5to%0AeTNk4ueWtfua5a3rTPfElUhDj2nUJsIc10AB%2B2Z6qteAs%2FcxgwcacnCL2RrIk3ECIB828Dc8NgOT%0Afl9aA60YO3fhi7afiBmwG6dGzDZNrBeuJsf19kj2%2FGIV9RwIle2l5ZSEE%2BnrJNZ6KPk3x9jmrzul%0Ana%2BW5R%2BKhCVf1klsJh0DiJcOC331|预订|240000G1010F|G101|VNP|AOH|VNP|NKH|06:43|11:14|04:31|Y|anKuw6ZIFPhViJi9kL%2Bo3KEA4Mj6oqybYA9LVMScFH3GP0MH|20180717|3|P2|01|08|1|0|||||||||||有|有|9||O0M090|OM9|0'
ls3=s.split('|')




########西安到上海
import urllib.request as r#导入联网工具包，命令为r
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-06-29&leftTicketDTO.from_station=XAY&leftTicketDTO.to_station=SHH&purpose_codes=ADULT'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data=data['data']['result']
p='  '
s1="|预订|950000T20603|T206|YMR|SHH|XAY|SHH|00:47|17:49|17:02|N|vNbLfYN1UkFU71ncpyx190l4VfEUebfBaRooFxUx6vGBQNFPPaxGKWJXbn8%3D|20180627|3|R1|21|32|0|0||||无|||无||无|无|||||10401030|1413|0"
#s2="rmyBiCdaPScy0uNADsY%2BXS2enzE6kJuyhHeFWXG2gU3p9iWJEPEoMaUnizXPpQwzn6%2F%2F8hPFbHEs%0A5QQvsZtY1nWF4EFPh0GJMyM3UOHJW4TToKSyIzgY6yT2LLilGEqPwioTBPbkAf2M2cKhnNK3RPYE%0AXI0IAM3BPmLrjH2rn9rEZY4wLsR%2BZIU%2BdRQLr8tecFCCXx7dQW48LeUXVegHlPhWYOn9cioc81Ky%0AfD%2FZAEIePCC8k5Cpsaz9qZ%2BSNMzgWtMuyQ%3D%3D|预订|850000T11850|T118|LZJ|SHH|XAY|SHH|20:15|13:30|17:15|Y|aFKi2sgCiF7OU1%2BvZSkfVaI4TijBOKFxJdN%2BvszX%2BsjE1RMpRJ%2BYXgZq9DU%3D|20180629|3|J1|06|16|0|0||||无|||无||无|12|||||10401030|1413|0" #17
s1=data[0]
ls=s1.split('|')
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站/到达站{}出发时间/到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(12),end='')
print()
#车次   车发站，到达站 出发时间,到达时间 历时间
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
for i in ls:
    print(str(i).center(13).replace('[','').replace(']',''),end='')



f=open('./T.csv','w')#csv表格文件，以逗号分割
f.write('车次,出发站/到达站,出发时间/到达时间,历时,商务座/特等座,一等座,二等,高级软卧,软卧,动卧,硬卧,软座,硬座,无座,其他,备注\n')
ls=[ls[3],[ls[6],ls[7]],[ls[8],ls[9]],ls[10],ls[32],ls[31],ls[30],'--','--','--','--','--','--',ls[26],'--',ls[1]]
f.close()#关闭文件，保存文件
