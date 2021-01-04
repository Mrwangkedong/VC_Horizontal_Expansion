#!/usr/bin/env python
#-*-coding:utf-8 -*-
_author_ = 'Administrator'
import numpy as np
from PIL import Image
# from VC_Horizontal_Expansion.Part_tool import tools
from Part_tool import tools
import os
import time


# 图像拆分
def vcs_split_photo(image):
    list = []
    wide, high = image.size
    for i in range(t.N):
        list.append(t.create_array())  # 存储图片操作对象
    for i in range(high):  # 行数
        for j in range(wide):  # 列数
            B0 = t.GetB0()  # 加密
            B1 = t.GetB1()
            if image.getpixel((j, i)) > 128:
                B = B0
            else:
                B = B1
            for n in range(t.N):  # 共享份份数
                a=[]
                for m in range(len(B)):
                    if B[n][m] == 1:
                        a.append(0)
                    else:
                        a.append(255)
                list[n].extend(a)
    for n in range(t.N):
        list[n] = np.array(list[n]).reshape((high, -1))
        img = Image.fromarray(np.array(list[n])).convert("L")
        t.d_img_save(img, curr_dir + os.sep + "out" + os.sep + "V" + str(n) + '.png')

# 恢复
def vcs_recover_photo():
    a=[]
    list= []
    list_names = t.ret_all_filenames(curr_dir + os.sep + "im" + os.sep)
    for k in range(len(list_names)):
        image_li = Image.open(list_names[k])
        list.append(np.array(image_li))
    list= np.array(list)
    for i in range(len(list[0])):
        b=[]
        for j in range(len(list[0][0])):
            sum=1
            for k in range(len(list)):
                sum=sum*list[k][i][j]
            b.append(sum)
        a.append(b)
    a=np.array(a)
    image=Image.fromarray(a).convert("L")
    t.d_img_save(image, curr_dir + os.sep + "photo" + os.sep + "final.png")



#start=time.clock()
t=tools(2,3,"I.png", "I1.png")
curr_dir = os.path.dirname(os.path.realpath(__file__))
I=Image.open(t.im_path)
wide,high=I.size
H=t.Binary(I,high,wide)
t.d_img_save(H,t.out_path)
vcs_split_photo(H)
# vcs_recover_photo()