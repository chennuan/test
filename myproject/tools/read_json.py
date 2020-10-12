# 导包 json
import json

"""
# 编写数据存储文件data.json

# 读取data.josn文件

# 使用参数化动态获取参数数据
"""


class ReadJson():

    # 使用函数封装，可以调用
    # 初始化函数
    def __init__(self, filename):
            self.filename = "../data/" + filename

    def read_json(self):
        # 打开json文件，并获取文件流
        # with open("../data/data.json", "r", encoding="utf-8") as f:
        #     # 调用load方法加载文件流
        #     return json.load(f)

        # 动态替换数据文件
        with open(self.filename, "r", encoding="utf-8") as f:
            # 调用load方法加载文件流
            return json.load(f)

# 测试类中方法是否成功运行


#if __name__ == '__main__':
