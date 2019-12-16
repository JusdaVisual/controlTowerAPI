# -*- encoding: utf-8 -*-
"""
@File    : do_mysql.py
@Time    : 2019/9/3 16:46
@Author  : tang
@Email   : 343577336@qq.com
@Software: PyCharm
"""

import logging
import mysql.connector
from api_test_frame.Common.my_logger import MyLogger
from api_test_frame.Common.pro_path import *
# from api_test_frame.Common.read_conf import ReadConf

class DoMysql:

    def read_sql(self,sql_query,state=1):
        conf = eval(ReadConf().readConf(conf_path,'DBCONFIG','config'))
        cn = mysql.connector.connect(**conf)
        cursor = cn.cursor()
        cursor.execute(sql_query)
        if state == 1:
            try:
                sql_result = cursor.fetchone()
            except Exception as e:
                logging.error('获取数据失败，错误是：{}'.format(e))
                raise e
        else:
            try:
                sql_result = cursor.fetchall()
            except Exception as e:
                logging.error('获取数据失败，错误是：{}'.format(e))
                raise e

        return sql_result





    def insert_sql(self):

        pass



if __name__ == '__main__':
    sql = 'select mobilephone from member limit 1'
    print(DoMysql().read_sql(sql))




















