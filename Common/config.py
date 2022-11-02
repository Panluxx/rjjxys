# -*- coding:utf-8 -*-
# @Time     :  16:28
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : config.py
# Software  : PyCharm

import os


class ProjectPath:
    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 图片
    picture_path = os.path.join(root_path, 'Picture')

    # log
    log_path = os.path.join(root_path, 'logs')

    # 资源
    resources_path = os.path.join(root_path, 'Resources')

    # 报告
    report_path = os.path.join(root_path, 'Report')

    # 截图
    screenshots_path = os.path.join(report_path, 'screenshots')


p_path = ProjectPath()
