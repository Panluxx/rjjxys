# -*- coding:utf-8 -*-
# @Time     : 2025/5/20
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : login_page.py
# Software  : PyCharm

from airtest.core.api import *
from Common.basepage import BasePage
from Common.utils import get_image_path
from Common.logger import logger
from Setting.constant import username, password


# 登录模块图片目录
LOGIN_MODULE = 'login'


def get_path(image):
    """获取登录模块的图片路径"""
    return get_image_path(LOGIN_MODULE, image)


class LoginPage(BasePage):
    """登录页面对象"""

    def do_login(self):
        """执行登录流程：填写表单 → 登录 → 处理弹窗"""
        # 直接填写登录表单
        self._fill_login_form()

        # 执行登录操作
        self.touch(get_path('登录'), img_doc='点击登录', threshold=0.85)
        sleep(2)

        # 处理"以后再说"弹窗（降低阈值）
        if self.exists(get_path('以后再说'), img_doc='以后再说存在', threshold=0.5):
            sleep(3)
            self.touch(get_path('以后再说'), img_doc='点击以后再说', threshold=0.5)

    def _fill_login_form(self):
        """填写登录表单（用户名、密码、勾选协议）"""
        # 输入用户名
        name_pos = self.exists(get_path('账号'), img_doc='账号', threshold=0.85)
        if name_pos:
            # 点击账号输入框（偏移80像素）
            double_click((name_pos[0] + 80, name_pos[1]))
        else:
            self.touch(get_path('输入用户名'), img_doc='点击用户名输入框', threshold=0.85)
        sleep(2)
        self.text(username, img_doc=f'输入用户名{username}')

        # 输入密码
        if self.exists(get_path('清空密码'), img_doc='密码输入框', threshold=0.85):
            self.double_click(get_path('清空密码'), img_doc='双击密码输入框', threshold=0.85)
        else:
            self.touch(get_path('输入密码'), img_doc='点击密码输入框', threshold=0.85)
        sleep(2)
        self.text(password, img_doc=f'输入密码{password}')

        # 勾选记住密码（降低阈值，尝试匹配）
        if self.exists(get_path('未勾选'), img_doc='记住密码未勾选', threshold=0.6):
            self.touch(get_path('未勾选'), img_doc='勾选记住密码', threshold=0.6)
            sleep(1)

        # 勾选协议（降低阈值，尝试匹配）
        if self.exists(get_path('未勾选'), img_doc='用户协议未勾选', threshold=0.6):
            self.touch(get_path('未勾选'), img_doc='勾选并同意协议', threshold=0.6)
            sleep(1)

    def click_client(self):
        """点击调起客户端（防误点优化：提高阈值 + 相对位置定位）"""
        # threshold=0.9：提高匹配精度，避免匹配到系统UI
        # record_pos：使用截图时记录的相对位置，定位更精准
        # 注：如需设置 record_pos，请在截"调起客户端"图片时记录位置
        self.touch(get_path('调起客户端'), img_doc='调起客户端', threshold=0.9)

    def assert_login_success(self, timeout=10, interval=2):
        """
        断言登录成功（带等待重试机制）

        Args:
            timeout: 最大等待时间（秒）
            interval: 每次检查的间隔（秒）

        Returns:
            True 表示登录成功，False 表示超时
        """
        elapsed = 0
        while elapsed < timeout:
            pos = self.exists(get_path('书架页'), img_doc='检查书架页布局', threshold=0.85)
            if pos:
                logger.info(f'登录成功，检测到书架页')
                return True
            elapsed += interval
            sleep(interval)

        # 超时后截图并抛出详细错误
        self.save_page_screenshots('登录成功检查失败')
        raise AssertionError(f"登录超时：{timeout}秒内未检测到书架页")

    def close_window(self):
        """关闭窗口"""
        self.touch(get_path('关闭窗口'), img_doc='关闭窗口', threshold=0.85)
        self.touch(get_path('确定关闭'), record_pos=(-0.259, 0.092), img_doc='确定关闭', threshold=0.85)
