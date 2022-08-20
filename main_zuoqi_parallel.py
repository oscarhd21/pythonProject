import win32gui,win32api, win32con, re, traceback
from time import sleep
import pyperclip,pyautogui
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import cv2_tools
import random
import sys
import common as com
import os
import time

def main():
    gamelist = []
    ###########遍历所有窗口的句柄##########################################
    win32gui.EnumWindows(com.get_all_hwnd, 0)
    ###########遍历所有的游戏窗口并放入数组#################################
    for hwnd, wdname in com.hwnd_title.items():
       if com.gametitle in wdname:
          gamelist.append([hwnd,wdname])
    l=len(gamelist)
    if l ==0 :
       print("游戏尚未打开")
       sys.exit()
    else:
       print("游戏打开的个数为：",l)
    ##########初始化：也就是回到师门################################
    for i in range(l):
        hwnd = gamelist[i][0]
        wdname = gamelist[i][1]
        wdname = wdname[wdname.rfind("]") + 1:]
        # gamelist[i][2]=i+1
        # 激活窗口
        com.set_foreground(hwnd)
        print(f"当前句柄是：'{hwnd}',窗口名称是：'{wdname}'，初始化开始")
        ##################################################################
        x1, y1, x2, y2 = com.get_window_info(hwnd)  # 获取窗口位置
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        # print(f"窗口位置：'{x1}, {y1}'")
        ##################################################################
        com.csh(hwnd, wdname)  # 初始化
    sleep(abs(6 - l + random.random()))

    for i in range(l):
        hwnd = gamelist[i][0]
        wdname = gamelist[i][1]
        wdname = wdname[wdname.rfind("]") + 1:]
        #  gamelist[i][2] = i + 1
        # 激活窗口
        com.set_foreground(hwnd)
        print(f"寻找兽神的窗口是：'{wdname}'")
        com.csh2(hwnd, wdname)  ####初始化2
        ##################################################################
        x1, y1, x2, y2 = com.get_window_info(hwnd)  # 获取窗口位置
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        sleep(random.uniform(0.2, 0.5))
        print("寻找兽神")
        # find_husong()
        npc = "zuoqi"
        com.find_npc(hwnd, npc)
        sleep(random.uniform(0.1, 0.5))
        ####跑到ss面前要多久

    sleep(abs(8 - l + random.random()))
    ########循环接任务###############
    for i in range(l):
       hwnd  =gamelist[i][0]
       wdname=gamelist[i][1]
       wdname=wdname[wdname.rfind("]")+1:]
     #  gamelist[i][2]=i+1
       #激活窗口
       com.set_foreground(hwnd)
       print(f"接任务的是：'{wdname}'")
       ##################################################################
       x1, y1,x2,y2 = com.get_window_info(hwnd)  # 获取窗口位置
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')

       sleep(random.uniform(0.1,0.3))
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       sleep(random.uniform(0.1,0.5))
       pyautogui.hotkey('alt', 'f')  ##调出好友菜单
       sleep(random.uniform(0.1,0.5))

       imgname = com.get_window_pos(hwnd, "npclist")
       res = com.photo_compare(imgname, './game_photo/npclist/ss.png', hwnd)
       if res <0.7:
           #########周围列表
           imgname = com.get_window_pos(hwnd, "zwlb")
           com.photo_compare(imgname, './game_photo/zwlb.jpg', hwnd)
           sleep(random.uniform(0.1,0.5))
           pyautogui.leftClick()
           ###############
           imgname = com.get_window_pos(hwnd, "npclist")
           res = com.photo_compare(imgname, './game_photo/npclist/ss.png', hwnd)
           if res < 0.7:
              com.photo_compare(imgname, './game_photo/zwnpc.jpg', hwnd)
              sleep(random.uniform(0.1, 0.5))
              pyautogui.leftClick()
           sleep(random.uniform(0.1,0.5))
           imgname = com.get_window_pos(hwnd, "npclist")
           res = com.photo_compare(imgname, './game_photo/npclist/ss.png', hwnd)
           ########这个if好像有问题
           if res >= 0.8:
              pyautogui.rightClick()
              sleep(random.uniform(0.1, 0.5))
           else:
              pyautogui.keyDown('esc')
              pyautogui.keyUp('esc')
              sleep(12+ random.random())
       else:
           pyautogui.rightClick()
           sleep(random.uniform(0.1, 0.5))
######################################################################################
       imgname = com.get_window_pos(hwnd, "rwlb")  ##任务列表
       res=com.photo_compare(imgname, './game_photo/husong/caidan.jpg', hwnd)#识别任务菜单图标
       while res <0.7:
          imgname = com.get_window_pos(hwnd, "rwlb")  ##
          res=com.photo_compare(imgname, './game_photo/husong/caidan.jpg', hwnd)  # 识别传送按钮
       sleep(random.uniform(0.1,0.5))
       pyautogui.leftClick()  # 左键
       sleep(random.uniform(0.2,0.6))
       ########################################################
       imgname=com.get_window_pos(hwnd,"husong")#这个图片不固定大小，所以必须截图
     #  com.photo_compare(imgname, './game_photo/husong/querens1.jpg', hwnd)  # 任务确认
       res=com.photo_compare(imgname, './game_photo/husong/caidan.jpg', hwnd)  # 任务确认
       while res <0.7:
          imgname = com.get_window_pos(hwnd, "husong")  ##
          res=com.photo_compare(imgname, './game_photo/husong/caidan.jpg', hwnd)  # 识别传送按钮

       sleep(random.uniform(0.1,0.5))
       pyautogui.leftClick()  # 左键
       sleep(random.uniform(0.5,1))
       #####################点击任务链接开始奔跑#########################

       imgname = com.get_window_pos(hwnd, "rwlj")  ##
       sleep(random.uniform(0.1, 0.3))
       res = com.photo_compare(imgname, './game_photo/husong/cs.png', hwnd)  # 识别任务菜单图标
       ####################优化：让接任务的速度高点
       if res<0.7:

          com.photo_compare(imgname, './game_photo/husong/zztp.jpg', hwnd)  # 先点击追踪图片
          sleep(random.uniform(0.1,0.5))
          pyautogui.leftClick()  # 左键
          sleep(random.uniform(0.1,0.3))
          res=com.photo_compare(imgname, './game_photo/husong/cs.png', hwnd)  # 识别任务菜单图标
          while res <0.7:
             imgname = com.get_window_pos(hwnd, "rwlj")  ##
             res=com.photo_compare(imgname, './game_photo/husong/cs.png', hwnd)  # 识别传送按钮
       ##################################
       sleep(random.uniform(0.1,0.5))
       pyautogui.moveRel(-70, 0, duration=0.1)  # 每个任务名称不一样，只能往左移动
       sleep(random.uniform(0.3, 0.7))
       pyautogui.leftClick()  # 左键
       sleep(random.uniform(0.1, 0.2))
       print("开始自动寻路")
       sleep(random.uniform(0.1,0.5))