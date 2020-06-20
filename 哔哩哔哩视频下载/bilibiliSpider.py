import sys
from you_get import common as you_get

def get_vidio():
    directory = r'D:\\下载\\Go视频教程'
    for i in range(1,4):
        url = "https://www.bilibili.com/video/av92510911?p=%s" % i      #需要下载的视频地址
        sys.argv = ['you-get','-o',directory,url]       #sys传递参数执行下载，就像在命令行一样
        you_get.main()

get_vidio()

import requests 