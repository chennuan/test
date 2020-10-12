#-*- coding: UTF-8 -*-
from api.lebov2.Register import Register
from public.http_request import HttpRequest

# 注册
def test_register():
    service = Register()
    request = HttpRequest(service)
    request.send()
    request.cheack()