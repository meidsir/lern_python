# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 20:11
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : day04.py
# @Software: PyCharm

a = 1
def func(a):
    print("在函数内部修改之前,变量a的内存地址为： %s" % id(a))
    a = 2
    print("在函数内部修改之后,变量a的内存地址为： %s" % id(a))
    print("函数内部的a为： %s" % a)


print("调用函数之前,变量a的内存地址为： %s" % id(a))
func(a)
print("函数外部的a为：%s" % a)