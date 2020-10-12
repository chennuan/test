class Login:
    def __init__(self):
        self.ServiceName = "Login"
        self.method = "post"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {
            "user": "botest2@huawei.com",
            "pass": "Admin_1234",
            "captcha": ""
        }

        self.expr = {
                "user": "0000000000UKajOnTqmf",
                "userId": "10gd000000UKajOnTqme",
                "tenantId": "0000000000UKajOnTqmf",
                "token": "0000000000UKajOnTqmf:CBDaRJUiCYeUJtse05aZPhfxpVedCRC8QWWHdRNLR2s="
            }
