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


@pytest.mark.usefixtures('open_client')
class TestLogin(object):
    def test_login(self, open_client):
        basepage = BasePage()
        # 图片地址
        login_picture_path = os.path.join(p_path.picture_path, 'login')
        # 输入用户名
        if basepage.exists(os.path.join(login_picture_path, '账号.png')):
            name = basepage.exists(os.path.join(login_picture_path, '账号.png'))
            name = (name[0] + 80, name[1])
            double_click(name)
        else:
            basepage.touch(os.path.join(login_picture_path, '输入用户名.png'))
        sleep(2)
        basepage.text(username)
        # 有就清空，没有就直接输入
        if basepage.exists(os.path.join(login_picture_path, '清空密码.png')):
            basepage.double_click(os.path.join(login_picture_path, '清空密码.png'))
        else:

            # 密码输入框
            basepage.touch(os.path.join(login_picture_path, '输入密码.png'))
        sleep(2)
        basepage.text(password)
        # 记住密码
        if basepage.exists(os.path.join(login_picture_path, '勾选.png')):
            basepage.touch(os.path.join(login_picture_path, '勾选.png'))
        sleep(2)
        # 勾选协议
        if basepage.exists(os.path.join(login_picture_path, '勾选.png')):
            basepage.touch(os.path.join(login_picture_path, '勾选.png'))
        sleep(2)
        # 登录
        basepage.touch(os.path.join(login_picture_path, '登录.png'))
        basepage.assert_exists(filepath=os.path.join(login_picture_path, '首页logo.png'), msg="登录成功后_存在logo")
        basepage.touch(os.path.join(login_picture_path, '关闭窗口.png'))
        sleep(1)
        basepage.touch(os.path.join(login_picture_path, '确定关闭.png'), record_pos=(-0.259, 0.092))
