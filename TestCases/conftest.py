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
from Common.Pages.login_page import LoginPage


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


@pytest.fixture(scope='function')
def login(open_client):
    """登录 fixture，使用 LoginPage 执行登录"""
    login_page = LoginPage()
    login_page.do_login()

