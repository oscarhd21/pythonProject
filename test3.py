import win32gui,win32api, win32con, re, traceback
from time import sleep
import pyperclip,pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import cv2_tools
import random
import os

hwnd_title = dict()
gametitle = "梦幻诛仙"

def get_all_hwnd(hwnd, mouse): #获取所有窗口句柄
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#win32gui.EnumWindows(get_all_hwnd, 0)

def resolution():  # 获取屏幕分辨率
    return win32api.GetSystemMetrics(0), win32api.GetSystemMetrics(1)

def get_window_info(hwnd):  # 获取game窗口信息
    # return  win32gui.GetWindowRect(hwnd)
    x1=win32gui.GetWindowRect(hwnd)[0]
    y1=win32gui.GetWindowRect(hwnd)[1]
    x2 = win32gui.GetWindowRect(hwnd)[2]
    y2 = win32gui.GetWindowRect(hwnd)[3]
    return x1,y1,x2,y2
    #get_window_info()函数返回游戏窗口信息(x1, y1, x2, y2)，(x1, y1)是窗口左上角的坐标，(x2, y2)是窗口右下角的坐标

def get_window_pos(hwnd,imgname):  # 游戏窗口截图
    imgname= "./game_photo/temp/"+imgname+".png"
    try:
       os.remove(imgname)
    except:
        pass
    x1,y1,x2,y2 = get_window_info(hwnd)
    img = pyautogui.screenshot(imgname,region=(x1,y1,x2-x1,y2-y1))
    return imgname


def photo_compare(p_big,p_small):#图像识别，并定位并移动到图片内的坐标

    original = cv2.imread(p_big)
    img = cv2.imread(p_big, 0)
    template = cv2.imread(p_small, 0)
    h, w = template.shape[:2]

    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCOEFF', 'cv2.TM_SQDIFF_NORMED', 'cv2.TM_SQDIFF',
               'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED']
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # res = cv2.rectangle(original, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)
    # cv2.imshow('res', res)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    ###max_loc是矩阵的左上点（x，y）坐标  ，而（x+w，y+h）是矩阵的右下点坐标
    print (w,h)
    if res.any():
        return cv2.minMaxLoc(res)
    else:
        return -1

def set_foreground(self):
        """put the window in the foreground"""
        #将窗口激活并前置#

        if self > 0:
            win32gui.SendMessage(self, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
            win32gui.SetForegroundWindow(self)
        return 1

def find_npc(npc):  # 寻找护送坐标 alt+n是快捷键
    if npc=="husong" :
        pyautogui.hotkey('alt', 'n')  # 寻找护送坐标 alt+n是快捷键
        sleep(0.3 + random.random())  # 随机函数
        # 输入”护送“两个字，点击查询
        pyperclip.copy('护送')  # 先复制
        pyautogui.hotkey('ctrl', 'v')  # 再粘贴
        sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # enter
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    elif npc=="zuoqi" :
        pyautogui.hotkey('alt', 'n')  # 寻找护送坐标 alt+n是快捷键
        sleep(0.3 + random.random())  # 随机函数
        # 输入”zuoqi“两个字，点击查询
        pyperclip.copy('兽神')  # 先复制
        pyautogui.hotkey('ctrl', 'v')  # 再粘贴
        sleep(1)
        win32api.keybd_event(13, 0, 0, 0)  # enter
        win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    else:
        pass
    sleep(1)

def isfighting():
    #判断是否在战斗
    pass


def main():

    res=photo_compare('./game_photo/isend.png', './game_photo/husong/end.jpg')

    print(res)



if __name__ == "__main__":
    main()