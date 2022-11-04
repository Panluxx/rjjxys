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
    return os.path.join(login_path, f'{image}.png')


@pytest.fixture(scope='function')
def click_client(open_client):
    BasePage().touch(get_path('调起客户端'), img_doc='调起客户端')


@pytest.mark.usefixtures('click_client')
class TestLogin(BasePage):
    @pytest.mark.login
    def test_user_agreement(self, click_client):
        self.touch(get_path('用户协议'), img_doc='打开用户协议')
        self.assert_exists(filepath=get_path('用户协议地址'), img_doc='查看地址')
        self.assert_exists(filepath=get_path('用户协议标题'), img_doc='查看标题')

    def test_privacy_policy(self, click_client):
        self.touch(get_path('隐私政策'), img_doc='打开隐私政策')
        self.assert_exists(filepath=get_path('隐私政策地址'), img_doc='查看地址')
        self.assert_exists(filepath=get_path('隐私政策标题'), img_doc='查看标题')

    def test_login(self, click_client):
        name = self.exists(get_path('账号'), img_doc='账号输入框存在')
        if name:
            name = (name[0] + 80, name[1])
            double_click(name)
        else:
            self.touch(get_path('输入用户名'), img_doc='输入账号')
        self.text(username, img_doc=f'输入用户名{username}')
        # 有就清空，没有就直接输入
        if self.exists(get_path('清空密码'), img_doc='密码输入框'):
            self.double_click(get_path('清空密码'), img_doc='双击密码输入框')
        else:
            # 密码输入框
            self.touch(get_path('输入密码'), img_doc='点击密码输入框')
        self.text(password, img_doc=f'输入密码{password}')
        # 记住密码
        if self.exists(get_path('未勾选'), img_doc='记住密码未勾选'):
            self.touch(get_path('未勾选'), img_doc='勾选记住密码')
        # 勾选协议
        if self.exists(get_path('未勾选'), img_doc='记住协议未勾选'):
            self.touch(get_path('未勾选'), img_doc='勾选并同意协议')
        # 登录
        self.touch(get_path('登录'), img_doc='点击登录')
        self.assert_exists(filepath=get_path('首页logo'), img_doc='检查首页logo')
        self.touch(get_path('关闭窗口'), img_doc='关闭窗口')
        self.touch(get_path('确定关闭'), record_pos=(-0.259, 0.092), img_doc='确定关闭')
