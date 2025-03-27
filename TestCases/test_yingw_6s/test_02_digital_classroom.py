# -*- coding:utf-8 -*-
# @Time     : 2022/10/27 16:51
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_02_digital_classroom.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    classroom_path = os.path.join(p_path.picture_path, r'yingw_6s\digital_classroom')
    return os.path.join(classroom_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestDigitalClassroom(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('数字课堂'), img_doc='点击备课资源')
        if self.exists(get_path('下载')):
            self.touch(get_path('确定'), img_doc='点击确定')
            self.assert_exists(get_path('下载中提示'), img_doc='检查资源是否在下载')
            self.touch(get_path('关闭'), img_doc='点击关闭')
        else:
            self.assert_exists(get_path('资源内容'), img_doc='检查资源是否正常打开')
            self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
            self.touch(get_path('确定关闭'), img_doc='点击确定关闭')
