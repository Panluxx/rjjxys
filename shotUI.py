import win32api, win32con, win32gui
from PIL import Image, ImageGrab
from Common.config import p_path
import os


def get_window_pos(name):
    name = name
    handle = win32gui.FindWindow(0, name)

    # 获取窗口句柄
    if handle == 0:
        return None
    else:
        return win32gui.GetWindowRect(handle), handle


def jietu(name, png):
    (x1, y1, x2, y2), handle = get_window_pos(name)
    win32gui.SendMessage(handle, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
    # 发送还原最小化窗口的信息
    win32gui.SetForegroundWindow(handle)
    # 设为高亮
    img_ready = ImageGrab.grab((x1, y1, x2, y2))
    # 截图
    img_ready.show()
    img_ready.save(png)


img_path = os.path.join(p_path.picture_path, 'login')

img_name = img_path + r"\人教教学易.png"
print(img_name)
jietu('人教教学易', img_name)
