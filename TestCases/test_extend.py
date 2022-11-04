# -*- coding:utf-8 -*-
# @Time     : 2022/10/28 14:46
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_extend.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from pywinauto.mouse import move


def get_path(image):
    courseware_path = os.path.join(p_path.picture_path, 'extend')
    return os.path.join(courseware_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestExtend(BasePage):
    def test_extend(self, login):
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        sleep(10)
        self.touch(get_path('拓展资源'), img_doc='点击拓展资源')
        self.touch(get_path('资源'), img_doc='点击资源')
        self.assert_exists(get_path('资源内容'), img_doc='检查资源内容是否正确')
        self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
        name = self.exists(get_path('资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.assert_exists(get_path('下载弹框'), img_doc='检查是否有下载弹框')
        self.touch(get_path('确定'), img_doc='点击确定')
