# 数据分析
from matplotlib import pyplot as plt  # 科学技术库
import csv  # 导入文件
from datetime import datetime  # 日期

filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    # print(reader)
    hear_row = next(reader)
    #print(hear_row)
    dates,highs,lows=[],[],[]

    for i in reader:
        current_date = datetime.strptime(i[0],"%Y/%m/%d")
        dates.append(current_date)
        high = int(i[1])
        highs.append(high)
        #print(highs)
        low= int(i[3])
        lows.append(low)

#画图 dpi分辨率
plt.figure(dpi=93,figsize=(10,6))
plt.plot(dates,highs,c='red',alpha=0.5)
plt.plot(dates,lows,c='blue',alpha=0.5)
plt.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

#样式
plt.title("Daily high and low temperatures",fontsize=24)
plt.xlabel('Dylan',)
plt.ylabel()
