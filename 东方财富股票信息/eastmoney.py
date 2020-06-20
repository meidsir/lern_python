import requests
import json

cookies = {
    'qgqp_b_id': '55a37d7e300b6a66342ceff587c39566',
    'intellpositionL': '1080.8px',
    'st_si': '34409245571399',
    'st_asi': 'delete',
    'cowCookie': 'true',
    'HAList': 'a-sz-300059-^%^u4E1C^%^u65B9^%^u8D22^%^u5BCC',
    'em_hq_fls': 'js',
    'intellpositionT': '772px',
    'st_pvi': '70362402911500',
    'st_sp': '2020-02-12^%^2011^%^3A00^%^3A17',
    'st_inirUrl': 'https^%^3A^%^2F^%^2Fwww.baidu.com^%^2Flink',
    'st_sn': '9',
    'st_psi': '20200217150117180-113300300813-8456547492',
}

headers = {
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36',
    'Accept': '*/*',
    'Referer': 'http://data.eastmoney.com/zjlx/detail.html',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

params = (
    ('pn', '1^'),
    ('pz', '50^'),
    ('po', '1^'),
    ('np', '1^'),
    ('ut', 'b2884a393a59ad64002292a3e90d46a5^'),
    ('fltt', '2^'),
    ('invt', '2^'),
    ('fid0', 'f4001^'),
    ('fid', 'f62^'),
    ('fs', 'm:0 t:6 f:^!2,m:0 t:13 f:^!2,m:0 t:80 f:^!2,m:1 t:2 f:^!2,m:1 t:23 f:^!2,m:0 t:7 f:^!2,m:1 t:3 f:^!2^'),
    ('stat', '1^'),
    ('fields', 'f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^'),
    ('rt', '52730762^'),
   # ('cb', 'jQuery18303708629584970644_1581922860454^'),
    ('_', '1581922880498'),
)

response = requests.get('http://push2.eastmoney.com/api/qt/clist/get', headers=headers, params=params, cookies=cookies)

# NB. Original query string below. It seems impossible to parse and
# reproduce query strings 100% accurately so the one below is given
# in case the reproduced version is not "correct".
# response = requests.get('http://push2.eastmoney.com/api/qt/clist/get?pn=1^&pz=50^&po=1^&np=1^&ut=b2884a393a59ad64002292a3e90d46a5^&fltt=2^&invt=2^&fid0=f4001^&fid=f3^&fs=m:0+t:6+f:^!2,m:0+t:13+f:^!2,m:0+t:80+f:^!2,m:1+t:2+f:^!2,m:1+t:23+f:^!2,m:0+t:7+f:^!2,m:1+t:3+f:^!2^&stat=1^&fields=f12,f14,f2,f3,f62,f184,f66,f69,f72,f75,f78,f81,f84,f87,f204,f205,f124^&rt=52716051^&cb=jQuery1830019578467110239473_1581480573748^&_=1581481533859', headers=headers, cookies=cookies, verify=False)

# print(response.text)
# print (type(response.text))

# 第2部，数据清洗

resp_dict = json.loads(response.text)
# print(resp_dict)
# print(type(resp_dict))

datas = resp_dict.get('data').get('diff')
# print(datas)
compnies = []
prices = []

for data in datas:
    # print(data)
    # 公司名
    company = data.get('f14')
    share_1 = data.get('f184')
    share_5 = data.get('f165')
    share_10 = data.get('f175')
# 当天股价
    price = data.get('f2')
    if share_1 >= 10:
        compnies.append(company)
        prices.append(price)


prices.sort(reverse=True)
print(compnies)
print(prices)

from pyecharts.charts import Bar
import pyecharts.options as opts

bar = Bar()
bar.add_xaxis(compnies)
bar.add_yaxis('股价图',prices)

bar.set_global_opts(
    xaxis_opts=opts.AxisOpts(
        axislabel_opts=opts.LabelOpts(rotate=-40),
    ),
    yaxis_opts=opts.AxisOpts(name='价格:(元/股)'),
)
bar.render('股价图.html')


def test(a,b,c):
    """
    
    """
    pass
