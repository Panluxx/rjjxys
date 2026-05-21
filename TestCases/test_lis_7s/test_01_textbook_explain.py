# -*- coding:utf-8 -*-
# @Time     : 2023/5/30 11:22
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_01_textbook_explain.py
# Software  : PyCharm


from airtest.core.api import *
import pytest
from Common.basepage import BasePage
from Common.utils import get_image_path
from pywinauto.mouse import move


# 模块图片目录
MODULE_DIR = 'lis_7s/textbook_explain'


def get_path(image):
    """获取当前模块的图片路径（兼容旧代码）"""
    return get_image_path(MODULE_DIR, image)


@pytest.mark.usefixtures('login')
class TestTextbookExplain(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('历史'), img_doc='选择历史学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.assert_exists(get_path('模块布局'))
        self.touch(get_path('专题讲座'), img_doc='点击专题讲座')
        self.assert_exists(get_path('专题讲座布局'))
        sleep(5)
        self.touch(get_path('暂停'), img_doc='点击暂停')
        self.assert_exists(get_path('暂停布局'))
        self.touch(get_path('播放'), img_doc='点击播放')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量')
        self.touch(get_path('倍速'), img_doc='点击倍速')
        self.touch(get_path('2.0倍速'), img_doc='点击2.0倍速')
        self.assert_exists(get_path('检查2.0倍速'))
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('确定'), img_doc='点击确定')
        # 验证下载
        self.touch(get_path('下载'), img_doc='点击下载')
        self.assert_exists(get_path('下载中'))
        self.touch(get_path('恢复音量'), img_doc='点击恢复音量')
        # 检查拖动 - 先定位滑块位置，再相对拖动
        slider_pos = self.exists(get_path('进度滑块'), img_doc='进度滑块', threshold=0.85)
        if slider_pos:
            # 从滑块当前位置向右拖动 200 像素
            self.swipe(slider_pos, (slider_pos[0] + 200, slider_pos[1]), img_doc='拖动进度')
        else:
            # 如果找不到滑块，使用相对坐标（在视频播放器区域内）
            # 假设进度条在 y=950 附近
            self.swipe((450, 950), (650, 950), img_doc='拖动进度')
        sleep(2)
        self.assert_exists(get_path('拖动后检查'))
        self.touch(get_path('全屏'), img_doc='点击全屏')
        sleep(5)
        # 移动到工具栏位置
        move(coords=(1890, 990))
        self.touch(get_path('退出全屏'), img_doc='点击退出全屏')
        self.touch(get_path('返回'), img_doc='点击返回')
        sleep(2)
        self.touch(get_path('专题讲座'), img_doc='点击专题讲座')
        self.touch(get_path('切换资源'), img_doc='点击切换资源')
        sleep(2)
        self.assert_exists(get_path('切换后界面'))
        self.touch(get_path('退出模块'), img_doc='点击退出模块')
