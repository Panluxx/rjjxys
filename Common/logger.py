# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 9:20
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : logger.py
# Software  : PyCharm

import os
import logging
from Common.config import p_path
from datetime import datetime


class LoggerHandler(logging.Logger):
    def __init__(self,
                 name,
                 level=0,
                 file_name=None,
                 handler_level=0,
                 fmt="%(asctime)s %(name)s %(levelname)s %(filename)s [第%(lineno)d行] %(message)s",
                 **kw
                 ):
        # 继承的方式
        super().__init__(name, level=level)

        # 初始化 handler
        if not file_name:
            handler = logging.StreamHandler()
        else:
            handler = logging.FileHandler(file_name)

        # 设置 handler 的级别
        handler.setLevel(handler_level)
        # 添加 handler
        self.addHandler(handler)
        # 设置 format
        handler_format = logging.Formatter(fmt)
        handler.setFormatter(handler_format)


# 获取当前时间
now_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# 拼接log文件名称
file_name = '{}.log'.format(now_time)
# 传入log日志跟名称，不想生成那么就把file_name写死
logger_path = os.path.join(p_path.log_path, file_name)
logger = LoggerHandler(name="rj_jxy", file_name=logger_path, encoding="utf-8")
