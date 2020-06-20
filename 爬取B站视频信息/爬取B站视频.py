import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bilibili.com/ranking'

# 发起网络请求
response = requests.get(url)
html_text = response.text

print(html_text)

soup = BeautifulSoup(html_text, 'html.parser')

# 用来保存视频信息的对象
class Vidoe:
    def __init__(self, rank, title, score, visit, up, up_id, url):
        self.rank = rank
        self.title = title
        self.score = score
        self.visit = visit
        self.up = up
        self.up_id = up_id
        self.url = url

    def to_csv(self):
        return [self.rank, self.title, self.score, self.visit, self.up, self.up_id, self.url]

    @staticmethod
    def CSV_title():
        return ['排名', '标题', '分数', '播放量', 'Up主', 'Up ID', 'URL']


# 提取列表
items = soup.findAll('li', {'class': 'rank-item'})
vidoes = []  # 保存提取出来的video列表

for item in items:
    title = item.find('a', {'class': 'title'}).text  # 视频标题
    score = item.find('div', {'class': 'pts'}).find('div').text  # 综合得分
    rank = item.find('div', {'class': 'num'}).text  # 排名
    visit = item.find('span', {'class': 'data-box'}).text  # 排名
    up = item.find_all('a')[2].text  # 播放量
    space = item.find_all('a')[2].get('href')
    up_id = space[len('//space.bilibili.com/'):]  # 播放量
    url = item.find('a', {'class': 'title'}).get('href')
    v = Vidoe(rank, title, score, visit, up, up_id, url)
    vidoes.append(v)

    #print(f'{url}')
file_name = 'top100.csv'
with open(file_name, 'w', newline='',encoding='utf-8') as f:
    pen = csv.writer(f)
    pen.writerow(Vidoe.CSV_title())
    for v in vidoes:
        pen.writerow(v.to_csv())
