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
from Setting.constant import resource_name

basepage = BasePage()
# 图片地址
resources_picture_path = os.path.join(p_path.picture_path, 'resources')


@pytest.mark.usefixtures('login')
class TestResources(object):
    @pytest.mark.parametrize("test_data", resource_name)
    def test_import_resources(self, login, test_data):
        basepage.touch(os.path.join(resources_picture_path, '我的资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '导入.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '下拉框.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '路径.png'))
        sleep(2)
        # 文件路径
        basepage.text(p_path.resources_path)
        sleep(2)
        SendKeys('{ENTER}')
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '输入文件名.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '输入文件名.png'))
        basepage.text(test_data['name'])
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '打开.png'))
        sleep(3)
        if test_data['name'] == '音频.mp3':
            basepage.assert_exists(os.path.join(resources_picture_path, '音频.png'), msg='对比资源封面')
        elif test_data['name'] == '视频.mp4':
            basepage.assert_exists(os.path.join(resources_picture_path, '视频.png'), msg='对比资源封面')
        elif test_data['name'] == '图片.jpg':
            basepage.assert_exists(os.path.join(resources_picture_path, '图片.png'), msg='对比资源封面')
        elif test_data['name'] == '动画.swf':
            basepage.assert_exists(os.path.join(resources_picture_path, '动画.png'), msg='对比资源封面')
        elif test_data['name'] == '文件.xlsx':
            basepage.assert_exists(os.path.join(resources_picture_path, '文件.png'), msg='对比资源封面')
        elif test_data['name'] == '文档.docx':
            basepage.assert_exists(os.path.join(resources_picture_path, '文档.png'), msg='对比资源封面')
        else:
            basepage.assert_exists(os.path.join(resources_picture_path, '课件.png'), msg='对比资源封面')

    def test_export_resources(self, login):
        basepage.touch(os.path.join(resources_picture_path, '我的资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '导出.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '更改目录.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '保存.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '勾选资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '确定.png'))
        sleep(2)
        basepage.assert_exists(os.path.join(resources_picture_path, '导出提示.png'), msg='对比导出提示')

    def test_create_folder(self, login):
        basepage.touch(os.path.join(resources_picture_path, '我的资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '新建文件夹.png'))
        basepage.text('test')
        SendKeys('{ENTER}')
        sleep(2)
        basepage.assert_exists(os.path.join(resources_picture_path, '文件夹名称.png'), msg='对比文件夹名称')

    def test_download(self, login):
        basepage.touch(os.path.join(resources_picture_path, '我的资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '打开列表.png'))
        sleep(2)
        basepage.assert_exists(os.path.join(resources_picture_path, '下载列表.png'), msg='检查是否打开列表')
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '关闭.png'))

    def test_add(self, login):
        basepage.touch(os.path.join(resources_picture_path, '我的资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '添加课本.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '输入激活码.png'))
        basepage.text('A12345678')
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '激活.png'))
