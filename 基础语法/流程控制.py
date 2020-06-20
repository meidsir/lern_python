# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 17:33
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : 流程控制.py
# @Software: PyCharm

age = input("请输入你的年龄：  ")
age = int(age)
if age >= 18:
    print("成年")

else:
    if age >= 12:
        print("少年")
    else:
        print("儿童")

