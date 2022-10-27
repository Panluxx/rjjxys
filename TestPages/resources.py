# -*- coding:utf-8 -*-
# @Time     : 2022/10/27 11:41
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : resources.py
# Software  : PyCharm


from Common.config import p_path
from Common.basepage import BasePage
from airtest.core.api import *
import os


def get_path(image):
    resources_path = os.path.join(p_path.picture_path, 'resources')
    return os.path.join(resources_path, image)


class Resources(BasePage):
    def my_resources(self):
        self.touch(get_path('我的资源.png'))
