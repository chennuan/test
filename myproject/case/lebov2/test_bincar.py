#-*- coding: UTF-8 -*-
from api.lebov2.BindCar import BindCar
from public.http_request import HttpRequest


# 绑定车辆
def test_bindcar():
    service = BindCar()
    request = HttpRequest(service)
    request.send()
    request.cheack()