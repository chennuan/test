#-*- coding: UTF-8 -*-
from myproject.data.settings import siteId


class GetBindCarsList:
    # 注册
    def __init__(self):
        self.ServiceName = "GetBindCarsList"
        self.method = "get"
        self.header = {
            "Content-Type": "application/json"
        }
        self.siteId = siteId
        self.userId = "157811"
        self.body = {

        }
        self.expect = ".*"