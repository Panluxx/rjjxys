# -*- coding:utf-8 -*-
# @Time     : 2022/10/21 10:22
# @Author   : Pan.
# @Email    : 619414118@qq.com
# File      : basepage.py
# Software  : PyCharm


from airtest.core.api import *
from Common.logger import logger
from Common.config import p_path
import allure
import win32gui
import win32ui
from ctypes import windll
from PIL import Image


class BasePage:

    def template(self, filepath, img_doc='', threshold=0.9, record_pos=None, resolution=(1920, 1080)):
        try:
            logger.info(f"{img_doc} : 查找：{filepath} 图片")
            path = Template(filepath, threshold=threshold, record_pos=record_pos, resolution=resolution)
            return path
        except Exception as e:
            logger.warn(f'找不到：{filepath}图片')
            self.save_page_screenshots(img_doc)
            raise e

    def exists(self, filepath, img_doc='', threshold=0.9, record_pos=None, resolution=(1920, 1080)):
        try:
            path = exists(self.template(filepath, threshold=threshold, record_pos=record_pos, resolution=resolution,
                                        img_doc=img_doc))
            # self.save_page_screenshots(img_doc)
            logger.info(f'{img_doc}页面：{filepath} 图片存在')
        except Exception as e:
            logger.warn(f'{filepath} 图片不存在')
            self.save_page_screenshots(img_doc)
            return False
        else:
            return path

    def touch(self, filepath, img_doc='', threshold=0.9, record_pos=None, resolution=(1920, 1080)):
        try:
            touch(self.template(filepath, threshold=threshold, record_pos=record_pos, resolution=resolution,
                                img_doc=img_doc))
            sleep(0.5)
            # self.save_page_screenshots(img_doc)
            logger.info(f"{img_doc}: 点击 {filepath} 图片")
        except Exception as e:
            logger.warn(f'{filepath} 图片无法点击')
            self.save_page_screenshots(img_doc)
            raise e

    def text(self, msg=None, img_doc=''):
        try:
            text(msg)
            # self.save_page_screenshots(img_doc)
            logger.info(f"输入文本 {msg}")
        except Exception as e:
            logger.error("输入文本失败：")
            self.save_page_screenshots(img_doc)
            raise e

    # def swipe(self, filepath, img_doc='', threshold=0.9, record_pos=None, resolution=(1920, 1080), vector=None):
    #     try:
    #         swipe(self.template(filepath, threshold=threshold, record_pos=record_pos, resolution=resolution,
    #                             img_doc=img_doc), vector=vector)
    #     except Exception as e:
    #         self.save_page_screenshots(img_doc)
    #         raise e
    def swipe(self, v1, v2, img_doc='', vector=None):
        try:
            swipe(v1, v2, vector=vector)
        except Exception as e:
            self.save_page_screenshots(img_doc)
            raise e

    def assert_exists(self, filepath, img_doc='', threshold=0.9, record_pos=None, resolution=(1920, 1080), msg=''):
        try:
            assert_exists(self.template(filepath, threshold=threshold, record_pos=record_pos, resolution=resolution,
                                        img_doc=img_doc),
                          msg=msg)
            # self.save_page_screenshots(img_doc)
            logger.info(f'对{img_doc}图片进行断言：结果为：True')
        except Exception as e:
            logger.error(f'对{img_doc}图片进行断言：结果为：False')
            self.save_page_screenshots(img_doc)
            raise e

    def double_click(self, filepath, img_doc='', threshold=0.9, record_pos=None, resolution=(1920, 1080)):
        try:
            double_click(self.template(filepath, threshold=threshold, record_pos=record_pos, resolution=resolution,
                                       img_doc=img_doc))
            logger.info(f'双击:{filepath} 图片')
        except Exception as e:
            logger.error('图片双击失败')
            self.save_page_screenshots(img_doc)
            raise e

    def click_key(self, keyname):
        try:
            keyevent(keyname)
            logger.info(f'使用快捷键{keyname}成功')
        except Exception as e:
            logger.error(f'使用快捷键{keyname}失败')
            raise e

    def save_page_screenshots(self, img_doc='', quality=None, max_size=None):
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        screenshots_path = p_path.screenshots_path + "/{}_{}.png".format(img_doc, now)
        try:
            snapshot(filename=screenshots_path, msg=img_doc, quality=quality, max_size=max_size)
        except Exception as e:
            logger.error("当前网页截图失败")
            raise e
        else:
            logger.info("截取当前网页成功并存储在: {}".format(screenshots_path))
            with open(screenshots_path, mode='rb') as f:
                file = f.read()
                allure.attach(file, img_doc, allure.attachment_type.PNG)

    # def save_page_screenshots(self, img_doc=''):
    #     # 获取窗口句柄，有弹框的情况下截不了
    #     hwnd = win32gui.FindWindow(None, "人教教学易")
    #
    #     # 获取窗口的位置和大小
    #     left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #
    #     # 计算窗口的宽度和高度
    #     width = right - left
    #     height = bottom - top
    #
    #     # 获取设备上下文DC（Device Context）
    #     hwndDC = win32gui.GetWindowDC(hwnd)
    #     mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    #     saveDC = mfcDC.CreateCompatibleDC()
    #
    #     # 创建位图对象
    #     saveBitMap = win32ui.CreateBitmap()
    #     saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    #
    #     # 将位图选入到设备上下文中
    #     saveDC.SelectObject(saveBitMap)
    #
    #     # 使用PrintWindow函数获取窗口截图
    #     windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    #
    #     # 将位图保存为PIL image对象
    #     bmpinfo = saveBitMap.GetInfo()
    #     bmpstr = saveBitMap.GetBitmapBits(True)
    #     im = Image.frombuffer(
    #         'RGB',
    #         (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    #         bmpstr, 'raw', 'BGRX', 0, 1
    #     )
    #
    #     # 释放资源
    #     saveDC.DeleteDC()
    #     mfcDC.DeleteDC()
    #     win32gui.ReleaseDC(hwnd, hwndDC)
    #     win32gui.DeleteObject(saveBitMap.GetHandle())
    #     now = time.strftime("%Y-%m-%d %H_%M_%S")
    #     screenshots_path = p_path.screenshots_path + "/{}_{}.png".format(img_doc, now)
    #     im.save(screenshots_path)
