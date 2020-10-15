#-*- coding: UTF-8 -*-
class GetPendingOrdersByCarPlateNoDital:
    def __init__(self):
        self.ServiceName = "GetPendingOrdersByCarPlateNo"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {
            "userId": "157811",
            "isFlag": 0,
            "siteId": 1,
            "carPlateNo": "%E8%8B%8FEL16F0",
            "carPlateColor": "001",
            "isPayOthersPage": 0,
            "parkingLotType": 0

        }
        self.expect = {
            "code": 200,
            "data": {
                "amount": 0
            },
            "success": "true",
            "message": "待付费订单信息"
        }