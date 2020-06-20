# -*- coding: utf-8 -*-
# @Time    : 2020/2/23 17:58
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : 函数.py
# @Software: PyCharm
lis = [1,2,3,4,5]

def summer(lis):
    """
    这里是函数的说明文档，doc的位置
    :param lis: 参数列表的说明
    :return: 返回值的说明
    """
    total = 0
    for i in lis:
        total += i
    return total

def test(lis):
    """
    调用函数
    :param lis: 传入数组
    :return:  无返回值
    """
    print(summer(lis))

if __name__=="__main__":
    test(lis)