# -*- encoding: utf-8 -*-
"""
@File    : my_logger.py
@Time    : 2019/9/26 9:51
@Author  : tang
@Email   : 343577336@qq.com
@Software: PyCharm
"""

import logging, time
from Common.pro_path import *

class MyLogger:
    def __init__(self):
        """设置日志初始化方法"""
        # 以当前时间作为日志文件名
        now_time=time.strftime("%Y%m%d%H%M%S.log")
        filename=log_path+"\\"+now_time
        self.logger=logging.getLogger()
        self.logger.setLevel("INFO")
        self.h1=logging.StreamHandler()
        self.h2=logging.FileHandler(filename,"w",encoding="utf-8")
        self.f=logging.Formatter("%(asctime)s-%(message)s-%(levelname)s",datefmt="%Y-%m-%d %H:%M:%S")
        self.h1.setFormatter(self.f)
        self.h2.setFormatter(self.f)
        self.logger.addHandler(self.h1)
        self.logger.addHandler(self.h2)
    def log_debug(self,message):
        self.logger.debug(message)
    def log_info(self,message):
        self.logger.info(message)
    def log_warning(self,message):
        self.logger.warning(message)
    def log_error(self,message):
        self.logger.error(message)


if __name__ == '__main__':
    m=MyLogger()
    m.log_error("严重错误")
