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

pytest.mark.usefixtures('login')


class TestDemoClass(object):
    def test_demo_class(self, login):
        # 图片地址
        module_picture_path = os.path.join(p_path.picture_path, 'module')
        touch(Template(os.path.join(module_picture_path, 'tpl1666165422051.png'), record_pos=(-0.259, 0.092),
                       resolution=(1920, 1080)))
        sleep(2)
        # 进入书本
        touch(Template(os.path.join(module_picture_path, 'tpl1666159055426.png'), record_pos=(0.077, -0.163),
                       resolution=(858, 770)))
        sleep(10)
        # 点击模块
        touch(Template(os.path.join(module_picture_path, 'tpl1666159097440.png'), record_pos=(-0.099, -0.119),
                       resolution=(858, 770)))
        sleep(5)
        # 暂停
        touch(Template(os.path.join(module_picture_path, 'tpl1666163502226.png'), record_pos=(-0.369, 0.124),
                       resolution=(1920, 1080)))
        sleep(5)
        # 播放
        touch(Template(os.path.join(module_picture_path, 'tpl1666163616266.png'), record_pos=(-0.291, 0.124),
                       resolution=(1920, 1080)))
        sleep(5)
        # 关闭声音
        touch(Template(os.path.join(module_picture_path, 'tpl1666163633656.png'), record_pos=(-0.023, 0.138),
                       resolution=(1920, 1080)))
        sleep(5)
        # 开启声音
        touch(Template(os.path.join(module_picture_path, 'tpl1666163644480.png'), record_pos=(-0.024, 0.138),
                       resolution=(1920, 1080)))
        sleep(5)
        # 下载
        touch(Template(os.path.join(module_picture_path, 'tpl1666163659088.png'), record_pos=(0.054, 0.138),
                       resolution=(1920, 1080)))
        # 确定下载
        touch(Template(os.path.join(module_picture_path, 'tpl1666163674512.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 拖动进度条
        swipe(Template(os.path.join(module_picture_path, 'tpl1666165609410.png'), record_pos=(-0.345, 0.141),
                       resolution=(1920, 1080)), vector=[0.3266, 0.0009])
        sleep(5)
        # 窗口放大
        touch(Template(os.path.join(module_picture_path, 'tpl16661656090952.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 窗口缩小
        touch(Template(os.path.join(module_picture_path, 'tpl16661656090958.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 窗口常规（小）
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091005.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 窗口常规（大）
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091006.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 模块窗口关闭
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091012.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 书本窗口关闭
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091031.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 确定关闭
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091022.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 程序窗口关闭
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091031.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
        sleep(5)
        # 确定关闭
        touch(Template(os.path.join(module_picture_path, 'tpl16661656091022.png'), record_pos=(-0.285, 0.089),
                       resolution=(1920, 1080)))
