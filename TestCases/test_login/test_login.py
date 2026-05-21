# -*- coding:utf-8 -*-
# @Time     :  9:43
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_login.py
# Software  : PyCharm


from airtest.core.api import *
from Common.basepage import BasePage
from Common.Pages.login_page import LoginPage, get_path
import pytest


@pytest.mark.usefixtures('open_client')
class TestLogin(BasePage):
    @pytest.mark.login
    def test_login(self, open_client):
        """完整登录流程：启动 → 用户协议 → 隐私协议 → 登录 → 关闭"""
        login_page = LoginPage()
        
        # 1. 启动客户端 (open_client fixture 已完成)
        sleep(3)
        
        # 2. 打开用户协议
        self.touch(get_path('用户协议'), img_doc='打开用户协议', threshold=0.9)
        sleep(2)
        self.assert_exists(filepath=get_path('用户协议地址'), img_doc='查看用户协议地址', threshold=0.85)
        
        # 3. 关闭协议弹窗
        self.touch(get_path('X关闭'), img_doc='关闭用户协议弹窗', threshold=0.9)
        sleep(1)
        
        # 4. 调起客户端
        login_page.click_client()
        sleep(2)
        
        # 5. 打开隐私协议
        self.touch(get_path('隐私政策'), img_doc='打开隐私政策', threshold=0.9)
        sleep(2)
        self.assert_exists(filepath=get_path('隐私政策地址'), img_doc='查看隐私政策地址', threshold=0.85)
        
        # 6. 关闭协议弹窗
        self.touch(get_path('X关闭'), img_doc='关闭隐私政策弹窗', threshold=0.9)
        sleep(1)
        
        # 7. 调起客户端
        login_page.click_client()
        sleep(2)
        
        # 8. 登录进去
        login_page.do_login()
        sleep(2)
        
        # 9. 验证登录成功
        login_page.assert_login_success()
        
        # 10. 关掉客户端
        login_page.close_window()
