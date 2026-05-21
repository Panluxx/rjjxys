# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:54
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_resources.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import pytest
from Common.basepage import BasePage
from Common.utils import get_image_path
from time import sleep
from Setting.constant import resource_name, resources_save_dir
from pywinauto.mouse import move
from pywinauto.keyboard import SendKeys


# 模块图片目录
MODULE_DIR = 'my_resources/resources'


def get_path(image):
    """获取当前模块的图片路径"""
    return get_image_path(MODULE_DIR, image)


# 资源类型配置：定义不同资源类型的操作
RESOURCE_CONFIG = {
    '音频.mp3': {
        'open_btn': '音频',
        'content': '音频资源',
        'close_btn': '关闭音频',
    },
    '视频.mp4': {
        'open_btn': '视频',
        'content': '视频资源',
        'close_btn': '关闭音频',  # 注：原代码使用关闭音频关闭视频
        'esc_key': True,
    },
    '图片.jpg': {
        'open_btn': '图片',
        'content': '图片资源',
        'close_btn': '关闭音频',
    },
    '动画.swf': {
        'open_btn': '动画',
        'content': '动画资源',
        'close_btn': '关闭动画',
    },
    '文件.xlsx': {
        'open_btn': '文件',
        'content': '文件资源',
        'close_btn': '文件关闭',
        'has_save_popup': True,
    },
    '文档.docx': {
        'open_btn': '文档',
        'content': '文档资源',
        'close_btn': '文件关闭',
        'has_delete': True,
        'delete_target': '文档',
    },
    '课件.pptx': {
        'open_btn': '课件',
        'content': '课件资源',
        'close_btn': '课件关闭',
        'open_wait': 10,
    },
}


def get_resource_config(name):
    """获取资源类型配置"""
    return RESOURCE_CONFIG.get(name, {
        'open_btn': name.split('.')[0],
        'content': f'{name.split(".")[0]}资源',
        'close_btn': '关闭',
    })


@pytest.mark.usefixtures('login')
class TestResources(BasePage):
    @pytest.mark.parametrize("test_data", resource_name)
    def test_import_resources(self, login, test_data):
        resource_name_val = test_data['name']
        config = get_resource_config(resource_name_val)

        # 切换到我的资源页面
        self.touch(get_path('我的资源'), img_doc='切换到我的资源页面')
        sleep(3)

        # 点击导入
        self.touch(get_path('导入'), img_doc='点击导入按钮')

        # 检查路径是否已存在
        if self.exists(get_path('路径存在')):
            pass
        else:
            self.touch(get_path('下拉框'), img_doc='点击下拉框')
            self.text(p_path.resources_path, img_doc=f'输入文件路径')
            self.click_key('{ENTER}')
        sleep(1)

        # 输入文件名
        self.touch(get_path('输入文件名'), img_doc='点击输入文件名')
        self.text(resource_name_val, img_doc=f'输入文件名{resource_name_val}')
        self.click_key('{ENTER}')
        sleep(3)

        # 根据配置打开资源
        self.touch(get_path(config['open_btn']), img_doc=f'打开{resource_name_val}')
        
        # 特殊等待时间（如课件需要等待10秒）
        if config.get('open_wait'):
            sleep(config['open_wait'])
        else:
            sleep(2)
            
        self.assert_exists(get_path(config['content']), img_doc='查看打开的资源')

        # ESC 键处理（如视频）
        if config.get('esc_key'):
            self.click_key('{ESC}')

        # 关闭资源
        self.touch(get_path(config['close_btn']), img_doc='关闭资源')

        # 保存弹窗处理（如文件）
        if config.get('has_save_popup') and self.exists(get_path('保存弹窗')):
            self.touch(get_path('不保存'), img_doc='不保存文件')

        # 删除处理（如文档）
        if config.get('has_delete'):
            target = config.get('delete_target', resource_name_val.split('.')[0])
            name = self.exists(get_path(target))
            if name:
                move(name)
                self.touch(get_path('删除'), img_doc='删除文档')
                sleep(1)
                self.touch(get_path('确定删除'), img_doc='确定删除')

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

