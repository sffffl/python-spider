############post请求

import requests

#定义请求的url
url = 'https://fanyi.baidu.com/sug'

#定义请求头
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

#post发送的数据
data = {'kw':'你好'}

#发送请求
res = requests.post(url=url,headers=headers,data=data)

#接收返回数据

code = res.status_code
if code == 200:
    print('请求成功！')
    data = res.json()
    if data['errno'] == 0:
        print('响应成功')
        k = data['data'][0]['k']
        v = data['data'][0]['v'].split(';')[-2]
        print(k,'===',v)
'''
print(res.status_code)
print(res.text)
print(res.json())
'''