# -*- coding: utf-8 -*-
'''
获取360热搜词
Author:yuzg667
https://github.com/yuzg667/hotwords
'''
import requests
import json

def get360words():
    header  =  {
            "Accept":"application/json, text/plain, */*",
            "Accept-Encoding":"gzip, deflate, br",
            "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
            "Connection":"keep-alive",
            "Host":"trends.so.com",
            "Referer":"https://trends.so.com/hot",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "X-Requested-With":"XMLHttpRequest"
    }   
    url = "https://trends.so.com/top/realtime"
    r = requests.get(url,headers=header)
    s = r.text
    s = s.encode('utf-8').decode('unicode_escape') #py2.7  3.6+
    s = json.loads(s)
    
    resDictList = []
    i = 0
    for resultList in s["data"]["result"]:
        query = s["data"]["result"][i]['query']
        heat = s["data"]["result"][i]['heat']
        jumpHref = 'https://www.so.com/s?ie=utf-8&src=zhishu&q=' + query

        resDict = {"num":str(i+1),"query":query,"heat":heat,"jumpHref":jumpHref}
        resDictList.append(resDict)
        i = i +1
        if i >100:
            break
    return (resDictList)

# res = get360words()
# print(res)
