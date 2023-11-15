'''
file: \Flicker\flicker.py
author: SMS
date: 2023-06-12 20:50:02
lasttime: 2023-07-12 09:50:37
description: Flicker主程序文件
'''
########################↓Pack↓#########################
import math_def 
import image_def
import num_lib as lib

import math
import numpy as np
import cv2
import csv
########################↓参数控制↓#########################
dc_min = 0.038
dc_max = 0.072
dmax_min = 0.256
dmax_max = 0.319
pst_min = 0.102
pst_max = 0.131
#文件名
file = "test24"
#文件数量
file_num = 9
#文件路径
file_path = "F:\OneDrive365\OneDrive - bp\General - bp\.ZMM\Flicker\\"

########################↓Function↓#########################

#生成图片
def image_creat(num:int,file_name:str):
    flicker = cv2.imread("flicker_0.png")
    #生成csv文件&附加行标题
    with open(file_path + file_name + ".csv",'w',encoding='utf8',newline='') as f:
        write = csv.writer(f)
        write.writerow(["flie_name","dc","dmax","pst","plt"])
    for _ in range(num):
        name = file_name + "_" + str(_)
        #生成数组
        dc = math_def.value_dc(12,dc_min,dc_max)
        dmax = math_def.value_dc(12,dmax_min,dmax_max)
        pst = math_def.value_dc(12,pst_min,pst_max)
        plt = math_def.array_average(pst)
        #输出最大值
        print(name)
        print("dc  :" + str(math_def.array_max(dc))+"--"+str(dc))
        print("dmax:" + str(math_def.array_max(dmax))+"--"+str(dmax))
        print("Pst :" + str(math_def.array_max(pst))+"--"+str(pst))
        print("Plt :" + str(plt))

        for i in range(len(dc)):
            if i%2 == 0:
                lib.b = 27
            else:
                lib.b = 0
                
            picture = image_def.array2image(image_def.array_add(
                        math_def.num2array(math_def.split_float(dc[i])[0]),
                        lib.num_dot(lib.b),
                        math_def.num2array(math_def.split_float(dc[i])[1]),
                        math_def.num2array(math_def.split_float(dc[i])[2]),
                        math_def.num2array(math_def.split_float(dc[i])[3])
                        ))
            flicker[lib.dc_pos[i][0]:lib.dc_pos[i][1],lib.dc_pos[i][2]:lib.dc_pos[i][3]] = picture

        for i in range(len(dmax)):
            if i%2 == 0:
                lib.b = 27
            else:
                lib.b = 0
                
            picture = image_def.array2image(image_def.array_add(
                        math_def.num2array(math_def.split_float(dmax[i])[0]),
                        lib.num_dot(lib.b),
                        math_def.num2array(math_def.split_float(dmax[i])[1]),
                        math_def.num2array(math_def.split_float(dmax[i])[2]),
                        math_def.num2array(math_def.split_float(dmax[i])[3])
                        ))
            flicker[lib.dmax_pos[i][0]:lib.dmax_pos[i][1],lib.dmax_pos[i][2]:lib.dmax_pos[i][3]] = picture

        for i in range(len(pst)):
            if i%2 == 0:
                lib.b = 27
            else:
                lib.b = 0     
            picture = image_def.array2image(image_def.array_add(
                        math_def.num2array(math_def.split_float(pst[i])[0]),
                        lib.num_dot(lib.b),
                        math_def.num2array(math_def.split_float(pst[i])[1]),
                        math_def.num2array(math_def.split_float(pst[i])[2]),
                        math_def.num2array(math_def.split_float(pst[i])[3])
                        ))
            flicker[lib.pst_pos[i][0]:lib.pst_pos[i][1],lib.pst_pos[i][2]:lib.pst_pos[i][3]] = picture
            

            lib.b = 0   
            picture = image_def.array2image(image_def.array_add(
                        math_def.num2array(math_def.split_float(plt)[0]),
                        lib.num_dot(lib.b),
                        math_def.num2array(math_def.split_float(plt)[1]),
                        math_def.num2array(math_def.split_float(plt)[2]),
                        math_def.num2array(math_def.split_float(plt)[3])
                        ))
            flicker[lib.plt_pos[0][0]:lib.plt_pos[0][1],lib.plt_pos[0][2]:lib.plt_pos[0][3]] = picture

        # cv2.imshow("1",flicker)
        # cv2.waitKey(1000)
        cv2.imwrite(file_path + name + ".png",flicker)
        # 附加csv文件数据
        with open(file_path + file_name+".csv",'a',encoding='utf8',newline='') as f:
            write = csv.writer(f)
            write.writerow([name,str(math_def.array_max(dc)),str(math_def.array_max(dmax)),str(math_def.array_max(pst)),str(plt)])

image_creat(file_num,file)