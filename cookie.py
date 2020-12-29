##一个服务器怎么记住你是谁的，这就是cookie

##http请求是无状态的请求协议，不会记住用户的状态和信息，也不清楚你在这之前访问过什么
##因为网站需要记录用户是否登录时，就需要在用户登录后新建一些信息，并且要把这些信息记录在当前用户的浏览器中，记录的内容就是cookie
##用户使用当前浏览器继续访问这个服务器时，会主动携带这个网站设置的cookie信息

##cookie会在浏览器中记录信息，并且在访问时携带这个信息
#1.浏览器更换或删除cookie后，信息丢失
#2.cookie在浏览器中记录的信息是不安全的，因此不能记录敏感信息

###session
##session是在服务器端进行数据的记录，并且给每一个用户生成一个sessionID
##并且把这个sessionID设置在用户的浏览器中，也就是设置为cookie


import requests

#定义请求的url
url = 'https://www.amazon.cn/gp/css/homepage.html?ie=UTF8&ref_=nav_topnav_ya'   #亚马逊，不能直接访问

#定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    #可以访问没有登陆的网页，加入cookie
    'Cookie':'lc-acbcn=zh_CN; ubid-acbcn=459-6879343-4959245; session-id=458-8829392-3635305; x-acbcn=DtMqgbbyiKejJQLIlIWivBtMjQcQVhWVA88Tqavk7jyRSDuVLQlRlqCS39sfY2Ke; at-main=Atza|IwEBIH6BVO0WVRaJKEpjzXKYQntdN-e_MGqeG1nysRglsXmZp4-LfQLp297Fss-Q-kv8Jtt5MZoqDrhMPISUXSRBpB38IuBirX9vSu0s114O2y_czC0l-o66ENXGEd6aStIdxBXb-iAzAlkChGWYxOEasXJJhliS0-qxDUDs2GsA6hS-4p2Q-WX-RQccMIFrU-gn1J-zWfo_YE6wt4RdKS7ELig2; sess-at-main="IsMHyeucgsdbReCjJngPWDrKdIIZQifJGKrqA7P2dfc="; sst-main=Sst1|PQECaDpKA2AN8Jtq_mRxy_vFCVrC8z5IWZn18iKlYSkVtgqb-2nvO669NkrlnP0EBWeAWgnm1CdAHLHkyH2gorOd9T3A2VkR7dp5OYZ4Ysq_vgYIcoJ69bRVaWtfpjjp_s9PjuUCp2z2ujnc9UJhej0xAHl-PL_zYvzUrY-VFQCvk92dhF4m3ubzSUVgpD7-kwWLZ-pywPA0a1oHi8TnCtl0qQLFTtnpf5c_V69hGelAWkFn9s3yjETGpMRVSEj-lNZZnaK1cE21un_EkWuFwyHaUAR0ais9_T6k5NNHrrvvCzk; i18n-prefs=CNY; session-token="mCkXqeWVKWjUnTwmpJbnTP0ccaRmyZRpf44uVYO+rTh7sDjh7hC755MaeMn7535/XYYmuiQWNThvarmZVNj7jspeSHf39uW2LEgbsr3ARnqnwr8TGUh3T6jHTAANOcCU1eaDcHPa0tyxmvZw2/BR0CPyjk+pcSraxcgvsga+LufF3UKqBz4/MFSaHgmEs1KlrES1bHkys+hSXI8YTINkQQ=="; csm-hit=tb:SG28FR3JMPPZNKKTCN24+s-N9QGSMZ09MC7FTP2W31B|1604393550592&t:1604393550592&adb:adblk_no; session-id-time=2082729601l'
}

##主动设置cookie


#发起get请求
res = requests.get(url=url,headers=headers)

#获取响应状态码
code = res.status_code
print(code)

#响应成功后把响应的内容写入文件
if code == 200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)