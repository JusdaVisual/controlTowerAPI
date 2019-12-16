# -*- encoding: utf-8 -*-
"""
@File    : test01.py
@Time    : 2019/8/27 8:57
@Author  : tang
@Email   : 343577336@qq.com
@Software: PyCharm
"""

from Common.my_logger import MyLogger
# from openpyxl import load_workbook
import xlrd,re,sys,unittest,yaml

class DoExcel:
    # 读取excel数据
    def read_excel(self,filename, sheetname):
        """
        读取excle表，把第一行的字段作为key，第二行及以后作为value，
        每一行生成一个字典，把字典添加到列表，返回列表
        :param filename: 文件路径
        :param sheetname: Sheet表名
        :return: 列表
        """
        # 获取文件
        try:
            data = xlrd.open_workbook(filename)
            # 获取工作表
            sheet = data.sheet_by_name(sheetname)
        except Exception as e:
            MyLogger().log_error("{}".format(e))
            raise e
        # 获取总行数
        row_num = sheet.nrows
        # 以第一行内容为键，第二行及以后的内容为值新建一个字典
        li=[]
        for i in range(2, row_num):
            # 获取第一行的内容
            fist_value = sheet.row_values(1)
            # 第i行的内容
            i_value = sheet.row_values(i)
            # 把第一行的内容作为键，第二行及以后的内容作为值，生成一个字典
            dic = dict(zip(fist_value, i_value))
            # 把每一行的字典添加到列表
            li.append(dic)
        return li

    # 写回数据到excel
    # def write_excel(self,filepath,sheetname,row,column,new_value):
    #     wk = load_workbook(filepath)
    #     sheet = wk[sheetname]
    #     sheet.cell(row,column).value = new_value
    #     wk.save(filepath)
    #     wk.close()

    # 对数据进行预处理，如果字符串类型的容器，还原为容器
    def pro_data(self,data):
        """
        把容器类型外层的引号去掉
        :param data:待处理的数据
        :return:处理后的数据
        """
        if data.startswith("{") or data.startswith("["):
            return eval(data)
        else:
            return data

    # 替换excel表中的${}格式
    def replace_excel(self,param, results):
        """
        通过parma中${}花括号里面的值在result中获取value,
        以获取的value把param中${}格式整个替换
        :param param: excel表中待更新的内容
        :param result: 响应结果或全局变量
        :return:替换后的param
        """
        try:
            globals = str(results)
            while "false" in globals or "true" in globals or "null" in globals:
                globals = globals.replace("false", "False")
                globals = globals.replace("true", "True")
                globals = globals.replace("null","None")
            while re.search("\${(.+?)}", param):
                key = re.search("\${(.+?)}", param).group(1)

                value = re.search("\${(.+?)}", param).group()
                v = eval(globals + key)
                param = param.replace(value, str(v))
            return param
        except Exception as e:
            raise e

    #把花括号里面的值作为键在响应结果或全局变量中获取替换整个${}
    def replace_excel2(self,param,result):
        """
        把parma中${}花括号里面的值做为key在result中获取value,
        以获取的value把param中${}格式整个替换
        :param param: excel表中待更新的内容
        :param result: 响应结果或全局变量
        :return:替换后的param
        """
        # 判断参数中是否有${},如果有用循环把所有的${}替换掉
        v = None
        while re.search("\${(.+?)}",param):
            # 获取花括号里面的值
            value=re.search("\${(.+?)}",param).group(1)
            # 根据花括号里面的值匹配到result中对应的内容
            # 匹配字符串类型的字典
            if re.search('("%s":")(.+?)(")'%value,str(result)):
                v=re.search('("%s":")(.+?)(")'%value,str(result)).group(2)
            # 匹配本身是字典
            elif re.search("('%s': ')(.+?)(')"%value,str(result)):
                v=re.search("('%s': ')(.+?)(')"%value,str(result)).group(2)

            # 匹配响应结果的value为非字符串
            elif re.search('("%s":)(\[.+?])'%value,str(result)):
                v = re.search('("%s":)(\[.+?])'%value,str(result)).group(2)
            elif re.search('("%s":)({.+?})'%value,str(result)):
                v = re.search('("%s":)({.+?})'%value,str(result)).group(2)

            # 匹配全局变量的value非字符串
            elif re.search("('%s': )(\[.+?])"%value,str(result)):
                v = re.search("('%s': )(\[.+?])"%value,str(result)).group(2)
            elif re.search("('%s': )({.+?})"%value,str(result)):
                v = re.search("('%s': )({.+?})"%value,str(result)).group(2)
            else:
                break
            # 获取整个${}
            key = re.search("\${(.+?)}", param).group(0)
            if v!= None:
                param = param.replace(key,v)
        return param

    # 断言方法
    def assert_fun(self,ExpectedResult,ActualResult):

        self.assertIn(ExpectedResult,ActualResult)
    # 更新全局变量
    def update_globals(self,dic,excel_message):
        """
        更新全局变量
        :param dic: 全局变量
        :param excel_message: 需要添加到全局变量的值
        """
        try:
            # 把需要设置全局变量的Global替换后的结果添加到全局变量dic，供后续使用
            dic.update(eval(excel_message))
        except Exception as e:
            pass
    # # 读取配置文件
    # def read_yaml(self,filename):
    #     try:
    #         with open(filename,"r") as f:
    #             data = yaml.load(f)
    #             url = data["url"]
    #             return url
    #     except Exception as e:
    #         raise e


if __name__=="__main__":
    d=DoExcel()
    # param='{"callid":${callId} "${Id}"}'
    # result={"callId":[1],"Id":"123"}
    # li=d.read_excel(r"D:\刘凯\liukai\框架\Frame\api_test_frame\Data\control_tower测试用例.xlsx","Sheet1")
    # p=d.replace_excel2(param,result)
    # print(p)
    a=d.read_excel(r"D:\刘凯\liukai\框架\Frame\api_test_frame\Data\test_cases.xlsx","Sheet1")
    print(a[1])










