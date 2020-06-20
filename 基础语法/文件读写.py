# -*- coding: utf-8 -*-
# @Time    : 2020/2/28 10:26
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : 文件读写.py
# @Software: PyCharm

#写入模式
f = open(r'd:\1.txt','w')
f.write("I live python!")
f.close()

#读取模式
f = open(r'D:\文档资料\开发相关\Python语言入门.pdf')
data = f.read(1024)
f.close()
print(data.encode())

#二进制写入模式
f = open(r'd:\2.txt','wb')
f.write("i love python".encode())
f.close()

#with关键字用于Python的上下文管理机制 file-like object

with open(r'd:\2.txt') as f:
    data = f.read()
    print(data)

#t同时读两个文件,将一个文件的一行写进另一个文件
with open('file1') as f1,open('file2') as f2:
    data = f1.readline()
    f2.write(data)
