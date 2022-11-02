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
from Setting.constant import client_dir, dir
from Setting.constant import username, password
from Common.basepage import BasePage
import os, webbrowser
from Common.config import p_path
from pywinauto.keyboard import SendKeys


@pytest.fixture(scope='module')
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
    webbrowser.open(os.path.realpath(dir()))
    if BasePage().exists(get_path('存放资源的文件.png'), img_doc='存在资源'):
        BasePage().touch(get_path('存放资源的文件.png'), img_doc='存在资源')
        SendKeys('{DELETE}')
    BasePage().touch(get_path('清除后关闭.png'), img_doc='关闭')
    sleep(2)
    APP.kill()
    logger.info('*' * 10 + '测试结束/关闭客户端' + '*' * 10)


def get_path(image):
    login_path = os.path.join(p_path.picture_path, 'login')
    return os.path.join(login_path, image)


@pytest.fixture(scope='module')
def login(open_client):
    basepage = BasePage()
    if basepage.exists(get_path('未勾选.png')):
        name = basepage.exists(get_path('账号.png'))
        if name:
            name = (name[0] + 80, name[1])
            double_click(name)
        else:
            basepage.touch(get_path('输入用户名.png'))
        sleep(2)
        basepage.text(username)
        # 有就清空，没有就直接输入
        if basepage.exists(get_path('清空密码.png')):
            basepage.double_click(get_path('清空密码.png'))
        else:
            # 密码输入框
            basepage.touch(get_path('输入密码.png'))
        sleep(2)
        basepage.text(password)
        # 记住密码
        if basepage.exists(get_path('未勾选.png')):
            basepage.touch(get_path('未勾选.png'))
        sleep(2)
        # 勾选协议
        if basepage.exists(get_path('未勾选.png')):
            basepage.touch(get_path('未勾选.png'))
        sleep(2)
    # 登录
    basepage.touch(get_path('登录.png'))
