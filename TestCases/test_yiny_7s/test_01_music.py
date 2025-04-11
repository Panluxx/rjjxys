# -*- coding:utf-8 -*-
# @Time     : 2023/6/5 9:23
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_01_music.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from pywinauto.mouse import move


def get_path(image):
    module_path = os.path.join(p_path.picture_path, r'yiny_7s\music')
    return os.path.join(module_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestMusic(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('音乐'), img_doc='选择音乐学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('音乐欣赏'), img_doc='点击音乐欣赏')
        self.touch(get_path('暂停'), img_doc='点击暂停')
        self.touch(get_path('播放'), img_doc='点击播放')
        self.touch(get_path('下一首'), img_doc='点击下一首')
        self.assert_exists(get_path('下一首章节'), img_doc='检查是否切换成功')
        self.touch(get_path('上一首'), img_doc='点击上一首')
        self.assert_exists(get_path('上一首章节'), img_doc='检查是否切换成功')
        self.touch(get_path('单曲循环'), img_doc='点击单曲循环')
        self.touch(get_path('取消循环'), img_doc='点击取消循环')
        self.touch(get_path('关闭声音'), img_doc='点击关闭声音')
        self.touch(get_path('播放声音'), img_doc='点击播放声音')
        self.swipe((450,950), (886,950), img_doc='拖动进度')
        self.touch(get_path('全屏'), img_doc='全屏')
        self.touch(get_path('退出全屏'), img_doc='点击退出全屏')


