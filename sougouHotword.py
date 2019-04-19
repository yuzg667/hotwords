# -*- coding: utf-8 -*-
'''
获取搜狗实时热点
Author:yuzg667
https://github.com/yuzg667/hotwords
'''
import requests
from bs4 import BeautifulSoup
import re

def getsougouHotWord(url,num,classTag,k):
    header  =  {
                "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                "Accept-Encoding":"gzip, deflate",
                "Accept-Language":"en-US,en;q=0.9",
                "Cache-Control":"max-age=0",
                "Connection":"keep-alive",
                "Host":"top.sogou.com",
                "Upgrade-Insecure-Requests":"1",
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36"

    }   
    r = requests.get(url,headers=header)
    r.encoding = 'utf-8'
    html = r.text

    s = BeautifulSoup(html,"lxml") 
    #获取页面内所有的热搜词的html
    hotwords = s.find_all("li", class_=classTag) #oneline
    
    i = 0
    resDictList = []
    for hotword in hotwords:
        #正则取
        hotword = str(hotword) #正则必须是string
        patternQuery = re.compile(r'''target="_blank">(.*?)</a>''')
        query = re.findall(patternQuery,hotword)
        patternHeat = re.compile(r'''<span class="s3">(.*?)<i class=''')
        heat = re.findall(patternHeat,hotword)
        patternJumpHref = re.compile(r'''<a href="(.*?)" target="_blank">''')
        jumpHref = re.findall(patternJumpHref,hotword)
       
        if len(query)>0 and len(jumpHref)>0: #有返回空的情况，过滤掉
            
            jumpHref = str(jumpHref[0])
            if len(heat)<1:
                heat = ["置顶"]
            resDict = {"num":str(num+1),"query":query[k],"heat":heat[0],"jumpHref":jumpHref}

            resDictList.append(resDict)
        i = i + 1
        num = num + 1
    return (resDictList)


def rungetsougouHotword():
    num1=0 #Top1
    url1 = "http://top.sogou.com/hot/shishi_1.html"
    classTag1 = "one"
    k1 = 1
    res1 = getsougouHotWord(url=url1,num=num1,classTag=classTag1,k=k1)
    
    num2=1 #Top2
    url2 = "http://top.sogou.com/hot/shishi_1.html"
    classTag2 = "two"
    k2 = 1
    res2 = getsougouHotWord(url=url2,num=num2,classTag=classTag2,k=k2)
    
    num3=2 #Top3
    url3 = "http://top.sogou.com/hot/shishi_1.html"
    classTag3 = "three"
    k3 = 1
    res3 = getsougouHotWord(url=url3,num=num3,classTag=classTag3,k=k3)
    
    num4=3 #第一页除了3个top的另外七个
    url4 = "http://top.sogou.com/hot/shishi_1.html"
    classTag4 = "oneline"
    k4 = 0
    res4 = getsougouHotWord(url=url4,num=num4,classTag=classTag4,k=k4)
    
    num5=10 #第2页的全部10个
    url5 = "http://top.sogou.com/hot/shishi_2.html"
    classTag5 = "oneline"
    k5 = 0
    res5 = getsougouHotWord(url=url5,num=num5,classTag=classTag5,k=k5)
    
    num6=20 #第3页的全部10个
    url6 = "http://top.sogou.com/hot/shishi_3.html"
    classTag6 = "oneline"
    k6 = 0
    res6 = getsougouHotWord(url=url6,num=num6,classTag=classTag6,k=k6)
    
    res = res1  + res2 + res3 + res4 + res5 + res6

    return(res)


# ress = rungetsougouHotword()
# print(ress)