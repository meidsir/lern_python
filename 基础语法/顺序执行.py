# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 17:36
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : 顺序执行.py
# @Software: PyCharm

import os

print('<[1]> time module start')        # 2


class ClassOne():
    print('<[2]> ClassOne body')            # 3

    def __init__(self):                     # 10
        print('<[3]> ClassOne.__init__')

    def __del__(self):
        print('<[4]> ClassOne.__del__')     # 101

    def method_x(self):                     # 12
        print('<[5]> ClassOne.method_x')

    class ClassTwo(object):
        print('<[6]> ClassTwo body')        # 4


class ClassThree():
    print('<[7]> ClassThree body')          # 5

    def method_y(self):                     # 16
        print('<[8]> ClassThree.method_y')


class ClassFour(ClassThree):
    print('<[9]> ClassFour body')           # 6


def func():
    print("<func> function func")

if __name__ == '__main__':                      # 7
    print('<[11]> ClassOne tests', 30 * '.')    # 8
    one = ClassOne()                            # 9
    one.method_x()                              # 11
    print('<[12]> ClassThree tests', 30 * '.')  # 13
    three = ClassThree()                        # 14
    three.method_y()                            # 15
    print('<[13]> ClassFour tests', 30 * '.')  # 17
    four = ClassFour()
    four.method_y()

print('<[14]> evaltime module end')             # 100