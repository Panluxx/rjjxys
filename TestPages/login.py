# -*- coding:utf-8 -*-
# @Time     : 2022/10/27 9:26
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : login.py
# Software  : PyCharm


from Common.config import p_path
from Common.basepage import BasePage
from airtest.core.api import *
import os


def get_path(image):
    login_path = os.path.join(p_path.picture_path, 'login')
    return os.path.join(login_path, image)


class Login(BasePage):
    def username(self):
        name = self.exists(get_path('账号.png'))
        if name:
            name = (name[0] + 80, name[1])
            double_click(name)

    def click_username(self):
        self.touch(get_path('输入用户名.png'))

    def input_username(self, username):
        self.text(username)

    def clear_password(self):
        if self.exists(get_path('清空密码.png')):
            self.double_click(get_path('清空密码.png'))

    def click_password(self):
        self.touch(get_path('输入密码.png'))

    def input_password(self, password):
        self.text(password)

    def remember_password(self):
        if self.exists(get_path('未勾选.png'), record_pos=(0.194, 0.178)):
            self.touch(get_path('未勾选.png'))

    def click_agreement(self):
        if self.exists(get_path('未勾选.png'), record_pos=(0.195, 0.234)):
            self.touch(get_path('未勾选.png'))

    def click_login(self):
        self.touch(get_path('登录.png'))

    def logo(self):
        self.assert_exists(filepath=get_path('首页logo.png'), msg="登录成功后_存在logo")

    def close(self):
        self.touch(get_path('关闭窗口.png'))

    def ensure(self):
        self.touch(get_path('确定关闭.png'), record_pos=(-0.259, 0.092))
