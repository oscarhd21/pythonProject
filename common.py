import win32gui,win32api, win32con, re, traceback
from time import sleep
import pyperclip
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import cv2_tools
import random
import os
################test
################test
################test
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
    ##先查看根目录下是否有temp目录，没有就创建一个
    if os.path.isdir("./game_photo/temp/"):
       pass
    else:
       os.mkdir("./game_photo/temp/")
    #############################################
    imgname= "./game_photo/temp/"+imgname+".png"
    try:
       os.remove(imgname)
    except:
        pass
    x1,y1,x2,y2 = get_window_info(hwnd)
    img = pyautogui.screenshot(imgname,region=(x1,y1,x2-x1,y2-y1))
    sleep(random.uniform(0.1, 0.4))
    return imgname


def photo_compare(p_big,p_small,hwnd,ismove=0):#图像识别，并定位并移动到图片内的坐标 ismove 0 移动鼠标，1不移动

    original = cv2.imread(p_big)
    img = cv2.imread(p_big, 0)
    template = cv2.imread(p_small, 0)
    h, w = template.shape[:2]

    methods = ['cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCOEFF', 'cv2.TM_SQDIFF_NORMED', 'cv2.TM_SQDIFF',
               'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED']
    ret = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(ret)
    ###max_loc是矩阵的左上点（x，y）坐标  ，而（x+w，y+h）是矩阵的右下点坐标
    ###########这句话可以画图，在大图中用矩形圈出小图，留着测试用
    # res = cv2.rectangle(original, max_loc, (max_loc[0] + w, max_loc[1] + h), (0, 255, 255), 2)
    # cv2.imshow('res', res)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    ##########################################################
    ######确定小图中心点的位置
    x1,y1,x2,y2=get_window_info(hwnd)
    x = int(max_loc[0] + w / 2)+x1
    y = int(max_loc[1] + h / 2)+y1
   # print(x, y)
   # print(max_val, max_loc)    啊
    if ismove ==0 :
        if round(max_val,2)>=0.7 :
            pyautogui.moveTo(x,y, duration=0.1)
            res=1
            print("比对成功",p_small,round(max_val,4), max_loc)
        else:
            res=0
            print("比对失败",p_small,round(max_val,4), max_loc)
    else:
        pass
    return max_val

def set_foreground(self):
        """put the window in the foreground"""
        #将窗口激活并前置#

        if self > 0:
            win32gui.SendMessage(self, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
            win32gui.SetForegroundWindow(self)
        return 1

def find_npc(hwnd,npc):  # 寻找护送坐标 alt+n是快捷键
    #pyautogui.hotkey('esc')
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    sleep(random.uniform(0.1,0.5))  # 随机函数
    pyautogui.hotkey('alt', 'n')  # 寻找护送坐标 alt+n是快捷键
    #sleep(random.uniform(0.1,0.5))  # 随机函数
    if npc=="jpe" :
        # 输入”护送“两个字，点击查询
        pyperclip.copy('护送')  # 先复制
    elif npc=="zuoqi" :
        # 输入”zuoqi“两个字，点击查询
        pyperclip.copy('兽神')  # 先复制
    elif npc=="gwcs" :
        # 点击查询
        pyperclip.copy('鬼王宗传')  # 先复制
    elif npc=="yqcs" :
        # 点击查询
        pyperclip.copy('门派传送人')  # 先复制
    elif npc=="slcs" :
        # 点击查询
        pyperclip.copy('传送弟子')  # 先复制
    elif npc=="ftcs" :
        # 点击查询
        pyperclip.copy('梵天宫传')  # 先复制
    elif npc == "hhcs":
        # 点击查询
        pyperclip.copy('合欢派传')  # 先复制
    elif npc == "cycs":
        # 点击查询
        pyperclip.copy('苍羽阁传')  # 先复制
    elif npc == "lycs":
        # 点击查询
        pyperclip.copy('灵音殿传')  # 先复制
    elif npc == "qycs":
        # 点击查询
        pyperclip.copy('青云门传')  # 先复制

    else:
        pass

    sleep(random.uniform(0.1,0.3))
    pyautogui.hotkey('ctrl', 'v')  # 再粘贴
    sleep(random.uniform(0.1,0.3))
    win32api.keybd_event(13, 0, 0, 0)  # enter
    win32api.keybd_event(13, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    image_npc = "./game_photo/find_npc/" + npc + ".png"
    sleep(random.uniform(0.1,0.5))
    imgname = get_window_pos(hwnd, "querynpc")  # 寻找npc
    photo_compare(imgname, image_npc, hwnd)
    sleep(random.uniform(0.1,0.5))
    pyautogui.doubleClick()
    sleep(random.uniform(0.1,0.5))
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    # win32api.keybd_event(27, 0, 0, 0)  # esc关闭npc查询窗口
    # sleep(0.1)
    # win32api.keybd_event(27, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键


def isfighting(hwnd):
    #判断是否在战斗 1战斗非我方回合  0非战斗 2 战斗我方回合
    imgname = get_window_pos(hwnd, "fighting")  ##任务链接
    # max_val=photo_compare(imgname, './game_photo/huihe.jpg', hwnd)  #是否在战斗
    # if max_val >0.9:
    #     max_val = photo_compare(imgname, './game_photo/zdzl.jpg', hwnd)
    #     if max_val>0.9:
    #         return 2         #我方回合
    #     else:
    #         return 1         #敌方回合
    # else:
    #     return 0
    max_val = photo_compare(imgname, './game_photo/zdzl.jpg', hwnd,1)  # 是否在战斗
    if max_val > 0.9:
        return 2  #我方回合
    else:
        max_val = photo_compare(imgname, './game_photo/huihe.jpg', hwnd,1)
        if max_val > 0.9:
            return 1  # 战斗中非我方回合
        else:
            return 0  # 非战斗


def isjpebb(hwnd):
     # 判断是否有金瓶儿bb 1有  0没有
     imgname = get_window_pos(hwnd, "isjpebb")  ##任务链接
     max_val = photo_compare(imgname, './game_photo/husong/jpebb.jpg', hwnd)  # 识别任务菜单图标
     if max_val > 0.9:
         return 1
     else:
         return 0


def isjsgz(hwnd):
    # 判断是否有僵尸鬼冢bb 1有  0没有
    imgname = get_window_pos(hwnd, "isjsgz")  ##任务链接
    max_val = photo_compare(imgname, './game_photo/husong/jsgz.png', hwnd)  # 识别任务菜单图标
    if max_val >= 0.8:
        return 1
    else:
        return 0


def isbb(hwnd):
    # 判断是否有bb 1有  0没有
    imgname = get_window_pos(hwnd, "isbb")  ##任务链接
    max_val = photo_compare(imgname, './game_photo/husong/bb.jpg', hwnd)  # 识别任务菜单图标
    if max_val > 0.9:
        return 1
    else:
        return 0

def check_menpai(wdname):
    # 判断是哪个门派
    gw = "鬼王宗"
    yq = "意气盟"
    sl = "森罗殿"
    qy = "青云门"
    ty = "天音寺"
    fx = "焚香谷"
    hh = "合欢派"
    sw = "圣巫教"
    cy = "苍羽阁"
    ly = "灵音殿"
    ft = "梵天宫"
    if gw in wdname:
        menpai = "gw"
    elif yq in wdname:
        menpai = "yq"
    elif sl in wdname:
        menpai = "sl"
    elif qy in wdname:
        menpai = "qy"
    elif ty in wdname:
        menpai = "ty"
    elif fx in wdname:
        menpai = "fx"
    elif hh in wdname:
        menpai = "hh"
    elif sw in wdname:
        menpai = "sw"
    elif cy in wdname:
        menpai = "cy"
    elif ly in wdname:
        menpai = "ly"
    elif ft in wdname:
        menpai = "ft"
    return menpai

def isend(hwnd) :
    #判断任务是否结束 1 结束 0 未结束 只针对护送
    sleep(0.5 + random.random())
    imgname = get_window_pos(hwnd, "isend")  ##任务链接
    max_val=photo_compare(imgname, './game_photo/husong/mdd.jpg', hwnd,1)  # 识别任务菜单图标

    if max_val >= 0.8:
        return 1
    else:
        max_val = photo_compare(imgname, './game_photo/husong/end.jpg', hwnd, 1)  # 再识别一次问号
        if max_val >= 0.7:
            return 1
        else:
            return 0

def npclist(hwnd,npc):
    pyautogui.hotkey('alt', 'f')  ##调出好友菜单
    sleep(random.uniform(0.2, 0.5))
    imgname = get_window_pos(hwnd, "zwlb1")
    res = photo_compare(imgname, './game_photo/npclist/zwlb.png', hwnd)
    sleep(random.uniform(0.2, 0.5))
    pyautogui.leftClick()
    ###############
    imgname = get_window_pos(hwnd, "npclist")
    image_npc="./game_photo/npclist/"+npc+".png"
    res = photo_compare(imgname, image_npc, hwnd)
    if res < 0.6:
        photo_compare(imgname, './game_photo/npclist/zwnpc.png', hwnd)##周围npc
        sleep(random.uniform(0.1,0.5))
        pyautogui.leftClick()
    sleep(random.random())
    imgname = get_window_pos(hwnd, "npclist")
    res = photo_compare(imgname,image_npc , hwnd)
    if res > 0.8:
        pyautogui.rightClick()
        sleep(random.uniform(0.1,0.5))
    else:
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
     #   sleep(12 + random.random())

def csh(hwnd,wdname) : #初始化1，也就是找到门派传送弟子
    ###########add 2021-5-22 把任务跟踪先去掉
    imgname = get_window_pos(hwnd, "rwgz")  ##结束任务
    res=photo_compare(imgname, './game_photo/rwgz.png', hwnd)  # 识别任务菜单图标
    if res >=0.7 :
       pyautogui.hotkey('alt', 'j')
    sleep(random.uniform(0.1,0.5))
    pyautogui.hotkey('f1')
    sleep(random.uniform(0.1,0.5))
    menpai=check_menpai(wdname)
    npc= menpai + "cs"
    find_npc(hwnd, npc)
#    sleep(5 + random.random())

def csh2(hwnd,wdname) :   #初始化2，也就是通过门派传送弟子回城
    menpai = check_menpai(wdname)
    npc = menpai + "cs"
    npclist(hwnd, npc)

    imgname = get_window_pos(hwnd, "hc_big")
    res = photo_compare(imgname, './game_photo/hc2.png', hwnd) ###回城
    while res<0.7 :
        print("点击回城识别率低：", round(res, 4))
        imgname = get_window_pos(hwnd, "hc_big1")
        res = photo_compare(imgname, './game_photo/hc2.png', hwnd)  ###回城
        sleep(random.uniform(0.1, 0.5))
    print("回城按钮比对率：",res)
    sleep(random.uniform(0.2,0.5))
    pyautogui.leftClick()
    sleep(random.uniform(0.1,0.5))

def havejpebb(hwnd): ##判断是否有jpebb
    sleep(0.1 + random.random())
    ##打开宠物页面
    pyautogui.hotkey('alt', 'p')
    sleep(random.uniform(0.1,0.6))
    imgname = get_window_pos(hwnd, "jpebb")
    res = photo_compare(imgname, './game_photo/husong/jpebb2.png', hwnd,1)
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')
    if res >=0.8 : #如果有jpebb
       return 1
    else:
       return 0


def givejpebb(hwnd):  ##交出jpebb
    sleep(0.1 + random.random())

    pyautogui.hotkey('alt', 'f')  ##调出好友菜单
    sleep(0.1 + random.random())
    imgname = get_window_pos(hwnd, "zwlb1")
    photo_compare(imgname, './game_photo/husong/zwlb.jpg', hwnd)
    sleep(0.1 + random.random())
    pyautogui.leftClick()
    ###############
    imgname = get_window_pos(hwnd, "npclist")
    res = photo_compare(imgname, './game_photo/husong/npclist_jpe.jpg', hwnd)
    if res < 0.5:
        photo_compare(imgname, './game_photo/husong/zwnpc.jpg', hwnd)
        sleep(0.1 + random.random())
        pyautogui.leftClick()
    sleep(0.1 + random.random())
    imgname = get_window_pos(hwnd, "npclist")
    res = photo_compare(imgname, './game_photo/husong/npclist_jpe.jpg', hwnd)

    if res > 0.8:
        pyautogui.rightClick()
        sleep(0.1 + random.random())
    #      break
    else:
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        #sleep(12 + random.random())

    sleep(0.1 + random.random())
    imgname = get_window_pos(hwnd, "rwlb")  ##任务列表
    photo_compare(imgname, './game_photo/husong/caidan2.png', hwnd)  # 识别"金瓶儿的宠物"
    sleep(0.1 + random.random())
    pyautogui.leftClick()  # 左键
    sleep(0.1 + random.random())
    ########################################################
    imgname = get_window_pos(hwnd, "givejpebb1")
    photo_compare(imgname, './game_photo/husong/qrjpebb.png', hwnd)  #“好，这就给你”
    sleep(0.1 + random.random())
    pyautogui.leftClick()  # 左键
    sleep(0.1 + random.random())


    imgname = get_window_pos(hwnd, "givejpebb2")  ##
    photo_compare(imgname, './game_photo/husong/bkq.png', hwnd)  # 先点击不客气
    sleep(0.1 + random.random())
    pyautogui.leftClick()  # 左键
    sleep(0.1 + random.random())

    imgname = get_window_pos(hwnd, "givejpebb3")  ##任务链接
    photo_compare(imgname, './game_photo/husong/jycw.png', hwnd)  # 给予宠物
    sleep(0.1 + random.random())
    pyautogui.leftClick()  # 左键
    sleep(0.1 + random.random())

    imgname = get_window_pos(hwnd, "givejpebb4")
    photo_compare(imgname, './game_photo/husong/jpebb3.png', hwnd)  # ‘选择jpebb’
    sleep(0.1 + random.random())
    pyautogui.leftClick()  # 左键
    sleep(0.1 + random.random())
    photo_compare(imgname, './game_photo/husong/jy.png', hwnd)  # 点击“给予”
    sleep(0.1 + random.random())
    pyautogui.leftClick()  # 左键
    sleep(0.1 + random.random())
