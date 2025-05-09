# -*- coding:utf-8 -*-
# @Time     : 2022/10/28 14:46
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_04_extend.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from pywinauto.mouse import move


def get_path(image):
    courseware_path = os.path.join(p_path.picture_path, r'tiy_34q\extend')
    return os.path.join(courseware_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestExtend(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('体育与健康'), img_doc='选择体育与健康学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('拓展资源'), img_doc='点击拓展资源')
        self.touch(get_path('展开章节'), img_doc='点击展开章节')
        self.touch(get_path('资源封面'), img_doc='点击资源封面')
        sleep(1)
        self.assert_exists(get_path('资源内容'), img_doc='检查资源是否正常打开')
        sleep(5)
        # 窗口会失去焦点，无法使用move
        self.click_key('{ESC}')
        self.touch(get_path('暂停'), img_doc='点击暂停按钮')
        self.touch(get_path('播放'), img_doc='点击播放按钮')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量按钮')
        self.touch(get_path('倍速'), img_doc='点击倍速按钮')
        self.touch(get_path('2.0x倍速'), img_doc='点击2.0x按钮')
        self.touch(get_path('恢复音量'), img_doc='点击恢复音量按钮')
        self.touch(get_path('全屏'), img_doc='点击全屏按钮')
        self.click_key('{ESC}')
        self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
        # 移动到资源封面
        name = self.exists(get_path('资源封面'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('确定下载'), img_doc='确定下载')
        if self.exists(get_path('覆盖弹框')):
            self.touch(get_path('取消下载'), img_doc='点击取消下载')
        sleep(1)
        # 批量单个下载
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('批量单个下载'), img_doc='选择单个下载')
        self.touch(get_path('点击下载'), img_doc='点击下载')
        self.touch(get_path('确定下载'), img_doc='确定下载')
        sleep(1)
        if self.exists(get_path('资源已存在')):
            self.touch(get_path('批量确定'), img_doc='点击批量确定下载')
        # 批量全选下载
        sleep(2)
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='点击全选')
        self.touch(get_path('点击下载'), img_doc='点击下载')
        self.touch(get_path('确定下载'), img_doc='确定下载')
        if self.exists(get_path('资源已存在')):
            self.touch(get_path('批量确定'), img_doc='点击批量确定下载')
