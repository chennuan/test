#-*- coding: UTF-8 -*-
class GueryLoadingActivity:
    # 绑定车辆
    def __init__(self):
        self.ServiceName = "GueryLoadingActivity"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.body = {

        }
        self.expect = {
            "code": 200,
            "data": "null",
            "success": "true",
            "message": "获取列表"
        }