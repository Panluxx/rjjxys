# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:22
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : basepage.py
# Software  : PyCharm


from airtest.core.api import *
from Common.logger import logger


class BasePage(object):

    def template(self, filepath, record_pos=None, resolution=(1920, 1080)):
        try:
            logger.info(f'开始寻找图片：{filepath}')
            path = Template(filepath, record_pos=record_pos, resolution=resolution)
        except Exception as e:
            logger.warn(f'{filepath}图片无法点击')
            raise e
        else:
            return path

    def exists(self, filepath, record_pos=None, resolution=(1920, 1080)):
        try:
            path = exists(self.template(filepath, record_pos=record_pos, resolution=resolution))
            logger.info(f'{filepath}图片存在')
        except Exception as e:
            logger.warn(f'{filepath}图片不存在')
            return False
        else:
            return path

    def touch(self, filepath, record_pos=None, resolution=(1920, 1080)):
        try:
            touch(self.template(filepath, record_pos=record_pos, resolution=resolution))
            logger.info(f'开始点击图片：{filepath}')
        except Exception as e:
            logger.warn(f'{filepath}图片无法点击')
            raise e

    def text(self, msg=None):
        try:
            text(msg)
            logger.info(f'输入text值为: {msg}')
        except Exception as e:
            logger.warn(f'{msg}值非法')
            raise e

    def swipe(self):
        pass

    def assert_exists(self, filepath, record_pos=None, resolution=(1920, 1080), msg=''):
        try:
            assert_exists(self.template(filepath, record_pos=record_pos, resolution=resolution), msg=msg)
            logger.info(f'断言成功：msg值为：{msg}')
        except Exception as e:
            logger.error('断言失败')
            raise e

    def double_click(self, filepath, record_pos=None, resolution=(1920, 1080)):
        try:
            double_click(self.template(filepath, record_pos=record_pos, resolution=resolution))
            logger.info(f'双击清除图片为：{filepath}')
        except Exception as e:
            logger.error('无法清除')
            raise e
