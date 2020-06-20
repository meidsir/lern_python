# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 12:02
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : novel.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup



def get_novel_chapters():
    root_url = "http://www.89wxw.cn/0/9/"
    r = requests.get(root_url)
    r.encoding = "gbk"

    soup = BeautifulSoup(r.text, "html.parser")

    data = []
    for dd in soup.find_all("dd"):
        link = dd.find("a")
        if not link:
            continue

        data.append(("http://www.89wxw.cn%s" % link['href'], link.get_text()))
    return data

def get_chapter_content(url):
    r = requests.get(url)
    # r.encoding = 'gbk'
    soup = BeautifulSoup(r.text, "html.parser")
    return soup.find("div", id='content').get_text()


novel_chapter = get_novel_chapters()
total_cnt = len(novel_chapter)
# idx = 0

for chapter in novel_chapter:
    # idx += 1
    print(total_cnt)
    url, title = chapter
    with open("%s.txt" % title, "w" , encoding="utf-8") as fout:
        fout.write(get_chapter_content(url))
