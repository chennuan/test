#-*- coding: UTF-8 -*-
import json
import sys
sys.path.append('../../')
print(sys.path)
import pytest
from api.lebov2.getParkingPayBase import GetParkingPayBase
from parameterized import parameterized
from api.lebov2.Register import Register
from api.lebov2.BindCar import BindCar
from public.http_request import HttpRequest
from api.lebov2.unbindCar import NnBindCar
from api.Login import Login
from api.lebov2.getBindCarsList import GetBindCarsList

'''
场景用例_001：
    前置条件：用户已注册
    场景描述：绑定车辆--》登录--》获取停车信息--》查询绑定车辆列表
    后置条件：解绑车辆
'''
userId = ""
carId = ""


# 注册
def setup_module():
    global userId
    service = Register()
    request = HttpRequest(service)
    request.send()
    request.cheack()
    res = json.loads(request.response.text)
    userId = res['data']

# 绑定车辆
def test_bindcar():
    service = BindCar()
    service.body["userId"] = userId
    request = HttpRequest(service)
    request.send()
    request.cheack()


# def test_login():
#     service = Login()
#     request = HttpRequest(service)
#     request.send()
#     request.cheack()

# 获取停车信息
carlist = ['苏EL16F0']
@pytest.mark.parametrize('carPlateNo', carlist)
def test_getparkingpaybase(carPlateNo):
    service = GetParkingPayBase()
    service.carPlateNo = carPlateNo
    request = HttpRequest(service)
    request.send()
    request.cheack()


# 获取绑定车辆列表
def test_getbindcarslist():
    global carId
    service = GetBindCarsList()
    service.userId = userId
    request = HttpRequest(service)
    request.send()
    request.cheack()
    res = json.loads(request.response.text)
    carId = res['data'][0]['id']


# 解绑车辆
def teardown_module():
    service = NnBindCar()
    service.userId = userId
    service.carId = carId
    #service.expect['data'][0]['id'] = carId
    request = HttpRequest(service)
    request.send()
    request.cheack()