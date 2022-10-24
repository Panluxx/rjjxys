# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:22
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : basepage.py
# Software  : PyCharm


from airtest.core.api import *
from Common.logger import logger


class BasePage(object):

    def template(self, filepath):
        try:
            logger.info(f'开始寻找图片：{filepath}')
            path = Template(filepath)
        except Exception as e:
            logger.warn(f'{filepath}图片无法点击')
        else:
            logger.info(f'{path}图片存在')
            return path

    def touch(self, filepath, record_pos=(-0.259, 0.092), resolution=(1920, 1080)):
        try:
            touch(self.template(filepath), record_pos=record_pos, resolution=resolution)
            logger.info(f'开始点击图片：{filepath}')
        except Exception as e:
            logger.warn(f'{filepath}图片无法点击')

    def text(self, msg=None):
        try:
            text(msg)
            logger.info(f'输入text值为: {msg}')
        except Exception as e:
            logger.warn(f'{msg}值非法')

    def swipe(self):
        pass

    def assert_exists(self, filepath, msg=''):
        try:
            assert_exists(self.template(filepath), msg=msg)
            logger.info(f'断言成功，断言的图片为：{filepath}')
        except Exception as e:
            logger.error('断言失败')

    def double_click(self, filepath):
        try:
            double_click(self.template(filepath))
            logger.info(f'双击清除图片为：{filepath}')
        except Exception as e:
            logger.error('无法清除')
