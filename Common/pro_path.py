# -*- encoding: utf-8 -*-
"""
@File    : pro_path.py
@Time    : 2019/9/3 17:38
@Author  : tang
@Email   : 343577336@qq.com
@Software: PyCharm
"""

import os

# 项目路径
project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
# 测试数据文件目录
data_path=os.path.join(project_path,'Data')
# 日志文件目录
log_path = os.path.join(project_path,'Log')
# 测试报告目录
html_report_path = os.path.join(project_path,'HtmlReport')
#Common路径
common_path = os.path.join(project_path,'Common')


if __name__ == '__main__':

    print(project_path)

    print(log_path)
    print(html_report_path)
    print(data_path)