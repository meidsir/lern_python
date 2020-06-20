# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 20:16
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : 参数类型.py
# @Software: PyCharm
# list_1 = [1,2,3,4,5]
# list_2 = ['a','b','c','d','e']

# m = lambda a:a*i i in range(10)
# i = range(10)
# print(i)

# s=zip(list_1,list_2)
#
# print(tuple(s))
#

# a = lambda x,y,z:x+y-z
# # print(a(2,4,8))
# lis = [1, 2, 3, 4, 5, ]
# for _ in range(len(lis)):
#     print(lis[_])


# class People:
#     title = "人类"
#
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def print_age(self):
#         print('%s:%s' % (self.__name, self.__age))
#
#     def get_name(self):
#         return self.__name
#
#     def get_age(self):
#         return self.__age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def set_age(self, age):
#         self.__age = age
#
#
# obj = People("jack", 18)
# obj.__name = "tom"          # 注意这一行
# print("obj.__name:  ", obj.__name)
# print("obj.get_name():  ", obj.get_name())


class Student:
    classroom = '101'
    address = 'beijing'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_age(self):
        print('%s: %s' % (self.name, self.age))


# 以下是错误的用法
# 类将它内部的变量和方法封装起来，阻止外部的直接访问
print(classroom)
print(adress)
print_age()