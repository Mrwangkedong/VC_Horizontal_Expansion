#!/usr/bin/env python
#-*-coding:utf-8 -*-
_author_ = 'Administrator'
import numpy as np
import random
from PIL import Image

import matplotlib.pyplot as plt
import os
curr_dir = os.path.dirname(os.path.realpath(__file__))
class tools:
    #(k,n)门限，m表示一个共享份中元素个数，g表示其汉明重量，im_path表示其输入路径，out_path表示其输出路径
    def __init__(self,K,N,im_path_filename,out_path_filename):
        self.K = K
        self.N = N
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        self.im_path=curr_dir +os.sep+"photo"+ os.sep+im_path_filename
        self.out_path=curr_dir +os.sep+"photo"+ os.sep+out_path_filename


    # 矩阵M是否存在于集合Ms中
    def is_matrix_in_set(self,M, Ms):
        for each_matrix in Ms:
            if np.array_equal(M, each_matrix):
                return True
        return False

    def pi_matrix_shift_right(self,M):
        R = []  # 基础矩阵集合
        r = np.matrix(M)
        R.append(r)
        col_nums = np.size(r, 1)  # 列数
        for i in range(col_nums - 1):
            r_col = r[:, col_nums - 1]
            l_cols = r[:, 0:col_nums - 1]
            r = np.hstack((r_col, l_cols))
            if self.is_matrix_in_set(r, R):
                continue
            R.append(r)
        #print("R:", R)
        return R

    #(2,3)门限
    def GetB0(self):
        list_str = []
        list_temp= []
        file = curr_dir +os.sep+"B0B1"+ os.sep+"B0.txt"
        f = open(file, 'r')
        line = f.readlines()
        for fields in line:
            fields = fields.strip('\n')
            fields = fields.split('\t')
            list_str.append(fields)
        for i in range(0, len(list_str)):
            temp = []
            for j in range(0, len(list_str[0][0]), 4):
                temp.append(int(list_str[i][0][j:j + 1]))
            list_temp.append(temp)
        pi = self.pi_matrix_shift_right(list_temp)
        b0 = np.array(random.choice(pi))
        return b0



    def GetB1(self):
        list_str = []
        list_temp = []
        file = curr_dir + os.sep + "B0B1" + os.sep + "B0.txt"
        f = open(file, 'r')
        line = f.readlines()
        for fields in line:
            fields = fields.strip('\n')
            fields = fields.split('\t')
            list_str.append(fields)
        for i in range(0, len(list_str)):
            temp = []
            for j in range(0, len(list_str[0][0]), 4):
                temp.append(int(list_str[i][0][j:j + 1]))
            list_temp.append(list(temp))
        pi = self.pi_matrix_shift_right(list_temp)
        b1 = np.array(random.choice(pi))
        return b1



    #二值化
    def Binary(self,image, high, wide):
        for i in range(high):
            for j in range(wide):
                if image.getpixel((j, i)) > 128:
                    image.putpixel((j, i), 255)
                else:
                    image.putpixel((j, i), 0)
        return image

    def create_array(self):
        a = []
        return a

    # 保存目标图片到img_path
    def d_img_save(self,img,img_path):
        img.save(img_path)
        print("图像被保存为: " + img_path)


    # 返回文件夹curr_dir下所有文件名
    def ret_all_filenames(self, curr_dir):
        if not os.path.isdir(curr_dir):
            return None
        filenames = os.listdir(curr_dir)
        r = []
        for filename in filenames:
            filename = curr_dir + filename
            if os.path.isfile(filename):
                r.append(filename)
        return r

