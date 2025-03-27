# -*- coding:utf-8 -*-
# @Time     : 2023/5/30 11:22
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_01_textbook_explain.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from pywinauto.mouse import move


def get_path(image):
    module_path = os.path.join(p_path.picture_path, r'yingw_3s\textbook_explain')
    return os.path.join(module_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestTextbookExplain(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.assert_exists(get_path('模块布局'))
        self.touch(get_path('教材解析'), img_doc='点击教材解析')
        self.assert_exists(get_path('教材解析布局'), img_doc='检查是否默认播放第一个资源')
        self.touch(get_path('暂停'), img_doc='点击暂停')
        self.assert_exists(get_path('暂停布局'), img_doc='检查是否暂停')
        self.touch(get_path('播放'), img_doc='点击播放')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量')
        self.touch(get_path('倍速'), img_doc='点击倍速')
        self.touch(get_path('2.0倍速'), img_doc='点击2.0倍速')
        self.assert_exists(get_path('检查2.0倍速'), img_doc='检查是否切换成功')
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('确定'), img_doc='点击确定')
        # 验证下载
        self.touch(get_path('下载'), img_doc='点击下载')
        self.assert_exists(get_path('下载中'), img_doc='检查是否在下载中')
        self.touch(get_path('恢复音量'), img_doc='点击恢复音量')
        # 检查拖动
        # self.swipe(get_path('拖动进度'), record_pos=(-0.107, 0.219), vector=[0.0005, 0.0037], img_doc='拖动进度条')
        # self.assert_exists(get_path('拖动后检查'))
        # 切换按钮
        self.touch(get_path('下一个'), img_doc='点击下一个按钮')
        sleep(5)
        self.touch(get_path('上一个'), img_doc='点击上一个按钮')
        # 切换目录
        self.touch(get_path('第一个目录'), img_doc='点击切换第一个目录')
        self.assert_exists(get_path('第一个目录时间'), img_doc='检查第一个目录时间')
        self.touch(get_path('第二个目录'), img_doc='点击切换第二个目录')
        self.assert_exists(get_path('第二个目录时间'), img_doc='检查第二个目录时间')
        # 切换窗口
        self.touch(get_path('返回'), img_doc='点击返回')
        self.touch(get_path('教材解析'), img_doc='点击教材解析')
        sleep(1)
        self.touch(get_path('切换窗口'), img_doc='点击窗口按钮')
        self.assert_exists(get_path('窗口切换的页面'), img_doc='检查是否切换成功')
        # 切换资源
        sleep(5)
        self.touch(get_path('切换资源'), img_doc='点击切换资源')
        self.assert_exists(get_path('切换后界面'), img_doc='检查页面是否切换成功')
        self.touch(get_path('退出模块'), img_doc='点击退出模块')

