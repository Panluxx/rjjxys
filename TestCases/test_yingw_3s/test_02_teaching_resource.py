# -*- coding:utf-8 -*-
# @Time     : 2025/3/7 15:21
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : test_02_teaching_resource.py
# Software  : PyCharm


from airtest.core.api import *
from Common.config import p_path
import os
import pytest
from Common.basepage import BasePage
from pywinauto.mouse import move


def get_path(image):
    module_path = os.path.join(p_path.picture_path, r'yingw_3s\teaching_resource')
    return os.path.join(module_path, f'{image}.png')


pytest.mark.usefixtures('login')


class TestTeachingResource(BasePage):
    def test_case_01(self, login):
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('展开章节'), img_doc='点击展开章节')
        self.assert_exists(get_path('展开目录布局'), img_doc='检查目录布局')
        self.touch(get_path('切换目录2'), img_doc='点击切换目录2')
        self.assert_exists(get_path('切换目录后的选项'), img_doc='检查切换目录的选项')
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_02(self, login):
        # 教学设计
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('教学设计'), img_doc='点击教学设计')
        self.touch(get_path('设计资源'), img_doc='点击设计资源')
        self.assert_exists(get_path('设计资源内容'), img_doc='检查设计资源内容')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        # 编辑
        name = self.exists(get_path('设计资源'))
        move(name)
        self.touch(get_path('编辑'), img_doc='点击编辑')
        self.touch(get_path('输入'), img_doc='点击输入')
        self.text('123', img_doc='输入123')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        self.touch(get_path('保存'), img_doc='点击保存')
        sleep(2)
        # 下载
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('设计资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表设计资源'), img_doc='点击列表设计资源')
        self.assert_exists(get_path('列表设计资源内容'), img_doc='检查列表设计资源内容')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        # 编辑
        name = self.exists(get_path('列表设计资源'))
        move(name)
        self.touch(get_path('编辑'), img_doc='点击编辑')
        self.touch(get_path('输入'), img_doc='点击输入')
        self.text('123', img_doc='输入123')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        self.touch(get_path('保存'), img_doc='点击保存')
        sleep(2)
        # 下载
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表设计资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_03(self, login):
        # 教学课件
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('教学课件'), img_doc='点击教学课件')
        self.touch(get_path('课件资源'), img_doc='点击课件资源')
        sleep(5)
        self.assert_exists(get_path('课件资源内容'), img_doc='检查课件资源内容')
        self.touch(get_path('退出预览'), img_doc='点击退出预览')
        # 编辑
        name = self.exists(get_path('课件资源'))
        move(name)
        self.touch(get_path('编辑'), img_doc='点击编辑')
        self.touch(get_path('编辑-图片'), img_doc='点击图片tab')
        self.touch(get_path('添加'), img_doc='点击添加按钮')
        self.touch(get_path('编辑-动画'), img_doc='点击动画tab')
        self.touch(get_path('添加'), img_doc='点击添加按钮')
        self.touch(get_path('PPT放映'), img_doc='点击PPT放映按钮')
        sleep(2)
        self.assert_exists(get_path('放映内容'), img_doc='检查课件放映内容')
        self.click_key('{ESC}')
        self.touch(get_path('课件关闭'), img_doc='点击课件关闭')
        self.touch(get_path('保存'), img_doc='点击保存')
        sleep(10)
        # 下载
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('课件资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表课件资源'), img_doc='点击列表课件资源')
        sleep(5)
        self.assert_exists(get_path('列表课件资源内容'), img_doc='检查列表课件资源内容')
        self.touch(get_path('退出预览'), img_doc='点击退出预览')
        # 编辑
        name = self.exists(get_path('列表课件资源'))
        move(name)
        self.touch(get_path('编辑'), img_doc='点击编辑')
        self.touch(get_path('编辑-动画'), img_doc='点击动画tab')
        self.touch(get_path('添加'), img_doc='点击添加按钮')
        sleep(1)
        self.double_click(get_path('PPT放映'), img_doc='点击PPT放映按钮')
        sleep(2)
        self.assert_exists(get_path('列表资源放映内容'), img_doc='检查课件放映内容')
        self.click_key('{ESC}')
        self.touch(get_path('课件关闭'), img_doc='点击课件关闭')
        self.touch(get_path('保存'), img_doc='点击保存')
        sleep(2)
        # 下载
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表课件资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_04(self, login):
        # 同步练习
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('同步练习'), img_doc='点击同步练习')
        self.touch(get_path('练习资源'), img_doc='点击练习资源')
        self.assert_exists(get_path('练习资源内容'), img_doc='检查练习资源内容')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        # 编辑
        name = self.exists(get_path('练习资源'))
        move(name)
        self.touch(get_path('编辑'), img_doc='点击编辑')
        self.touch(get_path('练习输入'), img_doc='点击练习输入')
        self.text('123', img_doc='输入123')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        self.touch(get_path('保存'), img_doc='点击保存')
        sleep(2)
        # 下载
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('练习资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表练习资源'), img_doc='点击列表练习资源')
        self.assert_exists(get_path('列表练习资源内容'), img_doc='检查列表练习资源内容')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        # 编辑
        name = self.exists(get_path('列表练习资源'))
        move(name)
        self.touch(get_path('编辑'), img_doc='点击编辑')
        self.touch(get_path('练习输入'), img_doc='点击练习输入')
        self.text('123', img_doc='输入123')
        self.touch(get_path('设计关闭'), img_doc='点击设计关闭')
        self.touch(get_path('保存'), img_doc='点击保存')
        sleep(2)
        # 下载
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表练习资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_05(self, login):
        # 开篇页视频
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('开篇页视频'), img_doc='点击开篇页视频')
        self.touch(get_path('视频资源'), img_doc='点击视频资源')
        self.assert_exists(get_path('视频资源内容'), img_doc='检查视频资源内容')
        sleep(5)
        self.click_key('{ESC}')
        self.touch(get_path('暂停'), img_doc='点击视频暂停')
        self.touch(get_path('播放'), img_doc='点击视频播放')
        self.touch(get_path('关闭字幕'), img_doc='点击关闭字幕')
        self.touch(get_path('倍速'), img_doc='点击倍速按钮')
        self.touch(get_path('2.0x倍速'), img_doc='点击2.0x倍速')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量')
        self.touch(get_path('打开字幕'), img_doc='点击打开字幕')
        self.touch(get_path('开启音量'), img_doc='点击开启音量')
        self.touch(get_path('全屏'), img_doc='点击全屏按钮')
        self.click_key('{ESC}')
        self.touch(get_path('视频关闭'), img_doc='点击视频关闭按钮')
        # 下载
        name = self.exists(get_path('视频资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('视频资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表视频资源'), img_doc='点击列表视频资源')
        self.assert_exists(get_path('视频资源内容'), img_doc='检查视频资源内容')
        sleep(5)
        self.click_key('{ESC}')
        self.touch(get_path('暂停'), img_doc='点击视频暂停')
        self.touch(get_path('播放'), img_doc='点击视频播放')
        self.touch(get_path('关闭字幕'), img_doc='点击关闭字幕')
        self.touch(get_path('倍速'), img_doc='点击倍速按钮')
        self.touch(get_path('2.0x倍速'), img_doc='点击2.0x倍速')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量')
        self.touch(get_path('打开字幕'), img_doc='点击打开字幕')
        self.touch(get_path('开启音量'), img_doc='点击开启音量')
        self.touch(get_path('全屏'), img_doc='点击全屏按钮')
        self.click_key('{ESC}')
        self.touch(get_path('视频关闭'), img_doc='点击视频关闭按钮')

        # 下载
        name = self.exists(get_path('列表视频资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表视频资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_06(self, login):
        # TPR活动
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('TPR活动'), img_doc='点击TPR活动')
        self.touch(get_path('活动资源'), img_doc='点击活动资源')
        self.assert_exists(get_path('活动资源内容'), img_doc='检查活动资源内容')
        sleep(5)
        self.click_key('{ESC}')
        self.touch(get_path('暂停'), img_doc='点击视频暂停')
        self.touch(get_path('播放'), img_doc='点击视频播放')
        self.touch(get_path('关闭字幕'), img_doc='点击关闭字幕')
        self.touch(get_path('倍速'), img_doc='点击倍速按钮')
        self.touch(get_path('2.0x倍速'), img_doc='点击2.0x倍速')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量')
        self.touch(get_path('打开字幕'), img_doc='点击打开字幕')
        self.touch(get_path('开启音量'), img_doc='点击开启音量')
        self.touch(get_path('全屏'), img_doc='点击全屏按钮')
        self.click_key('{ESC}')
        self.touch(get_path('视频关闭'), img_doc='点击视频关闭按钮')
        # 下载
        name = self.exists(get_path('活动资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('活动资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表活动资源'), img_doc='点击列表活动资源')
        self.assert_exists(get_path('活动资源内容'), img_doc='检查活动资源内容')
        sleep(5)
        self.click_key('{ESC}')
        self.touch(get_path('暂停'), img_doc='点击视频暂停')
        self.touch(get_path('播放'), img_doc='点击视频播放')
        self.touch(get_path('关闭字幕'), img_doc='点击关闭字幕')
        self.touch(get_path('倍速'), img_doc='点击倍速按钮')
        self.touch(get_path('2.0x倍速'), img_doc='点击2.0x倍速')
        self.touch(get_path('关闭音量'), img_doc='点击关闭音量')
        self.touch(get_path('打开字幕'), img_doc='点击打开字幕')
        self.touch(get_path('开启音量'), img_doc='点击开启音量')
        self.touch(get_path('全屏'), img_doc='点击全屏按钮')
        self.click_key('{ESC}')
        self.touch(get_path('视频关闭'), img_doc='点击视频关闭按钮')
        # 下载
        name = self.exists(get_path('列表活动资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表活动资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_07(self, login):
        # 动画
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('动画'), img_doc='点击动画')
        self.touch(get_path('动画资源'), img_doc='点击动画资源')
        self.assert_exists(get_path('动画资源内容'), img_doc='检查动画资源内容')
        sleep(5)
        self.click_key('{ESC}')
        # 下载
        name = self.exists(get_path('动画资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('动画资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表动画资源'), img_doc='点击列表动画资源')
        self.assert_exists(get_path('列表动画资源内容'), img_doc='检查动画资源内容')
        sleep(5)
        self.click_key('{ESC}')
        # 下载
        name = self.exists(get_path('列表动画资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表动画资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')

    def test_case_08(self, login):
        # 图片
        self.touch(get_path('学科筛选框'), img_doc='点击学科筛选框')
        self.touch(get_path('英语'), img_doc='选择英语学科')
        self.touch(get_path('书本封面'), img_doc='点击书本封面')
        self.touch(get_path('教学资源'), img_doc='点击教学资源')
        self.touch(get_path('切换目录1'), img_doc='点击切换目录1')
        self.touch(get_path('图片'), img_doc='点击图片')
        self.touch(get_path('图片资源'), img_doc='点击图片资源')
        self.assert_exists(get_path('图片资源内容'), img_doc='检查图片资源内容')
        sleep(5)
        self.touch(get_path('关闭图片'), img_doc='点击关闭图片')
        # 下载
        name = self.exists(get_path('图片资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('图片资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 切换列表模式
        self.touch(get_path('列表模式'), img_doc='切换列表模式')
        self.touch(get_path('列表图片资源'), img_doc='点击列表图片资源')
        self.assert_exists(get_path('列表图片资源内容'), img_doc='检查图片资源内容')
        sleep(5)
        self.touch(get_path('关闭图片'), img_doc='点击关闭图片')
        # 下载
        name = self.exists(get_path('列表图片资源'))
        move(name)
        self.touch(get_path('下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('覆盖提示'), img_doc='覆盖提示存在'):
            self.touch(get_path('覆盖确定'), img_doc='点击确定按钮')
        # 收藏
        move(name)
        self.touch(get_path('收藏'), img_doc='点击收藏按钮')
        self.touch(get_path('取消收藏'), img_doc='点击取消收藏按钮')

        # 批量下载--- 单个
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('列表图片资源下载'), img_doc='选择资源下载')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 批量下载--- 全选
        self.touch(get_path('批量下载'), img_doc='点击批量下载')
        self.touch(get_path('全选'), img_doc='选择全选按钮')
        self.touch(get_path('批量确认下载'), img_doc='点击下载')
        self.touch(get_path('下载确定'), img_doc='点击确定按钮')
        if self.exists(get_path('全选覆盖提示'), img_doc='全选覆盖提示存在'):
            self.touch(get_path('全选覆盖确定'), img_doc='点击确定按钮')

        # 恢复
        self.touch(get_path('卡片模式'), img_doc='切换卡片模式')