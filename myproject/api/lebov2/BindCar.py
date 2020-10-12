#-*- coding: UTF-8 -*-
class BindCar:
    # 绑定车辆
    def __init__(self):
        self.ServiceName = "BindCar"
        self.method = "post"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {
            "userId": "157762",
            "plateNo": "苏EL16F0",
            "plateColor": "001"
        }
        self.expect = {
            "code": 200,
            "data": "null",
            "success": "true",
            "message": "绑定车辆成功"
        }