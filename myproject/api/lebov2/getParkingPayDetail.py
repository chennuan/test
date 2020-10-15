#-*- coding: UTF-8 -*-
from myproject.data.settings import siteId, OpenID1


class GetParkingPayDetail:
    # 注册
    def __init__(self):
        self.ServiceName = "GetParkingPayDetail"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.siteId = siteId
        self.carPlateColor = "001"
        self.carPlateNo = "苏EL16F0"
        self.openId = OpenID1

        self.body = {
        }
        self.expect = {
            "code": 200,
            "data": {
                "carPlateNo": "苏EL16F0",
                "carPlateColor": "001",
                "parkingCode": "PR010072",
                "parkingName": "人民广场P+R停车场",
                "parkingType": "002",
                "orderNo": "20201013143208000148",
                "inTime": "2020-10-13 06:30:08",
                "parkingDuration": "37411",
                "orderAmount": 400,
                "payAmount": 400,
                "orderDetail": [{
                    "orderNo": "20201013143208000148",
                    "inTime": "2020-10-13 06:30:08",
                    "outTime": "2020-10-13 16:53:39",
                    "parkingDuration": "37411",
                    "orderAmount": 400,
                    "orderType": "null",
                    "orderStatus": "0"
                }],
                "couponAccount": 0,
                "merchantExpenses": 0,
                "userType": "null",
                "allowSettleAllFee": "null",
                "payStatus": "000"
            },
            "success": "true",
            "message": "停车缴费详情"
        }