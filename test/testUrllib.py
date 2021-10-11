import urllib.request

# 获取get请求
# response=urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))

import urllib.parse
data=bytes(urllib.parse.urlencode({"hee":"nene"}),encoding='utf-8')
response=urllib.request.urlopen('http://httpbin.org/post',data=data)
print(response.read())