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

################################暂时没什么用####################
gamelist = []

def main():
    ###########遍历所有窗口的句柄##########################################
    win32gui.EnumWindows(com.get_all_hwnd, 0)
    ###########遍历所有的游戏窗口并放入数组#################################
    for hwnd, wdname in com.hwnd_title.items():
       if com.gametitle in wdname:
          # 第三个参数是任务次数，是四个参数是战斗状态0 未接任务  1 接了任务自动寻路 2 完成
          gamelist.append([hwnd,wdname,0,0])
    l=len(gamelist)
    if l ==0 :
       print("游戏尚未打开")
       sys.exit()
    else:
       print("游戏打开的个数为：",l)
    ####################################################################
    ###################################################################
    ##########正式开始护送，多开多怎么写呢？################################
    for i in range(l) :
       hwnd  =gamelist[i][0]
       wdname=gamelist[i][1]
       wdname=wdname[wdname.rfind("]")+1:]
       gamelist[i][2]=i+1
       #激活窗口
       com.set_foreground(hwnd)
       print(f"目前执行的窗口句柄是：'{hwnd}',窗口名称是：'{wdname}'")
       ##################################################################
       x1, y1,x2,y2 = com.get_window_info(hwnd)  # 获取窗口位置
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       #print(f"窗口位置：'{x1}, {y1}'")
       ##################################################################
       com.csh(hwnd, wdname) #初始化
       sleep(0.1+random.random())
       print("寻找护送npc金瓶儿")
       #find_husong()
       npc="jpe"
       com.find_npc(hwnd,npc)
       # ##################################################################
       # imgname = com.get_window_pos(hwnd, "querynpc")  #寻找npc
       # com.photo_compare(imgname,'./game_photo/husong/zi.jpg',hwnd)
       # #zi是护送金瓶儿几个字
       # sleep(0.3 + random.random())
       # # pyautogui.click(clicks=2)#双击
       # pyautogui.doubleClick()# 上面的双击也可以用
       # sleep(1+random.random())
       # win32api.keybd_event(27, 0, 0, 0)  # esc关闭npc查询窗口
       # sleep(0.1)
       # win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
       ##############一路小跑到金瓶儿那#####################################
       a=1
       #这个循环完全是未了调试方便
       while a<1000 :
          a += 1
          sleep(0.2+random.random())
          pyautogui.keyDown('esc')
          pyautogui.keyUp('esc')
          sleep(0.1 + random.random())
          pyautogui.hotkey('alt', 'f')  ##调出好友菜单
          sleep(0.1 + random.random())
          imgname = com.get_window_pos(hwnd, "zwlb1")
          res = com.photo_compare(imgname, './game_photo/husong/zwlb.jpg', hwnd)
          pyautogui.leftClick()
          ###############
          imgname = com.get_window_pos(hwnd, "npclist")
          res = com.photo_compare(imgname, './game_photo/husong/npclist_jpe.jpg', hwnd)
          if res < 0.5:
             com.photo_compare(imgname, './game_photo/husong/zwnpc.jpg', hwnd)
             sleep(0.1 + random.random())
             pyautogui.leftClick()
          sleep(0.1 + random.random())
          imgname = com.get_window_pos(hwnd, "npclist")
          res = com.photo_compare(imgname, './game_photo/husong/npclist_jpe.jpg', hwnd)
          if res > 0.8:
             pyautogui.rightClick()
             sleep(1)
             break
          else:
             pyautogui.keyDown('esc')
             pyautogui.keyUp('esc')
             sleep(12+ random.random())


       ##########################这里还要判断下菜单是收起来的还是没收起来################################
          # sval=com.photo_compare(imgname, './game_photo/husong/shou.jpg', hwnd)#收缩的
          # zval = com.photo_compare(imgname, './game_photo/husong/zhankai.jpg', hwnd)#展开的
          #if sval>zval:#如果是收缩的先要展开
       # sleep(0.5 + random.random())
       # imgname = com.get_window_pos(hwnd, "npclist")
       # sleep(0.3 + random.random())
       # res=com.photo_compare(imgname, './game_photo/husong/npclist_jpe.jpg', hwnd)
       # if res>0.6 :
       #    pyautogui.rightClick()
       #    sleep(1)




       #########等下我改

       ###################################################################
       #获取护送任务
       #com.photo_compare('./game_photo/husong/big.jpg', './game_photo/husong/small2.jpg', hwnd)
       #pyautogui.moveRel(0, -80, duration=0.5) ##不好定位，所以鼠标向上移动80距离要准一些--定位到金瓶儿
       #sleep(0.3 + random.random())
       #pyautogui.leftClick() #左键
       #sleep(0.3 + random.random())
       #######################################################
       # com.photo_compare(imgname, './game_photo/husong/zztp.jpg', hwnd)  # 先点击追踪图片
       # pyautogui.leftClick()  # 左键
       sleep(0.3 + random.random())
       imgname = com.get_window_pos(hwnd, "rwlb")  ##任务列表
       com.photo_compare(imgname, './game_photo/husong/caidan.jpg', hwnd)#识别任务菜单图标
       sleep(0.3 + random.random())
       pyautogui.leftClick()  # 左键
       sleep(0.3 + random.random())
       ########################################################
       imgname=com.get_window_pos(hwnd,"husong")#这个图片不固定大小，所以必须截图
       com.photo_compare(imgname, './game_photo/husong/querens.jpg', hwnd)  # 任务确认
       sleep(0.3 + random.random())
       pyautogui.leftClick()  # 左键
       sleep(0.3 + random.random())
       #####################点击任务链接开始奔跑#########################

       imgname = com.get_window_pos(hwnd, "rwlj")  ##任务链接
       com.photo_compare(imgname, './game_photo/husong/zztp.jpg', hwnd)  # 先点击追踪图片
       sleep(0.3 + random.random())
       pyautogui.leftClick()  # 左键
       sleep(0.3 + random.random())
       com.photo_compare(imgname, './game_photo/husong/dddd.jpg', hwnd)  # 识别任务菜单图标
       sleep(0.3 + random.random())
       pyautogui.moveRel(-70, 0, duration=0.1)  # 每个任务名称不一样，只能往右移动
       print("开始自动寻路")
       pyautogui.leftClick()  # 左键
       sleep(0.3 + random.random())
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       sleep(0.1+random.random())
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       ####################勉强判断下门派把#################################
       menpai=com.check_menpai(wdname)
       ####################循环判断是不是在战斗#################################
       a=1
       while a<=9999999:
          a += 1
          res=com.isfighting(hwnd)
          if res ==2 : ##如果是我方回合
             print("开始战斗，我方回合")
             res = com.isjpebb(hwnd)
             if res ==1:  ##如果是金瓶儿的bb
                pyautogui.hotkey('alt', 'g')  #捕捉bb
                sleep(0.3 + random.random())
                pyautogui.leftClick()  # 左键
                pyautogui.hotkey('alt', 'd')  #bb防御
             else:     #打怪
                if menpai in ("gw","yq","sl","qy","ty","fx","hh","sw","cy","ly","ft"): #如果是鬼王，其他的还不知道怎么写
                  pyautogui.hotkey('alt', 'a')  #人物打怪
                  sleep(0.3 + random.random())
                  pyautogui.hotkey('alt', 'q')  # bb打怪

          sleep(2+random.random())

          res = com.isend(hwnd)
          if res ==1 :
             print("任务完成")
             pyautogui.keyDown('esc')
             pyautogui.keyUp('esc')
             imgname = com.get_window_pos(hwnd, "isend2")  ##任务链接
             max_val = com.photo_compare(imgname, './game_photo/husong/end.png', hwnd)  # 识别任务菜单图标
             sleep(0.3 + random.random())
             print("点击问号成功",max_val)
             pyautogui.moveRel(0, 40, duration=0.2)
             sleep(0.3 + random.random())
             pyautogui.leftClick()
             sleep(0.9 + random.random())
             imgname = com.get_window_pos(hwnd, "rw_end")  ##结束任务
             com.photo_compare(imgname, './game_photo/husong/jsrw.jpg', hwnd)  # 识别任务菜单图标
             sleep(0.3 + random.random())
             pyautogui.leftClick()
             sleep(0.3 + random.random())
             ###################################
             imgname = com.get_window_pos(hwnd, "aq")  ##结束任务
             com.photo_compare(imgname, './game_photo/husong/anquan.jpg', hwnd)  # 识别任务菜单图标
             sleep(0.3 + random.random())
             pyautogui.leftClick()
             sleep(0.3 + random.random())
             ###################################
             imgname = com.get_window_pos(hwnd, "shouqian")  ##结束任务
             com.photo_compare(imgname, './game_photo/husong/sq.jpg', hwnd)  # 识别任务菜单图标
             sleep(0.3 + random.random())
             pyautogui.leftClick()
             sleep(0.3 + random.random())
             break





if __name__ == "__main__":

   main()