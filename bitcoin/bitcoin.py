#导入要使用的相关模块（第三方模块）
#1.

#导入部分
#数据分析包
import pandas as pd
#数据绘图可视化
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SiHei']
#设置正常显示字符
plt.rcParams['axes.unicode_minus']= False

#设置绘图风格

#print(plt.style.available)


#1.获取数据
#current = pd.read_json('https://api.coinmarketcap.com/v1/ticker/')
#print(current.tail(10))

#haha = current.head(10)
#haha.to_excel('haha.xlsx')

#2.读取数据
data = pd.read_csv('data.csv')

#获取数据里面的id（虚拟货币名称）+ 市值
market_cap_raw = data[['id','market_cap_usd']]
#print(market_cap_raw.count())

#将市值大于0的数据过滤出来
cap = market_cap_raw.query('market_cap_usd>0')
#print(cap.count())

#数据可视化1 市值百分比
#拿到最值钱的前10个币种
cap10 = cap.set_index('id').sort_values(
    by = 'market_cap_usd',ascending=False)[:10]

#新增一列数据 market_cap_pera,该货币市值占总市值的百分比
cap10 = cap10.assign(
    market_cap_perc = lambda x:x.market_cap_usd / cap.market_cap_usd.sum()*100)

ax=cap10.plot.bar(y='market_cap_perc',title='市值Top10')
ax.set_ylabel('占总市值的百分数（%）')
plt.show()

#数据可视化2：市值表
#设置不同货币不同颜色