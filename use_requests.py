import requests

#定义请求的url
url = 'https://www.baidu.com/'

#发起get请求
res = requests.get(url=url)

#获取响应结果
print(res)   #<Response [200]>
print(res.content)  #b'...',是二进制的文本流
print(res.content.decode('utf-8'))  #<!DOCTYPE html> 把二进制的文本流按照utf8的字符集转化为普通字符串
print(res.text)  #获取响应的内容，与content一样
print(res.headers)  #响应头信息 {'Cache-Control': 'private, no-cache, no-store, proxy-revalidate, no-transform', 'Connection': 'keep-alive', 'Content-Encoding': 'gzip', 'Content-Type': 'text/html', 'Date': 'Mon, 02 Nov 2020 07:33:12 GMT', 'Last-Modified': 'Mon, 23 Jan 2017 13:23:50 GMT', 'Pragma': 'no-cache', 'Server': 'bfe/1.0.8.18', 'Set-Cookie': 'BDORZ=27315; max-age=86400; domain=.baidu.com; path=/', 'Transfer-Encoding': 'chunked'}
print(res.status_code)  #200 请求状态码，200是ok的意思
print(res.url)  #请求的url地址 https://www.baidu.com/
print(res.request.headers)  #请求的头信息 {'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}