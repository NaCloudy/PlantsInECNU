#bs4解析源码
#from urllib.request import urlopen
#from bs4 import BeautifulSoup

##data = json.loads(resp.text)

#爬取网页
#myHtml = urlopen("https://tree.sjtusv.com/trees?habit=%E4%B9%94%E6%9C%A8&order=&search=&owner=all&limit=20&offset=0")
#解析文件
#bsObj = BeautifulSoup(myHtml.read(), "html.parser")
#打印div字段
#print(bsObj)
from __future__ import unicode_literals
import requests

url = "https://tree.sjtusv.com/trees?limit=&offset=0"

#const Authorization = 'Bearer '+ wx.getStorageSync('token')
headers= {
    "Host": "tree.sjtusv.com",
    "Connection" : "keep-alive",
    "Authorization": "Bearer xxxx",
    "referer" : "https://servicewechat.com/xxxx.html", 
    "xweb_xhr" : "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)xxxx", 
    "content_type" : "application/json"
    } 
resp = requests.get(url, verify=False, headers = headers)


#解析为json并存储
resp_json = resp.json()
#resp_json_rep = resp_json.replace('\xa0', ' ')
import json

filename = '524full_data.json'  #文件路径   

with open(filename, 'w', encoding="utf-8") as f_obj:#打开模式为可写
	json.dump(resp_json, f_obj, ensure_ascii=False)  #存储文件