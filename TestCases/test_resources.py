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


@pytest.mark.usefixtures('login')
class TestResources(object):
    def test_resources(self, login):
        basepage = BasePage()
        # 图片地址
        resources_picture_path = os.path.join(p_path.picture_path, 'resources')
        basepage.touch(os.path.join(resources_picture_path, '我的资源.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '导入.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '输入文件名.png'))
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '输入文件名.png'))
        basepage.text('音频.mp3')
        sleep(2)
        basepage.touch(os.path.join(resources_picture_path, '打开.png'))
        sleep(3)
        basepage.assert_exists(os.path.join(resources_picture_path, '音频.png'), msg='上传的音频资源_封面显示正确')
