#-*- coding: UTF-8 -*-


class AppPay:
    # 注册
    def __init__(self):
        self.ServiceName = "AppPay"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {

        }
        self.expect = {
            "msg": "success",
            "code": "200",
            "data": {
                "timeStamp": "1602580836",
                "package": "prepay_id=wx13172036797163b37c4486a37f5c930000",
                "paySign": "1A8DAC51ED4706B434D906C4DAE10564",
                "appId": "wx9a0d589f4601c123",
                "signType": "MD5",
                "nonceStr": "1602580836856"
            }
        }