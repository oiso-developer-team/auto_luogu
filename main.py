import requests as r
import time as t
import urllib.parse as u
import datetime
#import csv
#import math
import os
token = os.environ["token"]
txt="""**请认准 OIso | OI搜 唯一官方机器人账号 ！**

*仍在开发中*

------

今天的微博热搜：.weibotop.

更新时间（UTC）：.date.

动态主页支持：@George_jiang

------

🍋OIso🔍 - 一款为 OIer 和开发者而生的搜索引擎

https://www.oiso.cf/

前端开发： @diyanqi @Lotuses

后端开发： @diyanqi

本 bot 可在洛谷上通知您的 OIso 消息以及一些推广。如果您不想继续接受这些消息，请回复 `td` 。如果您想恢复接收消息，请回复 `hf` 。"""
cookies={"__client_id":token,"_uid":"464111"}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47 BOTE"}
txt=txt.replace(".weibotop.",r.get("https://tenapi.cn/v2/weibohot").text.split('"name": "')[1].split('",')[0])
txt=txt.replace(".date.",str(datetime.datetime.today()))
first=r.get("https://v1.hitokoto.cn/").text.split('"hitokoto":"')[1].split('","typ')[0]
re=r.get("https://www.luogu.com.cn/user/464111",headers=headers,cookies=cookies)
headers["X-CSRF-TOKEN"]=re.text.split('name="csrf-token" content="')[1].split('">\n')[0]
headers["Referer"]="https://www.luogu.com.cn/user/464111"
re=r.post("https://www.luogu.com.cn/api/user/updateIntroduction",json={"introduction":txt},headers=headers,cookies=cookies)
print(re)
re=r.post("https://www.luogu.com.cn/api/user/updateSlogan",json={"slogan":"OIso | OI搜 唯一官方机器人账号 | "+first},headers=headers,cookies=cookies)
print(re)
