# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 15:09
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : constant.py
# Software  : PyCharm
import winreg


# 通过注册表查询安装文件路径
def client_dir():
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\EnTeach")
    path = winreg.QueryValueEx(reg, 'InstallPath')
    return path[0] + "\\main\\EnTeach.exe"


# 账号/密码
username = '18377560722'
password = 'Test@321'

# 资源
resource_name = [{"name": "音频.mp3"}, {"name": "视频.mp4"}, {"name": "图片.jpg"}, {"name": "动画.swf"},
                 {"name": "文件.xlsx"}, {"name": "文档.docx"}, {"name": "课件.pptx"}]

# 激活码
book_code = 'A12345678'
