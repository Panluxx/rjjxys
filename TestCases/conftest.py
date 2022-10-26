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
from Common.config import p_path
import os
from time import sleep
from Setting.constant import client_dir
from Common.basepage import BasePage
from Setting.constant import username, password


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
    sleep(5)
    APP.kill()
    logger.info('*' * 10 + '测试结束/关闭客户端' + '*' * 10)


@pytest.fixture(scope='module')
def login(open_client):
    # 图片地址
    basepage = BasePage()
    module_picture_path = os.path.join(p_path.picture_path, 'login')
    sleep(2)
    if basepage.exists(os.path.join(module_picture_path, '勾选.png')):
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
    basepage.touch(os.path.join(module_picture_path, '登录.png'))
