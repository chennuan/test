#-*- coding: UTF-8 -*-
import pytest
import json
from api.ToSimplifiedChinese import ToSimplifiedChinese
from parameterized import parameterized


# 读取数据函数
from tools.read_json import ReadJson


def get_data():
    datas = ReadJson("simp_data.json").read_json()
    arrs = []
    # 使用字典的values()方法获取所有值
    # 使用遍历获取所有的values
    for data in datas.values():
        arrs.append((data.get("url"),
                     data.get("headers"),
                     data.get("params"),
                     data.get("status_code")))
    return arrs;


@parameterized.expand(get_data())
def test_toSimplifiedChinese(url, headers, params, status_code):

    res = ToSimplifiedChinese().api_get_toSimplifiedChinese(url, params, headers)
    assert res.status_code == status_code

