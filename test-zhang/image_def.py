'''
file: \Flicker\image_def.py
author: SMS
date: 2023-06-12 23:34:35
lasttime: 2023-06-14 09:08:11
description: 图像相关方法
'''
########################↓Pack↓#########################
import random
import math
import cv2
import num_lib
import numpy as np

#######################################################

# image_RGB0 = img = cv2.imread("0-9_RGB0.png")
# image_RGB27 = img = cv2.imread("0-9_RGB27.png")
# image_RGB27 = 
# print(image_RGB0.shape)
# num_0 = image_RGB27[0:14,0:12]
# num_1 = image_RGB27[14:28,0:12]
# num_2 = image_RGB27[28:42,0:12]
# num_3 = image_RGB27[42:56,0:12]
# num_4 = image_RGB27[56:70,0:12]
# num_5 = image_RGB27[70:84,0:12]
# num_6 = image_RGB27[84:98,0:12]
# num_7 = image_RGB27[98:112,0:12]
# num_8 = image_RGB27[112:126,0:12]
# num_9 = image_RGB27[126:140,0:12]
# num_dot = image_RGB27[140:154,0:5]

######################↓Function↓########################




def array2image(arr):
    '''
    brief: 数组转化为OpenCV图像数组
    param {list} arr
    return {*}
    '''
    pred = np.array(arr,np.uint8)
    return pred

def array_add(arr1,arr2,arr3,arr4,arr5):
    '''
    brief: 数组拼接
    param {list} arr
    return {*}
    '''
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    arr3 = np.array(arr3)
    arr4 = np.array(arr4)
    arr5 = np.array(arr5)
    array_new = np.concatenate((arr1,arr2),axis=1)
    array_new = np.concatenate((array_new,arr3),axis=1)
    array_new = np.concatenate((array_new,arr4),axis=1)
    array_new = np.concatenate((array_new,arr5),axis=1)
    return array_new

# picture1 = array2image(array_add(num_lib.num_0,num_lib.num_dot,num_lib.num_4,num_lib.num_1,num_lib.num_3))




# flicker = cv2.imread("flicker_0.png")
# flicker[dc_pos[0][0]:dc_pos[0][1],dc_pos[0][2]:dc_pos[0][3]] = picture1
# cv2.imshow("11",flicker)
# cv2.waitKey(0)

