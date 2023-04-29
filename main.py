import requests as r
import time as t
import urllib.parse as u
import csv
import math
import os
token = os.environ["token"]
# 先实现登录
f=open("a.txt","w")
cookies={"__client_id":token,"_uid":"459900"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47"}
got=r.get("https://www.luogu.com.cn/problem/list?type=P&page=1", headers=headers,cookies=cookies)
msg=got.text.split('window._feInjection = JSON.parse(decodeURIComponent("')[1].split('            window._feConfigVersion =')[0]
temp2=u.unquote(msg)
fullpage=int(temp2.split('s":{"count":')[1].split(',"r')[0])
print("done")
for i in range(1,math.ceil(fullpage/50)+1):
    got=r.get("https://www.luogu.com.cn/problem/list?type=P&page={}".format(i), headers=headers,cookies=cookies)
    try:
        for j in range(1,51):
            msg=got.text.split('<li>')[j].split('&nbsp;<a')[0]
            f.write(msg+"\n")
    except:
        print("done")
    t.sleep(0.8)#这行是最最关键的一句代码，千万千万不要删除！
f.close()
data=[]
f=open("a.txt","r")
que=f.read().split("\n")
for i in que:
    if i=='':
        break
    got=r.get("https://www.luogu.com.cn/problem/solution/{}".format(i), headers=headers,cookies=cookies)
    msg=got.text.split('window._feInjection = JSON.parse(decodeURIComponent("')[1].split('            window._feConfigVersion =')[0]
    temp2=u.unquote(msg)
    msg=temp2.split('},"acceptSolution":')[1].split('},"')[0]
    t.sleep(0.8)#这行是最最关键的一句代码，千万千万不要删除！
    got2=r.get("https://www.luogu.com.cn/problem/{}".format(i), headers=headers,cookies=cookies)
    msg2=got2.text.split('window._feInjection = JSON.parse(decodeURIComponent("')[1].split('            window._feConfigVersion =')[0]
    temp3=u.unquote(msg2)
    if msg=="true":
        data.append(["P",i,1,temp2.split('"difficulty":')[1].split(',')[0],temp3.split(',"tags":')[1].split(',"')[0].replace('"', '')])
    else:
        data.append(["P",i,0,temp2.split('"difficulty":')[1].split(',')[0],temp3.split(',"tags":')[1].split(',"')[0].replace('"', '')])
    t.sleep(0.8)#这行是最最关键的一句代码，千万千万不要删除！
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for row in data:
        writer.writerow(row)
