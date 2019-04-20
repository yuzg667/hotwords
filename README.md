# hotwords
爬取 百度/360/新浪/搜狗 实时热搜词

示例演示：http://www.renyyy.com/hotwords/

#### 要求
- python 2.7
- BS4
- requests
	

#### 调用：

- 百度：getbaiduHotWord()

- 搜狗：rungetsougouHotword()

- 360：get360words()

- 微博：getweiboHotWord()

#### 返回结果都会以字典List形式返回：
[
{"num":1,"query":热搜词1,"heat":999,"jumpHref":http://123.html?k=111},

{"num":2,"query":热搜词2,"heat":888,"jumpHref":http://123.html?k=222}
]

