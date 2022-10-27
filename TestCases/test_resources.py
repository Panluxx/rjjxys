# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:54
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_resources.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from time import sleep
from pywinauto.keyboard import SendKeys
from Setting.constant import resource_name, book_code


def get_path(image):
    resources_path = os.path.join(p_path.picture_path, 'resources')
    return os.path.join(resources_path, image)


@pytest.mark.usefixtures('login')
class TestResources(BasePage):
    @pytest.mark.parametrize("test_data", resource_name)
    def test_import_resources(self, login, test_data):
        self.touch(get_path('我的资源.png'))
        sleep(2)
        self.touch(get_path('导入.png'))
        sleep(2)
        self.touch(get_path('下拉框.png'))
        sleep(2)
        self.touch(get_path('路径.png'))
        sleep(2)
        # 文件路径
        self.text(p_path.resources_path)
        sleep(2)
        SendKeys('{ENTER}')
        sleep(2)
        self.touch(get_path('输入文件名.png'))
        sleep(2)
        self.touch(get_path('输入文件名.png'))
        self.text(test_data['name'])
        sleep(2)
        self.touch(get_path('打开.png'))
        sleep(3)
        if test_data['name'] == '音频.mp3':
            self.assert_exists(get_path('音频.png'), msg='对比资源封面')
        elif test_data['name'] == '视频.mp4':
            self.assert_exists(get_path('视频.png'), msg='对比资源封面')
        elif test_data['name'] == '图片.jpg':
            self.assert_exists(get_path('图片.png'), msg='对比资源封面')
        elif test_data['name'] == '动画.swf':
            self.assert_exists(get_path('动画.png'), msg='对比资源封面')
        elif test_data['name'] == '文件.xlsx':
            self.assert_exists(get_path('文件.png'), msg='对比资源封面')
        elif test_data['name'] == '文档.docx':
            self.assert_exists(get_path('文档.png'), msg='对比资源封面')
        else:
            self.assert_exists(get_path('课件.png'), msg='对比资源封面')

    def test_export_resources(self, login):
        self.touch(get_path('我的资源.png'))
        sleep(2)
        self.touch(get_path('导出.png'))
        sleep(2)
        self.touch(get_path('更改目录.png'))
        sleep(2)
        self.touch(get_path('保存.png'))
        sleep(2)
        self.touch(get_path('勾选资源.png'))
        sleep(2)
        self.touch(get_path('确定.png'))
        sleep(2)
        self.assert_exists(get_path('导出提示.png'), msg='对比导出提示')

    def test_create_folder(self, login):
        self.touch(get_path('我的资源.png'))
        sleep(2)
        self.touch(get_path('新建文件夹.png'))
        self.text('test')
        SendKeys('{ENTER}')
        sleep(2)
        self.assert_exists(get_path('文件夹名称.png'), msg='对比文件夹名称')

    def test_download(self, login):
        self.touch(get_path('我的资源.png'))
        sleep(2)
        self.touch(get_path('打开列表.png'))
        sleep(2)
        self.assert_exists(get_path('下载列表.png'), msg='检查是否打开列表')
        sleep(2)
        self.touch(get_path('关闭.png'))

    def test_add(self, login):
        self.touch(get_path('我的资源.png'))
        sleep(2)
        self.touch(get_path('添加课本.png'))
        sleep(2)
        self.touch(get_path('输入激活码.png'))
        self.text(book_code)
        sleep(2)
        self.touch(get_path('激活.png'))
