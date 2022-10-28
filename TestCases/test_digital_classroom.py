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
        self.touch(get_path('书本封面'))
        sleep(10)
        self.touch(get_path('数字课堂'))
        if self.exists(get_path('下载')):
            self.touch(get_path('确定'))
            self.assert_exists(get_path('下载中提示'), msg='确定是否在下载中')
            self.touch(get_path('关闭'))
        else:
            self.assert_exists(get_path('资源封面'), msg='确定是否能正常打开')
            self.touch(get_path('关闭资源'))
            self.touch(get_path('确定关闭'))
