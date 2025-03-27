# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 15:09
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : constant.py
# Software  : PyCharm
import winreg


# 通过注册表查询安装文件路径
def dir():
    reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                         r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall\EnTeach")
    path = winreg.QueryValueEx(reg, 'InstallPath')
    return path[0]


def client_dir():
    path = dir()
    return path + "\\main\\EnTeach.exe"


# 文件存放路径
resources_save_dir = r'C:\Users\Administrator\Downloads'

# 账号/密码
username = '18269604642'
password = 'Test@321'

# 资源
resource_name = [{"name": "文档.docx"}, {"name": "课件.pptx"}, {"name": "音频.mp3"}, {"name": "视频.mp4"},
                 {"name": "文件.xlsx"}, {"name": "图片.jpg"},
                 {"name": "动画.swf"}]

# 激活码
book_code = 'A12345678'
