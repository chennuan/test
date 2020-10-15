#-*- coding: UTF-8 -*-
class Login:
    # 获取公钥
    def __init__(self):
        self.ServiceName = "Login"
        self.method = "get"
        self.openid = "ohURa5IyyvhXBw89X73HPTcJwEAY"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {

        }
        self.expect = ".*"