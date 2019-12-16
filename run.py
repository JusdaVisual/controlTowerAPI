# -*- encoding: utf-8 -*-
"""
@File    : run.py
@Time    : 2019/8/23 17:46
@Author  : tang
@Email   : 343577336@qq.com
@Software: PyCharm
"""

import unittest,time,datetime
# from Common.test import Test1
from BeautifulReport import BeautifulReport
from Common.pro_path import *
# import HTMLTestRunnerNew

date = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
testCase = unittest.defaultTestLoader.discover(start_dir=common_path, pattern='test.py')
print(testCase.countTestCases())

#执行测试用例
runner = BeautifulReport(testCase)
#生成测试报告
runner.report(description='control-tower接口测试', filename='control-tower接口测试' + date + '.html', report_dir=html_report_path)