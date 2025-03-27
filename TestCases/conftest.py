# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 9:25
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : conftest.py
# Software  : PyCharm


from airtest.core.api import *
from pywinauto.application import Application
import pytest
from Common.logger import logger
from Setting.constant import client_dir
from Setting.constant import username, password
from Common.basepage import BasePage
from Common.config import p_path


@pytest.fixture(scope='function')
def open_client():
    logger.info('*' * 10 + '开始连接/启动设备' + '*' * 10)
    try:
        # 连接设备
        __author__ = "Administrator"
        auto_setup(__file__, devices=["Windows:///"])
        # 启动设备
        APP = Application().start(client_dir())
        logger.info('*' * 10 + '连接/启动设备正常' + '*' * 10)
    except Exception as e:
        logger.warn('*' * 10 + '连接/启动设备异常' + '*' * 10)
        raise e
    yield
    sleep(2)
    APP.kill()
    logger.info('*' * 10 + '测试结束/关闭客户端' + '*' * 10)


def get_path(image):
    login_path = os.path.join(p_path.picture_path, 'login')
    return os.path.join(login_path, f'{image}.png')


@pytest.fixture(scope='function')
def login(open_client):
    basepage = BasePage()
    if basepage.exists(get_path('未勾选'), img_doc='未勾选'):
        name = basepage.exists(get_path('账号'), img_doc='账号')
        if name:
            name = (name[0] + 80, name[1])
            double_click(name)
        else:
            basepage.touch(get_path('输入用户名'), img_doc='点击用户名输入框')
        sleep(2)
        basepage.text(username, img_doc='输入用户名{username}')
        # 有就清空，没有就直接输入
        if basepage.exists(get_path('清空密码'), img_doc='密码输入框'):
            basepage.double_click(get_path('清空密码'), img_doc='双击密码输入框')
        else:
            # 密码输入框
            basepage.touch(get_path('输入密码'), img_doc='点击密码输入框')
        sleep(2)
        basepage.text(password, img_doc=f'输入密码{password}')
        # 记住密码
        if basepage.exists(get_path('未勾选'), img_doc='记住密码未勾选'):
            basepage.touch(get_path('未勾选'), img_doc='勾选记住密码')
        sleep(2)
        # 勾选协议
        if basepage.exists(get_path('未勾选'), img_doc='记住协议未勾选'):
            basepage.touch(get_path('未勾选'), img_doc='勾选并同意协议')
        sleep(2)
    # 登录
    basepage.touch(get_path('登录'), img_doc='点击登录')
    if basepage.exists(get_path('以后再说'), img_doc='以后再说弹框存在'):
        basepage.touch(get_path('以后再说'), img_doc='点击以后再说')

