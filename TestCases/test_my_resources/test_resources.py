# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:54
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_resources.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from time import sleep
from Setting.constant import resource_name, resources_save_dir
from pywinauto.mouse import move
from pywinauto.keyboard import SendKeys


def get_path(image):
    resources_path = os.path.join(p_path.picture_path, r'my_resources\resources')
    return os.path.join(resources_path, f'{image}.png')


@pytest.mark.usefixtures('login')
class TestResources(BasePage):
    @pytest.mark.parametrize("test_data", resource_name)
    def test_import_resources(self, login, test_data):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        self.touch(get_path('导入'), img_doc='点击导入按钮')
        if self.exists(get_path('路径存在')):
            pass
        else:
            self.touch(get_path('下拉框'), img_doc='点击下拉框')
            # 文件路径
            self.text(p_path.resources_path, img_doc=f'输入文件路径')
            self.click_key('{ENTER}')
        sleep(1)
        self.touch(get_path('输入文件名'), img_doc='点击输入文件名')
        self.text(test_data['name'], img_doc=f'输入文件名{test_data["name"]}')
        self.click_key('{ENTER}')
        sleep(3)
        if test_data['name'] == '音频.mp3':
            self.touch(get_path('音频'), img_doc='打开资源')
            self.assert_exists(get_path('音频资源'), img_doc='查看打开的资源')
            self.touch(get_path('关闭音频'), img_doc='点击关闭音频')
        elif test_data['name'] == '视频.mp4':
            self.touch(get_path('视频'), img_doc='打开视频')
            self.assert_exists(get_path('视频资源'), img_doc='查看打开的资源')
            self.click_key('{ESC}')
            self.touch(get_path('关闭音频'), img_doc='关闭视频')
        elif test_data['name'] == '图片.jpg':
            self.touch(get_path('图片'),  img_doc='打开图片')
            self.assert_exists(get_path('图片资源'), img_doc='查看打开的资源')
            self.touch(get_path('关闭音频'), img_doc='关闭图片')
        elif test_data['name'] == '动画.swf':
            self.touch(get_path('动画'), img_doc='打开动画')
            self.assert_exists(get_path('动画资源'), img_doc='查看打开的资源')
            self.touch(get_path('关闭动画'), img_doc='关闭动画')
        elif test_data['name'] == '文件.xlsx':
            self.touch(get_path('文件'),  img_doc='打开文件')
            self.assert_exists(get_path('文件资源'), img_doc='查看打开的资源')
            sleep(2)
            self.touch(get_path('文件关闭'), img_doc='关闭文件')
            if self.exists(get_path('保存弹窗')):
                self.touch(get_path('不保存'), img_doc='不保存文件')
        elif test_data['name'] == '文档.docx':
            self.touch(get_path('文档'), img_doc='打开文档')
            sleep(2)
            self.assert_exists(get_path('文档资源'), img_doc='查看打开的资源')
            self.touch(get_path('文件关闭'), img_doc='关闭文档')
            name = self.exists(get_path('文档'))
            move(name)
            self.touch(get_path('删除'), img_doc='删除文档')
            sleep(1)
            self.touch(get_path('确定删除'), img_doc='确定删除')
        else:
            self.touch(get_path('课件'), img_doc='打开课件')
            sleep(10)
            self.assert_exists(get_path('课件资源'), img_doc='查看打开的资源')
            self.touch(get_path('课件关闭'), img_doc='关闭课件')

    def test_edit_resources(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        name1 = self.exists(get_path('课件'))
        move(name1)
        self.touch(get_path('编辑'), img_doc='编辑课件')
        self.assert_exists(get_path('课件资源'), img_doc='查看打开的资源')
        self.touch(get_path('课件关闭'), img_doc='关闭课件')

    def test_rename(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        name2 = self.exists(get_path('课件'))
        move(name2)
        self.touch(get_path('重命名'), img_doc='重命名课件')
        self.text('编辑课件', img_doc='输入文件名')
        self.click_key('{ENTER}')
        self.assert_exists(get_path('编辑课件'), img_doc='查看编辑后的课件名')

    def test_export_resources(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        self.touch(get_path('导出授课包'), img_doc='点击导出')
        self.touch(get_path('更改目录'), img_doc='点击更改目录')
        if self.exists(get_path('导出目录')):
            self.touch(get_path('保存'), img_doc='点击保存')
        else:
            self.touch(get_path('下拉框'), img_doc='点击下拉框')
            # 存放位置
            self.text(resources_save_dir, img_doc='输入文件路径')
            self.click_key('{ENTER}')
            self.touch(get_path('保存'), img_doc='点击保存')
        self.touch(get_path('勾选资源'), img_doc='点击全选资源')
        self.touch(get_path('确定'), img_doc='点击确定按钮')
        self.assert_exists(get_path('取消导出'), img_doc='检查导出窗口')

    def test_create_folder(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        self.touch(get_path('新建文件夹'), img_doc='点击新建文件夹')
        self.text('test', img_doc='输入文件名test')
        self.click_key('{ENTER}')
        self.assert_exists(get_path('文件夹名称'), img_doc='检查文件夹名称')

    def test_download(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        self.touch(get_path('打开列表'), img_doc='打开列表')
        self.assert_exists(get_path('下载列表'), img_doc='检查是否打开列表')
        self.touch(get_path('关闭'), img_doc='点击关闭')

    def test_search(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        self.touch(get_path('搜索'), img_doc='点击搜索按钮')
        self.touch(get_path('搜索框'), img_doc='点击搜索框')
        self.text('课件', img_doc='输入搜索名称')
        self.touch(get_path('确定搜索'), img_doc='点击确定搜索')
        self.assert_exists(get_path('搜索内容'), img_doc='检查搜索的内容')

    def test_del(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        name4 = self.exists(get_path('编辑课件'))
        move(name4)
        self.touch(get_path('删除'), img_doc='删除课件')
        sleep(1)
        self.touch(get_path('确定删除'), img_doc='确定删除')

    def test_batch_del(self, login):
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        if self.exists(get_path('批量操作'), img_doc='批量操作可点击'):
            self.touch(get_path('批量操作'), img_doc='点击批量操作')
            self.touch(get_path('全选'), img_doc='点击全选按钮')
            self.touch(get_path('批量删除'), img_doc='点击批量删除')
            self.touch(get_path('批量确定删除'), img_doc='点击批量确定删除按钮')

