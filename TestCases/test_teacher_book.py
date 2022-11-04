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
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        sleep(10)
        self.touch(get_path('电子教材'), img_doc='点击电子教材')
        self.assert_exists(get_path('资源封面'), img_doc='检查资源封面')
        self.touch(get_path('下一页'), img_doc='点击下一页')
        self.assert_exists(get_path('翻页内容'), img_doc='检查翻页内容')
        sleep(1)
        self.touch(get_path('目录'), img_doc='点击目录')
        self.assert_exists(get_path('目录内容'), img_doc='检查目录内容')
        self.touch(get_path('上一页'), img_doc='点击上一页')
        self.assert_exists(get_path('翻页内容'), img_doc='检查翻页内容')
        sleep(1)
        self.text('20', img_doc='输入页码20')
        self.touch(get_path('跳转'), img_doc='点击跳转')
        self.assert_exists(get_path('跳转页码'), img_doc='检查跳转页码')
        self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
