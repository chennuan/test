#-*- coding: UTF-8 -*-
from data.settings import siteId, OpenID1


class GetParkingPayBase:
    # 绑定车辆
    def __init__(self):
        self.ServiceName = "GetParkingPayBase"
        self.method = "get"
        self.siteId = siteId
        self.carPlateColor = "001"
        self.carPlateNo = "苏EL16F0"
        self.openId = OpenID1
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {

        }
        self.expect = {
            "code": 200,
            "data": {
                "carPlateNo": "苏EL16F0",
                "carPlateColor": "001",
                "parkingCode": "PR010072",
                "parkingName": ".*",
                "parkingType": "002",
                "orderNo": "",
                "inTime": ".*",
                "parkingDuration": "",
                "orderAmount": "",
                "payAmount": "",
                "orderDetail": "",
                "couponAccount": "",
                "merchantExpenses": "",
                "userType": "",
                "allowSettleAllFee": "",
                "payStatus": "000"
            },
            "success": "True",
            "message": "停车缴费信息"
        }