# -*- coding:utf-8 -*-
# @Time     : 2022/10/27 17:10
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_courseware.py
# Software  : PyCharm

from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    courseware_path = os.path.join(p_path.picture_path, 'courseware')
    return os.path.join(courseware_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestCourseware(BasePage):
    def test_courseware(self, login):
        self.touch(get_path('书本封面'))
        sleep(10)
        self.touch(get_path('教学课件'))
        self.touch(get_path('资源'))
        sleep(2)
        self.assert_exists(get_path('资源封面'), msg='对比打开的资源是否正确')
        sleep(2)
        self.touch(get_path('退出浏览'))
