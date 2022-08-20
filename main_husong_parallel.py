import win32gui,win32api, win32con, re, traceback
from time import sleep
import pyperclip,pyautogui
import cv2
#from cv2 import *
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import cv2_tools
import random
import sys
import common as com
import os
import time

#################

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
    ####################################################################
    ###################################################################
    ##########初始化：也就是回到师门################################
    for i in range(l) :
       hwnd  =gamelist[i][0]
       wdname=gamelist[i][1]
       wdname=wdname[wdname.rfind("]")+1:]
       #gamelist[i][2]=i+1
       #激活窗口
       com.set_foreground(hwnd)
       print(f"当前句柄是：'{hwnd}',窗口名称是：'{wdname}'，初始化开始")
       ##################################################################
       x1,y1,x2,y2 = com.get_window_info(hwnd)  # 获取窗口位置
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       #print(f"窗口位置：'{x1}, {y1}'")
       ##################################################################
       com.csh(hwnd, wdname) #初始化
    sleep(abs(6-l + random.random()))

    for i in range(l):
       hwnd = gamelist[i][0]
       wdname = gamelist[i][1]
       wdname = wdname[wdname.rfind("]") + 1:]
     #  gamelist[i][2] = i + 1
       # 激活窗口
       com.set_foreground(hwnd)
       print(f"寻找jpe的窗口名称是：'{wdname}'")
       com.csh2(hwnd, wdname)  ####初始化2
       ##################################################################
       x1, y1, x2, y2 = com.get_window_info(hwnd)  # 获取窗口位置
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       sleep(random.uniform(0.2, 0.5))
       print("寻找护送npc金瓶儿")
       #find_husong()
       npc="jpe"
       com.find_npc(hwnd,npc)
       sleep(random.uniform(0.1,0.5))
    ####跑到jpe面前要11s
    sleep(abs(13-l + random.random()))

    ############如果有jpebb就交任务
    #bb=1
    for i in range(l):

       hwnd   = gamelist[i][0]
       wdname = gamelist[i][1]
       wdname = wdname[wdname.rfind("]") + 1:]
       # 激活窗口
       com.set_foreground(hwnd)
       print(f"交jpebb的窗口名称是：'{wdname}'")
       ##################################################################
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       sleep(random.random())
       bb = com.havejpebb(hwnd)
       while bb > 0:
          #bb = com.havejpebb(hwnd)
          #if bb == 1:
          sleep(random.uniform(0.1, 0.5))
          com.givejpebb(hwnd)
          sleep(random.uniform(0.1,0.5))
          pyautogui.keyDown('esc')
          pyautogui.keyUp('esc')
          bb = com.havejpebb(hwnd)


    ########循环接任务###############
    for i in range(l):
       hwnd  =gamelist[i][0]
       wdname=gamelist[i][1]
       wdname=wdname[wdname.rfind("]")+1:]
     #  gamelist[i][2]=i+1
       #激活窗口
       com.set_foreground(hwnd)
       print(f"当前句柄是：'{hwnd}',win名称是：'{wdname}'")
       ##################################################################
       x1, y1,x2,y2 = com.get_window_info(hwnd)  # 获取窗口位置
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')

       sleep(random.uniform(0.1,0.5))
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')
       sleep(random.uniform(0.1,0.5))
       pyautogui.hotkey('alt', 'f')  ##调出好友菜单
       sleep(random.uniform(0.1,0.5))
       imgname = com.get_window_pos(hwnd, "zwlb1")
       com.photo_compare(imgname, './game_photo/husong/zwlb.jpg', hwnd)
       sleep(random.uniform(0.1,0.5))
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
          sleep(0.1 + random.random())
    #      break
       else:
          pyautogui.keyDown('esc')
          pyautogui.keyUp('esc')
          sleep(12+ random.random())

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
    ############################################################################################
    ############################################################################################
       ############################################################################################
      ####把没用的窗口关上
    for i in range(l):
       hwnd  =gamelist[i][0]
       #激活窗口
       com.set_foreground(hwnd)
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')

       sleep(0.1)
       pyautogui.keyDown('esc')
       pyautogui.keyUp('esc')

    #############指挥战斗
    sleep(0.1)
    a=0
    while a<l :
       try:
          for i in range(l):

             hwnd = gamelist[i][0]
             wdname = gamelist[i][1]
             wdname = wdname[wdname.rfind("]") + 1:]
            # gamelist[i][2] = i + 1
             # 激活窗口
             com.set_foreground(hwnd)
             print(f"护送中,角色名称是：'{wdname}'")
             ##################################################################
             sleep(random.uniform(0.1, 0.5))
             ####################勉强判断下门派把#################################
             menpai=com.check_menpai(wdname)
             ####################循环判断是不是在战斗#################################
             #sleep(1.5 + random.random())
             res=com.isfighting(hwnd)
             if res ==2 : ##如果是我方回合

                print("开始战斗，我方回合")
                res =com.isjsgz(hwnd)
                if res == 1:  ##如果有僵尸鬼冢bb
                   pyautogui.hotkey('alt', 'd')  # 防御
                   sleep(random.uniform(0.1, 0.3))
                   #pyautogui.leftClick()  # 左键
                   pyautogui.hotkey('alt', 'd')  # bb防御

                res = com.isjpebb(hwnd)
                if res ==1:  ##如果是金瓶儿的bb
                   pyautogui.hotkey('alt', 'g')  #捕捉bb
                   sleep(random.uniform(0.2, 0.5))
                   pyautogui.leftClick()  # 左键
                   pyautogui.hotkey('alt', 'd')  #bb防御
                else:     #打怪
                   if menpai in ("gw","yq","sl","qy","ty","fx","hh","sw","cy","ly","ft"): #如果是鬼王，其他的还不知道怎么写
                     pyautogui.hotkey('alt', 'a')  #人物打怪
                     sleep(0.1)
                     pyautogui.hotkey('alt', 'q')  # bb打怪
                sleep(random.random())
                continue
             elif res ==0 : ##如果不是战:
               # sleep(0.1+random.random())
                sleep(random.uniform(0.2, 0.6))

                res1 = com.isend(hwnd)

                if res1 ==1 :

                   print("任务完成")
                #   sleep(random.uniform(0.1, 0.5))
                   pyautogui.keyDown('esc')
                   pyautogui.keyUp('esc')
                   sleep(random.uniform(0.1, 0.5))
                   imgname = com.get_window_pos(hwnd, "isend2")  ##任务链接
                   max_val = 0
                   # while max_val<0.70:
                   #    max_val = com.photo_compare(imgname, './game_photo/husong/end.png', hwnd)  # 识别任务菜单图标
                   #    print("问号的比对率为：", round(max_val,4))
                   max_val = com.photo_compare(imgname, './game_photo/husong/end2.png', hwnd)
                   if max_val<0.7 :####为什么问号的识别率这么低
                      print("问号的识别率低：", round(max_val, 4))
                      sleep(random.uniform(0.1, 0.5))
                      continue
                   sleep(random.uniform(0.3, 0.8))
                   pyautogui.moveRel(0, 40, duration=0.1)
                   sleep(random.uniform(0.3, 0.5))
                   pyautogui.leftClick()
                   print("点击问号成功", round(max_val,4))
                   sleep(random.uniform(0.6, 0.9))
                   imgname = com.get_window_pos(hwnd, "rw_end")  ##结束任务
                   max_val=com.photo_compare(imgname, './game_photo/husong/jsrw2.png', hwnd)  # 识别任务菜单图标
                   if max_val<0.8 :
                      print("点护送JPE的识别率低：", round(max_val, 4))
                      sleep(random.uniform(0.2, 0.5))
                      pyautogui.keyDown('esc')
                      pyautogui.keyUp('esc')
                      continue
                   print("点护送JPE的识别率：", round(max_val, 4))
                   sleep(random.uniform(0.2,0.7))
                   pyautogui.leftClick()
                   sleep(random.uniform(0.3,0.8))
                   ###################################
                   imgname = com.get_window_pos(hwnd, "aq")  ##结束任务
                   res=com.photo_compare(imgname, './game_photo/husong/anquan.png', hwnd)  # 识别任务菜单图标
                   if res >=0.7 :
                      sleep(random.uniform(0.1,0.5))
                      pyautogui.leftClick()
                   else:
                      com.photo_compare(imgname, './game_photo/husong/anquan2.png', hwnd)  # 识别任务菜单图标
                      sleep(random.uniform(0.1,0.5))
                      pyautogui.leftClick()
                      sleep(random.uniform(0.1,0.5))
                   ###################################
                   imgname = com.get_window_pos(hwnd, "shouqian")  ##结束任务
                   res=com.photo_compare(imgname, './game_photo/husong/sq2.png', hwnd)  # 识别任务菜单图标
                   if res >= 0.7:
                      sleep(random.uniform(0.1, 0.5))
                      pyautogui.leftClick()
                   else:
                      print("点击不客气识别率低：", round(max_val, 4))
                      sleep(random.uniform(0.2, 0.5))
                      pyautogui.keyDown('esc')
                      pyautogui.keyUp('esc')
                      continue
                   sleep(random.uniform(0.1,0.5))
                   # pyautogui.leftClick()
                   # sleep(random.uniform(0.1,0.5))
                   a += 1

                   del gamelist[i]
                   print(a,"个角色完成单次任务")

                else:
                   pass
                   #break
       except IndexError:
          continue
          sleep(random.uniform(0.1,0.6))
       sleep(random.uniform(0.1,0.6))
    sleep(random.uniform(0.1,0.6))




if __name__ == "__main__":

      t=0  #护送是30次
      while t <30 :
          main()
          t+=1
