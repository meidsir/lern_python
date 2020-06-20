import urllib.request  # 发送请求
import  requests
import re  # 正则表达式
from bs4 import BeautifulSoup


# 1.获取网页源码
def gethtml():  # 封装代码
    url = 'http://ncov.dxy.cn/ncovh5/view/pneumonia'
    User_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    headers = {'User_Agent': User_agent
               }
    response = requests.get(url,headers=headers).text
    #response.encoding='utf-8'
    #print(response.text)

    #return  response.text
#def list():
    soup= BeautifulSoup(response,'html.parser')
    items = soup.findAll('div', {'class': 'expand___wz_07'})
    name = items.findA('class', class_='subBlock1___j0DGa').get_text()
    xcqz = items.findA('class', class_='subBlock2___E7-fW').get_text()
    print(name)
    print(xcqz)
gethtml()
