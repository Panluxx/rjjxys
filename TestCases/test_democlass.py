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
    return os.path.join(module_path, image)


pytest.mark.usefixtures('login')


class TestDemoClass(BasePage):
    def test_demo_class(self, login):
        # 进入书本
        self.touch(get_path('书本封面.png'))
        sleep(10)
        # 点击模块
        self.touch(get_path('教学课例.png'))
        # 暂停
        self.touch(get_path('暂停.png'))
        # 播放
        self.touch(get_path('播放.png'))
        # 关闭声音
        self.touch(get_path('关闭声音.png'))
        # 开启声音
        self.touch(get_path('播放声音.png'))
        # 下载
        self.touch(get_path('下载.png'))
        # 确定下载
        self.touch(get_path('确定.png'))
        # 拖动进度条
        swipe(Template(get_path('拖动.png'), record_pos=(-0.345, 0.141),
                       resolution=(1920, 1080)), vector=[0.3266, 0.0009])
        # 窗口放大
        self.touch(get_path('窗口放大.png'))
        # 窗口缩小
        self.touch(get_path('窗口缩小.png'))
        # 窗口常规（小）
        self.touch(get_path('窗口常规（小）.png'))
        # 窗口常规（大）
        self.touch(get_path('窗口常规（大）.png'))
        # 模块窗口关闭
        self.touch(get_path('模块窗口关闭.png'))
        # 书本窗口关闭
        self.touch(get_path('书本窗口关闭.png'))
        # 确定关闭
        self.touch(get_path('确定关闭.png'))
