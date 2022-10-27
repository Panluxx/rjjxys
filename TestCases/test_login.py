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
from Setting.constant import username, password


def get_path(image):
    login_path = os.path.join(p_path.picture_path, 'login')
    return os.path.join(login_path, image)


@pytest.mark.usefixtures('open_client')
class TestLogin(BasePage):
    @pytest.mark.login
    def test_login(self, open_client):
        name = self.exists(get_path('账号.png'))
        if name:
            name = (name[0] + 80, name[1])
            double_click(name)
        else:
            self.touch(get_path('输入用户名.png'))
        self.text(username)
        # 有就清空，没有就直接输入
        if self.exists(get_path('清空密码.png')):
            self.double_click(get_path('清空密码.png'))
        else:
            # 密码输入框
            self.touch(get_path('输入密码.png'))
        self.text(password)
        # 记住密码
        if self.exists(get_path('未勾选.png')):
            self.touch(get_path('未勾选.png'))
        # 勾选协议
        if self.exists(get_path('未勾选.png')):
            self.touch(get_path('未勾选.png'))
        # 登录
        self.touch(get_path('登录.png'))
        self.assert_exists(filepath=get_path('首页logo.png'), msg="登录成功后_存在logo")
        self.touch(get_path('关闭窗口.png'))
        self.touch(get_path('确定关闭.png'), record_pos=(-0.259, 0.092))
