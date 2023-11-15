'''
file: \Flicker\math_def.py
author: SMS
date: 2023-06-12 23:11:19
lasttime: 2023-06-14 15:56:36
description: 数学有关方法
'''
########################↓pack↓###########################
import random
import math
import numpy as np
import num_lib as lib
#######################↓Function↓########################



def randbetween(a:float,b:float):
    '''
    brief: 生成随机数-3位小数
    param {float} a 
    param {float} b
    return {*}
    '''
    if random.random()>0.4:
        result = round(random.uniform(a,b),3)
    else:
        result = round(random.uniform(a,0.5*(a+b)),3)
    return result


def value_dc(num:int,a:float,b:float):
    '''
    brief: 随机生成12个值的元组
    param {int} num 
    param {float} a
    param {float} b
    return {*}
    '''
    array = [0 for i in range(12)]
    for i in range(1,num+1,1):
        array[i-1]=randbetween(a,b)
    return array


def array_max(arr:list):
    '''
    brief: 输出元素最大值
    param {list} arr
    return {*}
    ''' 
    max = arr[0]
    for i in range(0,len(arr),1):
        if max < arr[i]:
            max = arr[i]
    return max



def split_float(num:float):
    '''
    brief: 分离浮点数返回4位数组
    param {float} num
    return {*}
    '''
    num = int(1000*num)
    array = [0 for i in range(4)]
    array[0] = num//1000
    array[1] = math.fmod(num,1000)//100
    array[2] = math.fmod(num,100)//10
    array[3] = math.fmod(num,10)//1
    return array


def num2array(num:int):
    '''
    brief: 单个数字转化为库中numpy数组
    param {int} num
    return {*}
    '''
    match num:
        case 0:
            return lib.num_0(lib.b)
        case 1:
            return lib.num_1(lib.b)
        case 2:
            return lib.num_2(lib.b)
        case 3:
            return lib.num_3(lib.b)
        case 4:
            return lib.num_4(lib.b)
        case 5:
            return lib.num_5(lib.b)
        case 6:
            return lib.num_6(lib.b)
        case 7:
            return lib.num_7(lib.b)
        case 8:
            return lib.num_8(lib.b)
        case 9:
            return lib.num_9(lib.b)
        

def array_average(arr:list):
    '''
    brief: 求数组元素均值
    param {list} arr
    return {*}
    '''
    average = round(np.mean(arr),3)
    return average

