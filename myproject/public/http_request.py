#-*- coding: UTF-8 -*-
import json
import re

import requests

from myproject.api.Login import Login
from myproject.api.lebov2.PublicKey import Publickey
from myproject.api.lebov2.Token import Token
from myproject.data import endpoints
from myproject.public import logs_add
from myproject.public.cheack import comper_str, comper_json
from myproject.logging import config, getLogger
from myproject.api.lebov2.Register import Register


config.dictConfig(logs_add.LOGGING_DIC)
log = getLogger("logs")


class HttpRequest:


    def __init__(self, Service):
        self.service = Service
        self.__parese()
        self.session = requests.session()

    def __parese(self):
        # 判断object对象中是否存在name属性
        if hasattr(self.service, 'ServiceName'):
            self.url = getattr(endpoints, self.service.ServiceName)
            for k in self.service.__dict__:
                log.info("输出获取的属性"+ k)
            if "{" in self.url:
                self.url = self.url.format(**self.service.__dict__)
            # print(self.url)

        if hasattr(self.service, 'method'):
            self.method = self.service.method
            # print(self.method)

        if hasattr(self.service, 'header'):
            self.header = self.service.header
            # print(self.header)

    def cheack(self):
        success_code = "200"
        comper_str(success_code, self.response.status_code)
        if str(self.service.expect).startswith("{"):
            comper_json(self.service.expect, self.response.json())
        else:
            comper_str(self.service.expect, self.response.json())

    def send(self):
        # 2、解析body
        self.__auth()
        self.__body()
        print("")
        print_header = json.dumps(self.header)
        log.info("--------------------------------["+self.service.ServiceName+" Start]-----------------------------")
        log.info("[URl: ]"+self.url)
        log.info("[Request Header: ]" + print_header)
        log.info("[Request Body: ]" + self.print_body)

        self.response = self.session.request(method=self.method, url=self.url, params=None, data=self.body,
                                        headers=self.header)

        log.info("[Response Status_Code: ]" +str(self.response.status_code))
        log.info("[Response Text: ]" +self.response.text)


    def __body(self):
        if self.method == "get":
            self.body = len(self.service.body) > 0 and "?" or ""
            self.body = self.body + self.__dictoer(self.service.body)
            self.url = self.url + self.body
            self.print_body = json.dumps(self.service.body)
        elif "application/json" == self.service.header['Content-Type']:
            self.body = json.dumps(self.service.body, ensure_ascii=False).encode('utf-8')
            self.print_body = json.dumps(self.service.body)


    def __auth(self):
        # if self.url.endswith('sessions'):
        #     return
        # elif self.url.endswith('toh'):
        #     return
        if self.url.endswith('register'):
            return
        elif 'publicKey' in self.url:
            return
        elif 'token' in self.url:
            return
        else:
            access_token = self.getlebotoken()
            # self.header = {
            #     "Content-Type": "application/json",
            #     "Cookie": "access-token="+access_token[0]
            # }
            self.header = {
                "Content-Type": "application/json",
                "token": access_token
            }

    def getlebotoken(self):

        # 获取publickey
        service = Publickey()
        request = HttpRequest(service)
        request.send()
        request.cheack()
        res = json.loads(request.response.text)
        publickey = res['data']

        # 根据获取的publickey获取token值
        service = Token(publickey)
        request = HttpRequest(service)
        request.send()
        request.cheack()
        restoken = json.loads(request.response.text)
        token = restoken['data']['token']

        return token

    def __dictoer(self, dic):
        path = ""
        for (k, v) in dic.items():
            path = path + k + "=" + v + "&"
        # print(path)
        return path[0:-1]

    # def gettoken(self):
    #         # 实例化Login类
    #         service = Login()
    #         # 实例化HttpRequest类，并将service中的值带入
    #         request = HttpRequest(service)
    #         # 使用request对象访问HttpRequest中的方法
    #         response = request.send()
    #         access_token = str(response.headers['Set-Cookie'])
    #         access_token = re.findall(r"access-token=(.*?);", access_token)
    #         return access_token

