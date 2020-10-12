class Publickey:
    # 获取公钥
    def __init__(self):
        self.ServiceName = "Publickey"
        self.method = "get"
        self.openid = "ohURa5IyyvhXBw89X73HPTcJwEAY"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {

        }
        self.expect = {
            "code": 200,
            "data": ".*",
            "success": "True",
            "message": "success"
        }