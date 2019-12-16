from config.Log import Log
from Common.http_requests import HttpRequest
from Common.pro_path import *
from Common import globalvar
from Common.do_excel import DoExcel
from Common.my_logger import MyLogger
import ddt,unittest,json,sys
import traceback
# 定义一个全局变量
dic={}
# 读取excel表的内容返回一个[{},{}]格式的值
d=DoExcel()
r = d.read_excel(data_path+'\\control_tower测试用例.xlsx',"登录")
r1_air = d.read_excel(data_path +'\\control_tower测试用例.xlsx',"AirExceptList_API")
r1_sea = d.read_excel(data_path +'\\control_tower测试用例.xlsx',"SeaExceptList_API")
r2 = d.read_excel(data_path +'\\control_tower测试用例.xlsx',"邓天苹")

r.extend(r1_air)
r.extend(r1_sea)
r.extend(r2)

@ddt.ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.log = Log()

    @ddt.data(*r)
    # 登录
    def test01(self,data):
        # 引用全局变量字典
        global dic
        # 把测试用例名作为测试用例说明
        Case_name = data["Case_name"]
        self.log.info('======{}开始！========='.format(Case_name))
        self._testMethodDoc = Case_name
        # 对请求头、参数、url进行预处理
        new_url=d.replace_excel(data["Url"],dic)
        param=d.replace_excel(data["Param"],dic)
        header=d.replace_excel(data["Header"],dic)
        new_param=d.pro_data(param)
        new_header=d.pro_data(header)
        Method = data["Method"]
        Global = data["Global"]
        ExpectedResult = data["ExpectedResult"]
        self.log.info('\n请求方法：%s\n\n URL：%s \n\n 请求参数：%s \n\n 请求头部信息：%s\n\n'%(Method, new_url, new_param, new_header))
        # 发送请求,获取响应的实际结果
        try:
            response_result = HttpRequest().http_request(Method, new_url, new_param, new_header)
        except Exception as e:
            self.log.error('未知错误：%s'%str(traceback.format_exc()))
        else:
            if isinstance(response_result,str):
                response_result = json.loads(response_result)
                response_result = json.dumps(response_result,sort_keys=True, indent=4, separators=(',', ':'),ensure_ascii=False)
                self.log.info('响应结果信息：\n%s\n预期结果信息：\n%s'%(response_result,ExpectedResult))
            #把预期结果中的${}形式替换为实际结果
            true_result = d.replace_excel(ExpectedResult, response_result)
            # print(true_result)
            # 对预期结果进行预处理
            true_result = d.pro_data(true_result)
            # 对响应结果进行断言
            for i in true_result:
                self.assertIn(i[0], i[1])
                self.log.info('断言：\n 实际结果:%s \n预期结果：%s'%(i[0], i[1]))
            # 把需要设置全局变量的Global中的${}替换为响应中的值
            excel_message = d.replace_excel(Global, response_result)
            # print(excel_message)
            # 把需要设置全局变量的Global替换后的结果添加到全局变量dic，供后续使用
            d.update_globals(dic,excel_message)
            self.log.info('\n \n')

if __name__=="__main__":
    unittest.main()

