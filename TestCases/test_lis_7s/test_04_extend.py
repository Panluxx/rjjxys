# -*- coding:utf-8 -*-
# @Time     : 2022/10/28 14:46
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_04_extend.py
# Software  : PyCharm


from airtest.core.api import *
import pytest
from Common.basepage import BasePage
from Common.utils import get_image_path
from pywinauto.mouse import move


# 模块图片目录
MODULE_DIR = 'lis_7s/extend'


def get_path(image):
    """获取当前模块的图片路径"""
    return get_image_path(MODULE_DIR, image)



@pytest.mark.usefixtures('login')
class TestExtend(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('历史'), img_doc='选择历史学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('拓展资源'), img_doc='点击拓展资源')
        sleep(1)
        self.touch(get_path('展开章节'), img_doc='点击展开章节')
        sleep(1)
        self.touch(get_path('资源封面'), img_doc='点击资源封面')
        sleep(1)
        self.assert_exists(get_path('资源内容'), img_doc='检查资源是否正常打开')
        sleep(1)
        self.touch(get_path('关闭资源'), img_doc='点击关闭资源')
        sleep(1)
        name = self.exists(get_path('资源封面'))
        move(name)
        sleep(1)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('确定下载'), img_doc='确定下载')
        if self.exists(get_path('覆盖弹框')):
            self.touch(get_path('确定下载'), img_doc='点击确定下载')
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


