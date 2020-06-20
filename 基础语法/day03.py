# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 11:16
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : day03.py
# @Software: PyCharm

#递归函数

def sum_number(n):
    # total = 0
    # for i in range(1,n+1):
    #     total += i
    # return total
    if n <= 0:
        return 0
    return sum_number(n-1)+n

result =  sum_number(10)

print(result)