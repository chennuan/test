#-*- coding: UTF-8 -*-



# 绑定车辆
from myproject.api.lebov2.BindCar import BindCar
from myproject.public.http_request import HttpRequest

from myproject.api.lebov2.unbindCar import NnBindCar


from myproject.public.global_var import get_value

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