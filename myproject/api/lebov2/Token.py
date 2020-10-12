from myproject.data.settings import OpenID1


class Token:
    # 获取token
    def __init__(self, publickey):
        self.ServiceName = "Token"
        self.method = "post"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {
            "username": OpenID1,
            "publicKey": publickey,
            "type": 1
        }
        self.expect = {
            "code": 200,
            "data": {
                "expirationTime": ".*",
                "token": ".*"
            },
            "success": "True",
            "message": "success"
        }