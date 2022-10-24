# -*- coding:utf-8 -*-
# @Time     :  9:43
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_login.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
from Common.basepage import BasePage
import os
import pytest
from Setting.constant import *


@pytest.mark.usefixtures('open_client')
class TestLogin(object):
    def test_login(self, open_client):
        basepage = BasePage()
        # 图片地址
        login_picture_path = os.path.join(p_path.picture_path, 'login')
        # 账号输入框
        basepage.touch(os.path.join(login_picture_path, '输入用户名.png'))
        # 有就清空，没有就直接输入
        if exists(Template(os.path.join(login_picture_path, '清空用户名.png'))):
            basepage.double_click(os.path.join(login_picture_path, '清空用户名.png'))
        basepage.text(username)
        # 密码输入框
        basepage.touch(os.path.join(login_picture_path, '输入密码.png'))
        #  有就清空，没有就直接输入
        if exists(Template(os.path.join(login_picture_path, '清空密码.png'))):
            basepage.double_click(os.path.join(login_picture_path, '清空密码.png'))
        basepage.text(password)
        sleep(2)
        # 记住密码
        if exists(Template(os.path.join(login_picture_path, '勾选.png'))):
            basepage.touch(os.path.join(login_picture_path, '勾选.png'))
        sleep(2)
        # 勾选协议
        if exists(Template(os.path.join(login_picture_path, '勾选.png'))):
            basepage.touch(os.path.join(login_picture_path, '勾选.png'))
        sleep(2)
        # 登录
        basepage.touch(os.path.join(login_picture_path, '登录.png'))
        basepage.assert_exists(os.path.join(login_picture_path, '首页logo.png'), "登录成功后_存在logo")
        basepage.touch(os.path.join(login_picture_path, '关闭窗口.png'))
        basepage.touch(os.path.join(login_picture_path, '确定关闭.png'))