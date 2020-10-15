#-*- coding: UTF-8 -*-
class NnBindCar:
    # 绑定车辆
    def __init__(self):
        self.ServiceName = "NnBindCar"
        self.method = "delete"
        self.header = {
            "Content-Type": "application/json"
        }
        self.userId = "157757"
        self.carId = "152969"
        self.plateNo = "苏EL16F0"
        self.plateColor = "001"
        self.body = {

        }
        self.expect = ".*"