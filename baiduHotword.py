# -*- coding: utf-8 -*-
'''
获取百度热搜词
Author:yuzg667
https://github.com/yuzg667/hotwords
'''
import requests
from bs4 import BeautifulSoup
import re

def getbaiduHotWord():
    header  =  {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"en-US,en;q=0.9",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Host":"top.baidu.com",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

    }   
    url = "http://top.baidu.com/buzz?b=1&fr=topindex"
    r = requests.get(url,headers=header)
    html = r.text.encode('iso-8859-1').decode('gbk')   #中文乱码处理，非常重要    print (html)

    s = BeautifulSoup(html,"lxml") 
    #获取页面内所有的热搜词的html
    hotwords = s.find_all("tr") #oneline
    
    i = 0
    resDictList = []
    for hotword in hotwords:
        #正则取
        hotword = str(hotword) #正则必须是string
        patternQuery = re.compile(r'''target="_blank">(.*?)</a>''')
        query = re.findall(patternQuery,hotword)
        
        patternHeat = re.compile(r'''">(.*?)</span>''')
        heat = re.findall(patternHeat,hotword)
        
        if len(query)>0 and len(heat)>0: #有返回空的情况，过滤掉
             
            jumpHref = "https://www.baidu.com/baidu?cl=3&tn=SE_baiduhomet8_jmjb7mjw&rsv_dl=fyb_top&fr=top1000&wd=" + str(query[0])
            resDict = {"num":str(i+1),"query":query[0],"heat":heat[-1],"jumpHref":jumpHref}

            resDictList.append(resDict)
            i = i + 1
    return (resDictList)




