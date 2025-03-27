# -*- coding:utf-8 -*-
# @Time     : 2022/10/28 14:13
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_05_teacher_book.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage


def get_path(image):
    courseware_path = os.path.join(p_path.picture_path, r'lis_7s\teacher_book')
    return os.path.join(courseware_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestTeacherBook(BasePage):
    def test_teacher_book(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('历史'), img_doc='选择历史学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        sleep(2)
        self.touch(get_path('电子教材'), img_doc='点击电子教材')
        if self.exists(get_path('缓存失败'), img_doc='界面缓存失败'):
            self.touch(get_path('缓存失败'), img_doc='点击重新缓存')
        self.assert_exists(get_path('打开页面'), img_doc='检查是否打开')
        self.touch(get_path('下一页'), img_doc='点击下一页')
        self.assert_exists(get_path('下一页内容'), img_doc='检查下一页内容')
        sleep(1)
        self.touch(get_path('目录'), img_doc='点击目录')
        self.assert_exists(get_path('目录内容'), img_doc='检查目录内容')
        self.touch(get_path('上一页'), img_doc='点击上一页')
        self.assert_exists(get_path('上一页内容'), img_doc='检查上一页内容')
        sleep(1)
        self.touch(get_path('放大'), img_doc='点击放大按钮')
        self.assert_exists(get_path('放大后页面'), img_doc='检查放大后页面')
        sleep(1)
        self.touch(get_path('缩小'), img_doc='点击缩小按钮')
        self.assert_exists(get_path('上一页内容'), img_doc='检查上一页内容')
        sleep(1)
        self.text('20', img_doc='输入页码20')
        self.touch(get_path('跳转'), img_doc='点击跳转')
        self.assert_exists(get_path('跳转页码后的资源'), img_doc='检查跳转页码后的资源')
        self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
