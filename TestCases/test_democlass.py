# -*- coding:utf-8 -*-
# @Time     :  16:04
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_democlass.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    module_path = os.path.join(p_path.picture_path, 'democlass')
    return os.path.join(module_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestDemoClass(BasePage):
    def test_demo_class(self, login):
        self.touch(get_path('书本封面'))
        self.touch(get_path('片头'))
        self.touch(get_path('教学课例'))
        sleep(2)
        self.touch(get_path('暂停'))
        self.touch(get_path('播放'))
        self.touch(get_path('关闭声音'))
        self.touch(get_path('播放声音'))
        self.touch(get_path('下载'))
        self.touch(get_path('确定'))
        self.swipe(get_path('拖动'), record_pos=(-0.345, 0.141), vector=[0.3266, 0.0009])
        self.touch(get_path('窗口放大'))
        self.touch(get_path('窗口缩小'))
        self.touch(get_path('窗口常规（小）'))
        self.touch(get_path('窗口常规（大）'))
        self.touch(get_path('模块窗口关闭'))
        self.touch(get_path('播放片尾'))
        self.touch(get_path('片尾'))
        self.touch(get_path('书本窗口关闭'))
        self.touch(get_path('确定关闭'))
