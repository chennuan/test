#-*- coding: UTF-8 -*-
import pytest

from api.lebov2.getParkingPayBase import GetParkingPayBase
from public.http_request import HttpRequest
from parameterized import parameterized

# 获取停车信息
carlist = ['苏EL16F0', '苏EL16F1']
@pytest.mark.parametrize('carPlateNo', carlist)
def test_bindcar(carPlateNo):
    service = GetParkingPayBase()
    service.carPlateNo = carPlateNo
    request = HttpRequest(service)
    request.send()
    request.cheack()