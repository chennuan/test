#-*- coding: UTF-8 -*-
class GetParkingLotArea:
    # 注册
    def __init__(self):
        self.ServiceName = "GetParkingLotArea"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.parkId = "PR010072"
        self.body = {

        }
        self.expect = {
                "msg": "success",
                "code": "200",
                "data": "吴江区"
            }