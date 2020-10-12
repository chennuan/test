# 导入logging包
import logging

# 日志基本配置
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'log', 'access.log')
# 日志配置字典
standard_format = '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s'
LOGGING_DIC = {
    'version': 1,
    # 自定义格式
    'formatters': {
        'standard': {
            'format': standard_format
        }
    },
    # 日志接受者，处理日志需要做的事，会将日志输出到不同的位置
    'handlers': {
        # 打印到终端日志
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  #打印到屏幕
            'formatter': 'standard'
        },
        'other': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'formatter': 'standard',
            'filename': path,
            'encoding': 'utf-8'
        }

    },
    # 日志产生者
    'loggers': {
        'logs': {
            'handlers': ['console', 'other'],
            'level': 'DEBUG',
            'propagate': False
        }

    }
}


# logging.basicConfig(
#
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S %p',
#     filename=path,
#     # 设置日志级别
#     # debug --10
#     # info --20
#     # warning -- 30
#     # error --40
#     # critical --50
#     level=30
# )
