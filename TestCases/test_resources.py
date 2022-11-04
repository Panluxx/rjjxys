# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:54
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_resources.py
# Software  : PyCharm
import time

from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from time import sleep
from Setting.constant import resource_name, book_code, resources_save_dir
import webbrowser
from Setting.constant import dir
from pywinauto.mouse import move
from pywinauto.keyboard import SendKeys


def get_path(image):
    resources_path = os.path.join(p_path.picture_path, 'resources')
    return os.path.join(resources_path, f'{image}.png')


@pytest.fixture(scope='module')
def del_resources(login):
    BasePage().touch(get_path('我的资源'))
    yield
    sleep(2)
    webbrowser.open(os.path.realpath(dir()))
    if BasePage().exists(get_path('存放资源的文件'), img_doc='存在资源'):
        BasePage().touch(get_path('存放资源的文件'), img_doc='删除文件')
        SendKeys('{DELETE}')
    BasePage().touch(get_path('清除后关闭'), img_doc='关闭窗口')


@pytest.mark.usefixtures('del_resources')
class TestResources(BasePage):
    @pytest.mark.parametrize("test_data", resource_name)
    def test_import_resources(self, del_resources, test_data):
        self.touch(get_path('导入'), img_doc='点击导入按钮')
        if self.exists(get_path('路径存在')):
            pass
        else:
            self.touch(get_path('下拉框'), img_doc='点击下拉框')
            self.touch(get_path('路径'), img_doc='点击路径输入框')
            # 文件路径
            self.text(p_path.resources_path, img_doc=f'输入文件路径')
            SendKeys('{ENTER}')
        self.touch(get_path('输入文件名'), img_doc='点击输入文件名')
        self.text(test_data['name'], img_doc=f'输入文件名{test_data["name"]}')
        self.touch(get_path('打开'), img_doc='点击打开')
        sleep(3)
        if test_data['name'] == '音频.mp3':
            self.assert_exists(get_path('音频'), img_doc='查看音频封面')
            self.touch(get_path('音频'), img_doc='打开资源')
            self.assert_exists(get_path('音频资源'), img_doc='查看打开的资源')
            self.touch(get_path('资源关闭'), img_doc='关闭音频')
        elif test_data['name'] == '视频.mp4':
            self.assert_exists(get_path('视频'), img_doc='查看视频封面')
            self.touch(get_path('视频'), img_doc='打开视频')
            self.assert_exists(get_path('视频资源'), img_doc='查看打开的资源')
            self.touch(get_path('资源关闭'), img_doc='关闭视频')
        elif test_data['name'] == '图片.jpg':
            self.assert_exists(get_path('图片'), img_doc='查看图片封面')
            self.touch(get_path('图片'), img_doc='打开图片')
            self.assert_exists(get_path('图片资源'), img_doc='查看打开的资源')
            self.touch(get_path('资源关闭'), img_doc='关闭图片')
        elif test_data['name'] == '动画.swf':
            self.assert_exists(get_path('动画'), img_doc='查看动画封面')
            self.touch(get_path('动画'), img_doc='打开动画')
            self.assert_exists(get_path('动画资源'), img_doc='查看打开的资源')
            self.touch(get_path('资源关闭'), img_doc='关闭动画')
        elif test_data['name'] == '文件.xlsx':
            self.assert_exists(get_path('文件'), img_doc='查看文件封面')
            self.touch(get_path('文件'), img_doc='打开文件')
            self.assert_exists(get_path('文件资源'), img_doc='查看打开的资源')
            sleep(2)
            self.touch(get_path('文件关闭'), img_doc='关闭文件')
            if self.exists(get_path('保存弹窗')):
                self.touch(get_path('不保存'), img_doc='不保存文件')
        elif test_data['name'] == '文档.docx':
            self.assert_exists(get_path('文档'), img_doc='查看文档封面')
            self.touch(get_path('文档'), img_doc='打开文档')
            sleep(2)
            self.assert_exists(get_path('文档资源'), record_pos=(0.378, 0.007), img_doc='查看打开的资源')
            self.touch(get_path('文件关闭'), img_doc='关闭文档')
        else:
            self.assert_exists(get_path('课件'), img_doc='查看课件封面')
            self.touch(get_path('课件'), img_doc='打开课件')
            sleep(2)
            self.assert_exists(get_path('课件资源'), img_doc='查看打开的资源')
            self.touch(get_path('课件关闭'), img_doc='关闭课件')

    def test_edit_resources(self, del_resources):
        name = self.exists(get_path('课件'))
        if name:
            move(name)
            self.touch(get_path('编辑'), img_doc='编辑课件')
            self.assert_exists(get_path('课件资源'), img_doc='查看打开的资源')
            self.touch(get_path('课件关闭'), img_doc='关闭课件')

    def test_rename(self, del_resources):
        name = self.exists(get_path('课件'))
        if name:
            move(name)
            self.touch(get_path('重命名'), img_doc='重命名课件')
            self.text('编辑课件', img_doc='输入文件名')
            SendKeys('{ENTER}')
            self.assert_exists(get_path('编辑课件'), img_doc='查看编辑后的课件名')

    def test_del(self, del_resources):
        if self.exists(get_path('删除')):
            self.touch(get_path('删除'), img_doc='删除课件')
        else:
            name = self.exists(get_path('课件'))
            if name:
                move(name)
                self.touch(get_path('删除'), img_doc='删除课件')
        self.touch(get_path('确定删除'), img_doc='确定删除')

    def test_export_resources(self, del_resources):
        self.touch(get_path('导出'), img_doc='点击导出')
        self.touch(get_path('更改目录'), img_doc='点击更改目录')
        self.touch(get_path('下拉框'), img_doc='点击下拉框')
        self.touch(get_path('路径'), img_doc='点击路径')
        # 存放位置
        self.text(resources_save_dir, img_doc='输入文件路径')
        SendKeys('{ENTER}')
        self.touch(get_path('保存'), img_doc='点击保存')
        self.touch(get_path('勾选资源'), img_doc='点击全选资源')
        self.touch(get_path('确定'), img_doc='点击确定按钮')
        self.assert_exists(get_path('导出提示'), img_doc='检查导出提示')

    def test_create_folder(self, del_resources):
        if self.exists(get_path('导出提示')):
            sleep(60)
        self.touch(get_path('新建文件夹'), img_doc='点击新建文件夹')
        self.text('test', img_doc='输入文件名test')
        SendKeys('{ENTER}')
        self.assert_exists(get_path('文件夹名称'), img_doc='检查文件夹名称')

    def test_download(self, del_resources):
        self.touch(get_path('打开列表'), img_doc='打开列表')
        self.assert_exists(get_path('下载列表'), img_doc='检查是否打开列表')
        self.touch(get_path('关闭'), img_doc='点击关闭')

    def test_add(self, del_resources):
        self.touch(get_path('添加课本'), img_doc='点击添加')
        self.touch(get_path('输入激活码'), img_doc='点击输入框')
        self.text(book_code, img_doc=f'输入激活码{book_code}')
        self.touch(get_path('激活'), img_doc='点击激活')
