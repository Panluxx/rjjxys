# -*- coding:utf-8 -*-
# @Time     : 2022/10/28 14:13
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_teacher_book.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    courseware_path = os.path.join(p_path.picture_path, 'teacher_book')
    return os.path.join(courseware_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestTeacherBook(BasePage):
    def test_teacher_book(self, login):
        self.touch(get_path('书本封面'))
        sleep(10)
        self.touch(get_path('电子教材'))
        self.assert_exists(get_path('资源封面'), msg='对比打开的资源是否正确')
        self.touch(get_path('下一页'))
        self.assert_exists(get_path('翻页内容'), msg='对比翻页的内容是否正确')
        sleep(1)
        self.touch(get_path('目录'))
        self.assert_exists(get_path('目录内容'), msg='对比目录的内容是否正确')
        self.touch(get_path('上一页'))
        self.assert_exists(get_path('翻页内容'), msg='对比翻页的内容是否正确')
        sleep(1)
        self.text('20')
        self.touch(get_path('跳转'))
        self.assert_exists(get_path('跳转内容'), msg='对比跳转的内容是否正确')
        self.touch(get_path('关闭资源'))
