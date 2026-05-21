# -*- coding:utf-8 -*-
# @Time     : 2025/5/20
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : utils.py
# Software  : PyCharm

import os
from Common.config import p_path


def get_image_path(module_dir, image_name):
    """
    获取图片资源的完整路径

    Args:
        module_dir: 模块目录名，如 'login', 'lis_7s/textbook_explain'
        image_name: 图片文件名（不含扩展名）

    Returns:
        图片的完整路径

    Example:
        >>> get_image_path('login', '登录')
        'E:/.../Picture/login/登录.png'
        >>> get_image_path('lis_7s/textbook_explain', '学科筛选框')
        'E:/.../Picture/lis_7s/textbook_explain/学科筛选框.png'
    """
    # 统一使用反斜杠（Windows）
    module_dir = module_dir.replace('/', os.sep)
    module_path = os.path.join(p_path.picture_path, module_dir)
    return os.path.join(module_path, f'{image_name}.png')
