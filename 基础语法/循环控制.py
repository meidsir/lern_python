# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 17:44
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : 循环控制.py
# @Software: PyCharm

n = 100
sum = 0
counter = 1
while counter <= n:
    sum += counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))