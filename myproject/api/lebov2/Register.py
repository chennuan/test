#-*- coding: UTF-8 -*-
class Register:
    # 注册
    def __init__(self):
        self.ServiceName = "Register"
        self.method = "post"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {
            "nickName": "我叫李狗蛋",
            "gender": 2,
            "language": "zh_CN",
            "city": "沈阳",
            "province": "辽宁",
            "country": "中国",
            "avatarUrl": "https://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKUA1Nles5pr4qSYwcwcFqjFKNxWPrA8luJYdWXB4ub9YB0OD5sNJD7mkHpcnPRK45BnXtVen51DQ/132",
            "openId": "ohURa5IyyvhXBw89X73HPTcJwEAY"
        }
        self.expect = {
            "code": 200,
            "data": ".*",
            "success": "True",
            "message": "注册成功"
        }