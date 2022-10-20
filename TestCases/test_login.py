# -*- coding:utf-8 -*-
# @Time     :  9:43
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_login.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
from pywinauto.application import Application
import os

# 图片地址
login_picture_path = os.path.join(p_path.picture_path, 'login')

# 连接设备
auto_setup(__file__, devices=["Windows:///"])
# 启动设备
APP = Application().start(r"D:\testpackage\renjiaojiaoxueyi\main\EnTeach.exe")
sleep(2)
# 账号输入框
touch(Template(os.path.join(login_picture_path, '输入用户名.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))
text('18377560722')

sleep(2)
# 密码输入框
touch(Template(os.path.join(login_picture_path, '输入密码.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))
text('Test@321')

sleep(2)
# 记住密码
touch(Template(os.path.join(login_picture_path, '记住密码.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))

sleep(2)
# 勾选协议
touch(Template(os.path.join(login_picture_path, '勾选协议.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))

sleep(2)
# 登录
touch(Template(os.path.join(login_picture_path, '登录.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))
sleep(3)
try:
    assert_exists(Template(os.path.join(login_picture_path, '首页logo.png'), record_pos=(-0.259, 0.092),
                           resolution=(1920, 1080)), "首页登录成功后_存在logo")
    print('断言成功')
except Exception as e:
    print('断言失败')
    raise e
sleep(3)
touch(Template(os.path.join(login_picture_path, '关闭窗口.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))
sleep(3)
touch(Template(os.path.join(login_picture_path, '确定关闭.png'), record_pos=(-0.259, 0.092),
               resolution=(1920, 1080)))
