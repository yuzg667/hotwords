# -*- coding: utf-8 -*-
'''
获取微博热搜词
Author:yuzg667
https://github.com/yuzg667/hotwords
'''
import requests
from bs4 import BeautifulSoup
import re

def getweiboHotWord():
    header  =  {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.9",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Host":"s.weibo.com",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

    }   
    url = "https://s.weibo.com/top/summary?cate=realtimehot"  #请求地址
    r = requests.get(url,headers=header)
    html = r.text

    s = BeautifulSoup(html,"lxml") 
    #获取页面内所有的热搜词的html
    hotwords = s.find_all("td", class_="td-02")
    
    i = 0
    resDictList = []
    for hotword in hotwords:
        #正则取
        hotword = str(hotword) #正则必须是string
        
        patternQuery = re.compile(r'''target="_blank">(.*?)</a>''')
        query = re.findall(patternQuery,hotword)
        
        patternHeat = re.compile(r'''<span>(.*?)</span>''')
        heat = re.findall(patternHeat,hotword)
        
        patternJumpHref = re.compile(r'''<a href="(.*?)" target="_blank">''')
        jumpHref = re.findall(patternJumpHref,hotword)
       
        if len(query)>0 and len(jumpHref)>0: #有返回空的情况，过滤掉
            
            jumpHref = "https://s.weibo.com" + str(jumpHref[0])
            if len(heat)<1:
                heat = ["置顶"]
            resDict = {"num":str(i+1),"query":query[0],"heat":heat[0],"jumpHref":jumpHref}

            resDictList.append(resDict)
        i = i + 1
    return (resDictList)

# res = getweiboHotWord()
# print(res)
