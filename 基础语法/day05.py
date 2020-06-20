import requests
from requests import Response


def GetHTML():
    url="https://www.baidu.com/"
    response =  requests.get(url)
    response.encoding="utf-8"
    # print(response.status_code)    #使用status_code状态码检查访问是否成功
    # print(response.encoding)       #查看编码方式
    # print(response.apparent_encoding)
    print(response.text)


GetHTML()
