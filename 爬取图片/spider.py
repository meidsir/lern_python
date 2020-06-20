# 导入需要用到的包（模块）
import requests  # 用来模拟浏览器发送的网络请求
from lxml import etree  # 用来对需要解析提取的数据做预处理
from urllib import request  # 用request里面的urlretrive()下载图片
import time  # 让程序延迟几秒再进行


# 函数的封装
# 使用def开始一个函数的定义
# spider类定义如何去爬取某个网站
# 包括爬取的动作，以及如何从网页中提取结构化的数据 分析某个网页
def huya_spider():
    # 请求数据
    #
    url = 'https://www.huya.com/g/4079'
    User_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36'

    headers = {
        'User_Agent': User_agent
    }

    response = requests.get(url, headers=headers)
    data_txt = response.text
    #print(data_txt)

    # Xpath构造一个xpath解析对象 对HTML文本进行自动修正
    # 输出修正后的结构  类型是bytes
    data = etree.HTML(data_txt)
    friend_list = data.xpath('//img[@class="pic"]')

    # 通过这个数据 for循环遍历这个数据 把图片的url地址拿出来 ，再一张张下载
    for friend in friend_list:
        img = friend.xpath('./@data-original')[0]
    # 写这个过程的目的在于：
        img = img.split("?")[0]
    # 接着把每一张图片进行命名
        name = friend.xpath('./@alt')[0]


        request.urlretrieve(img, 'friends/' + name + '.jpg')


    #显示一下打印的进度
        print("<%s>下载完毕！"%name)
        time.sleep(3)

    #调用函数
huya_spider()


