#-*- coding: UTF-8 -*-



# 绑定车辆
from api.lebov2.BindCar import BindCar
from public.http_request import HttpRequest

from api.lebov2.unbindCar import NnBindCar


from public.global_var import get_value

# def setup_module():
#     service = NnBindCar()
#     request = HttpRequest(service)
#     request.send()
#     request.cheack()

def test_bindcar():
    userId1 = get_value("userId")
    service = BindCar()
    service.body["userId"] = userId1
    request = HttpRequest(service)
    request.send()
    request.cheack()

def teardown_module():

    service = NnBindCar()
    request = HttpRequest(service)
    request.send()
    request.cheack()