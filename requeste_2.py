import requests

#定义请求的url
#url = 'https://www.lmonkey.com/'
#url = 'https://www.xicidaili.com/nn'  #一个服务器代理网站  这里由于对方拒绝，不能接入
#url = 'https://music.163.com/'  #网易云
url = 'https://www.amazon.cn/'   #亚马逊，不能直接访问

#对于不能直接爬虫的网站，我们要定义请求头信息
#定义请求头信息
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    #身份表明,其实是套了一个别的浏览器的外壳
}

#发起get请求
res = requests.get(url=url,headers=headers) #,

#获取响应状态码
code = res.status_code
print(code)

#响应成功后把响应的内容写入文件
if code == 200:
    with open('./test.html','w',encoding='utf-8') as fp:
        fp.write(res.text)