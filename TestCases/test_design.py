# -*- coding:utf-8 -*-
# @Time     : 2022/10/28 13:56
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_design.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    courseware_path = os.path.join(p_path.picture_path, 'design')
    return os.path.join(courseware_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestDesign(BasePage):
    def test_design(self, login):
        self.touch(get_path('书本封面'))
        sleep(10)
        self.touch(get_path('教学设计'))
        self.touch(get_path('资源封面'))
        self.assert_exists(get_path('资源内容'), msg='对比打开的资源是否正确')
        self.touch(get_path('关闭资源'))
