#-*- coding: UTF-8 -*-
class GetPendingOrdersByCarPlateNo:
    def __init__(self):
        self.ServiceName = "GetPendingOrdersByCarPlateNo"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {
            "userId": "157811",
            "isFlag": 0,
            "siteId": 1

        }
        self.expect = {
            "code": 200,
            "data": {
                "amount": 0
            },
            "success": "true",
            "message": "待付费订单信息"
        }