# -*- encoding: utf-8 -*-
"""
@File    : http_requests.py
@Time    : 2019/8/26 15:56
@Author  : tang
@Email   : 343577336@qq.com
@Software: PyCharm
"""

import logging
import requests, json


class HttpRequest:
    def http_request(self,method,  url, data, headers):
        # 发送get请求
        if method.upper() == "GET":
            try:
                r = requests.request(method="GET", url=url, params=data, headers=headers)
                response = r.text
            except Exception as e:
                raise e
        # 发送其他请求
        else:
            method = method.upper()
            try:
                r = requests.request(method=method, url=url, data = json.dumps(data), headers=headers)
                response = r.text
            except TypeError:
                # 文件上传
                r = requests.request(method=method, url=url, files = data, headers=headers)
                response = r.text
            except Exception as e:
                raise e

        return response


if __name__ == '__main__':
   pass