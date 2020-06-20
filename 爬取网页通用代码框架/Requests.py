import requests
from bs4 import BeautifulSoup as soup

def GetHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()   #如果状态不是200,引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

def htmlsoup(getHTML):
    soup = soup(getHTML,'lxml')
    return soup.text


def funcname(parameter_list):
    pass

if __name__ == "__main__":
    url="https://www.baidu.com"
    getHTML=(GetHTMLText(url))
    souphtml =  htmlsoup(getHTML)
    print(souphtml)
