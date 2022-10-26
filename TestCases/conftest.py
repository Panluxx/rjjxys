# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 9:25
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : conftest.py
# Software  : PyCharm


from airtest.core.api import *
from airtest.core.device import *
from pywinauto.application import Application
import pytest
from Common.logger import logger
from Common.config import p_path
import os
from time import sleep
from Setting.constant import client_dir


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
    module_picture_path = os.path.join(p_path.picture_path, 'login')
    sleep(2)
    touch(Template(os.path.join(module_picture_path, '登录.png'), record_pos=(-0.259, 0.092),
                   resolution=(1920, 1080)))
