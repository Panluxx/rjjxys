# -*- coding:utf-8 -*-
# @Time     : 2022/10/27 16:51
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_digital_classroom.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    classroom_path = os.path.join(p_path.picture_path, 'classroom')
    return os.path.join(classroom_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestClassRoom(BasePage):
    def test_class_room(self, login):
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        sleep(10)
        self.touch(get_path('数字课堂'), img_doc='点击数字课堂')
        if self.exists(get_path('下载')):
            self.touch(get_path('确定'), img_doc='点击确定')
            self.assert_exists(get_path('下载中提示'), img_doc='检查资源是否在下载')
            self.touch(get_path('关闭'), img_doc='点击关闭')
        else:
            self.assert_exists(get_path('资源封面'), img_doc='检查资源是否正常打开')
            self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
            self.touch(get_path('确定关闭'), img_doc='点击确定关闭')
