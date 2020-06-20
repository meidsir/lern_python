# -*- coding: utf-8 -*-
# @Time    : 2020/2/21 18:50
# @Author  : #meid
# @Email   : 306055516@qq.com
# @File    : day02.py
# @Software: PyCharm
from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route('/')
def show_excel():
    df = pd.read_excel("./销售数据.xlsx")
    table_html = df.to_html()
    print(table_html)

    return f"""
        <html>
            <body>
                <h1><销售数据表></h1>
                <div>{table_html}</div>
            </body>
        </html>
    """
if  __name__=='__main__':
    app.run(host="0.0.0.0")
