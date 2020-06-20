from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType, CurrentConfig
from pyecharts.options import InitOpts
import os
import requests
import json
import re


provinces = ['湖北', '广东', '浙江', '河南', '湖南', '安徽', '江西', '重庆', '江苏', '山东', '四川', '北京', '黑龙江', '上海', '福建', '陕西',
             '河北', '广西', '云南', '海南', '山西', '辽宁', '贵州', '天津', '甘肃', '吉林', '内蒙古', '宁夏', '新疆', '香港', '台湾', '青海', '澳门', '西藏']
value = [27100, 1120, 1075, 1033, 838, 779, 740, 468, 446, 435, 386, 326, 307, 293,
         250, 208, 206, 195, 140, 128, 115, 105, 96, 90, 79, 78, 54, 45, 45, 26, 18, 17, 10, 1]


def reptile() -> list:
    news = []
    R = requests.get("https://opendata.baidu.com/data/inner?tn=reserved_all_res_tn&dspName=iphone&from_sf=1&dsp=iphone&resource_id=28565&alr=1&query=%E8%82%BA%E7%82%8E&cb=jsonp_1581217937737_29516")
    txt = R.text
    num = txt.find('(')
    txt = txt[num+1:-1]
    data = json.loads(txt)
    length = len(data['Result'][0]['DisplayData']['result']['items'])
    for i in range(length):
        news.append(data['Result'][0]['DisplayData']
                    ['result']['items'][i]['eventDescription'])
    return news


def geo_base(data) -> Geo:
    c = (
        Geo()
        .add_schema(maptype="china")
        .add("疫情人数", data, type_=ChartType.EFFECT_SCATTER,)
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            visualmap_opts=opts.VisualMapOpts(max_=1000),
            title_opts=opts.TitleOpts(title="全国各地疫情分布图"),
        )
    )
    return c


def analysis(news):
    result = []
    for i in news:
        for j in provinces:
            if i[:4] == j+'新增':
                keyword = re.findall('\d*例\Z', i)
                try:
                    keyword = keyword[0][:-1]
                except:
                    keyword = ''
                if keyword != '':
                    result.append((j, int(keyword)))
    return result


def correct_data(correct):
    data = [list(z) for z in zip(provinces, value)]
    for i in data:
        for j in correct:
            if i[0] == j[0]:
                i[1] = j[1]
    return data


if __name__ == "__main__":
    correct = analysis(reptile())
    data = correct_data(correct)
    geo_base(data).render()
    os.startfile("render.html")
