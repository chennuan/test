# 导入requests包
import requests

# 新建类，直接获得验证码图片接口对象

# 类名使用大驼峰命名法
class CnValiDateImage():
    # 新建方法，直接获得验证码图片方法

    # 方法名全部小写，以api_请求方法_接口名
    def api_post_cnvalidateimage(self, url, bystring):

        # header定义
        headers = {"Content-Type": "application/x-www-form-urlencoded","Content-Length": "length"}

        # data定义
        data = {"byString": bystring}

        # 调用post并返回响应对象
        return requests.post(url, data=data, headers=headers)

"""
url、bystring都从data数据文件中读取
"""