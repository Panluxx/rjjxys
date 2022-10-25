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


@pytest.mark.usefixtures('login')
class TestResources(object):
    @pytest.mark.parametrize("test_data", resource_name)
    def test_resources_mp3(self, login, test_data):
        basepage = BasePage()
        # 图片地址
        resources_picture_path = os.path.join(p_path.picture_path, 'resources')
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
            basepage.assert_exists(os.path.join(resources_picture_path, '音频.png'), msg='上传的音频资源_封面显示正确')
        elif test_data['name'] == '视频.mp4':
            basepage.assert_exists(os.path.join(resources_picture_path, '视频.png'), msg='上传的视频资源_封面显示正确')
        elif test_data['name'] == '图片.jpg':
            basepage.assert_exists(os.path.join(resources_picture_path, '图片.png'), msg='上传的图片资源_封面显示正确')
        elif test_data['name'] == '动画.swf':
            basepage.assert_exists(os.path.join(resources_picture_path, '动画.png'), msg='上传的动画资源_封面显示正确')
        elif test_data['name'] == '文件.xlsx':
            basepage.assert_exists(os.path.join(resources_picture_path, '文件.png'), msg='上传的文件资源_封面显示正确')
        elif test_data['name'] == '文档.docx':
            basepage.assert_exists(os.path.join(resources_picture_path, '文档.png'), msg='上传的文档资源_封面显示正确')
        else:
            basepage.assert_exists(os.path.join(resources_picture_path, '课件.png'), msg='上传的课件资源_封面显示正确')
