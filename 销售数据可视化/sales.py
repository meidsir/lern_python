# 1.导入相关模块
from pyecharts.charts import Bar
import xlrd

# 2.读取Excel文件数据
data = xlrd.open_workbook('销售数据.xlsx')
# print(data)
# 3.获取特定的sheet
# 表格有多少行就打印多少行
table = data.sheets()[0]

# 数据提取目的：1.把销售员姓名与业绩分别放入到两个空列表中
#            2.要求两个列表数据一一对应
names = []
sales = []

for i in range(1, table.nrows):  # 高内聚，低耦合
    # print(table.row_values(i))
    name = table.row_values(i)[0]
    names.append(name)

    sale = table.row_values(i)[2]
    sales.append(sale)

print(names)
print(sales)

# 数据准备完成，开始用数据做可视化操作
bar = Bar()
bar.add_xaxis(names)
bar.add_yaxis('业务详情表', sales)

bar.render('销售数据可视化.html')

# 第2种方式
import matplotlib.pyplot as plt

zhong = 0
bei = 0
nan = 0
dong = 0

for i in range(1, table.nrows):
    # 部门
    di = table.row_values(i)[3]

    # 业绩
    sale = table.row_values(i)[2]

    if di == '华中':
        # zhong = zhong + sale
        zhong += sale
    elif di == '华北':
        bei += sale
    elif di == '华南':
        nan += sale
    elif di == '华东':
        dong += sale

    # print(zhong)
    # print(bei)
    # print(nan)
    # print(dong)

sales_bm = []

sales_bm.append(zhong)
sales_bm.append(bei)
sales_bm.append(nan)
sales_bm.append(dong)

fracs = []
for i in sales_bm:
    i = i / sum(sales_bm)
    fracs.append(i)

print(fracs)

# 效果图

# 各部门的标签
lables = ['华中', '华北', '华南', '华东']

print(lables)
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']

# 分离度

explode = [0.1, 0.1, 0, 0]

plt.pie(x=fracs, labels=lables, autopct='%.0f%%', explode=explode, shadow=True)
plt.show()
