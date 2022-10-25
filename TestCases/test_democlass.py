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

pytest.mark.usefixtures('login')


class TestDemoClass(object):
    def test_demo_class(self, login):
        basepage = BasePage()
        # 图片地址
        module_picture_path = os.path.join(p_path.picture_path, 'module')
        sleep(2)
        # 进入书本
        basepage.touch(os.path.join(module_picture_path, '书本封面.png'))
        sleep(10)
        # 点击模块
        basepage.touch(os.path.join(module_picture_path, '教学课例.png'))
        sleep(5)
        # 暂停
        basepage.touch(os.path.join(module_picture_path, '暂停.png'))
        sleep(5)
        # 播放
        basepage.touch(os.path.join(module_picture_path, '播放.png'))
        sleep(5)
        # 关闭声音
        basepage.touch(os.path.join(module_picture_path, '关闭声音.png'))
        sleep(5)
        # 开启声音
        basepage.touch(os.path.join(module_picture_path, '播放声音.png'))
        sleep(5)
        # 下载
        basepage.touch(os.path.join(module_picture_path, '下载.png'))
        # 确定下载
        basepage.touch(os.path.join(module_picture_path, '确定.png'))
        sleep(5)
        # 拖动进度条
        swipe(Template(os.path.join(module_picture_path, '拖动.png'), record_pos=(-0.345, 0.141),
                       resolution=(1920, 1080)), vector=[0.3266, 0.0009])
        sleep(5)
        # 窗口放大
        basepage.touch(os.path.join(module_picture_path, '窗口放大.png'))
        sleep(5)
        # 窗口缩小
        basepage.touch(os.path.join(module_picture_path, '窗口缩小.png'))
        sleep(5)
        # 窗口常规（小）
        basepage.touch(os.path.join(module_picture_path, '窗口常规（小）.png'))
        sleep(5)
        # 窗口常规（大）
        basepage.touch(os.path.join(module_picture_path, '窗口常规（大）.png'))
        sleep(5)
        # 模块窗口关闭
        basepage.touch(os.path.join(module_picture_path, '模块窗口关闭.png'))
        sleep(5)
        # 书本窗口关闭
        basepage.touch(os.path.join(module_picture_path, '书本窗口关闭.png'))
        sleep(5)
        # 确定关闭
        basepage.touch(os.path.join(module_picture_path, '确定关闭.png'))
        sleep(5)
