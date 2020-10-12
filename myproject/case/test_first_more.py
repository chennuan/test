#-*- coding: UTF-8 -*-
# 导包
import pytest

from parameterized import parameterized
# 新建测试类
# 测试脚本名以test_开头
# 测试脚本中若是执行一个类中的函数，测试类以Test开头，并且不能带有init方法


# 测试脚本中若是执行函数，以test_开头
# 新建测试方法

from api.cnValidateImage import CnValiDateImage
from tools.read_json import ReadJson

"""
parameterized参数化组件使用
安装：
    pip install parameterized
    
使用：
    导包：
        from parameterized import parameterized
    @parameterized.expand(参数)
    参数:
        单个参数格式：列表 [值1，值2]
        多个参数格式：列表嵌套元组[(值1，值2)，(值1，值2)]
"""

# 参数化示例
# @parameterized.expand([("string", "123456"), ("chennuan", "564897")])
# def test_pri(admin, password):
#     print("admin", admin, password)


# 读取数据函数
def get_data():
    datas = ReadJson("data_more.json").read_json()
    arrs = []
    # 使用字典的values()方法获取所有值
    # 使用遍历获取所有的values
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("bystring"),
                     data.get("status_code")))
    return arrs;


@parameterized.expand(get_data())
def test_cnvalidateimage_more(url, bystring, status_code):
    # 暂时存放数据url、bystring
    # url ="http://www.webxml.com.cn/WebServices/ValidateCodeWebService.asmx/cnValidateImage"
    # bystring = "string"

    # 调用直接获得验证码图片方法
    res = CnValiDateImage().api_post_cnvalidateimage(url, bystring)
    # 断言 响应信息及状态码
    assert res.status_code == status_code


