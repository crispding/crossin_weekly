#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def is_ArmstrongNumber(n):
    ori_num = n
    cubic_sum = 0
    try:
        while n > 0:
            m = n % 10
            cubic_sum += m**3
            n = n // 10
        if ori_num == cubic_sum:
            return True
        else:
            return False
    except TypeError as e:
        return 'Must be an int number.', e

def closest_ASN(n):

    n_small = n - 1
    cls_asn = 0
    while n_small > 0:
        if is_ArmstrongNumber(n_small):
            cls_asn = n_small
            break
        n_small -= 1
    
    n_large = n + 1
    while n_large:
        if cls_asn > 0 and n_large - n >= n - cls_asn:
            break
        if is_ArmstrongNumber(n_large):
            cls_asn = n_large
            break
        n_large += 1

    return cls_asn    

if __name__ == '__main__':

    # print(is_ArmstrongNumber(407))

    Armstr_num_list = []
    for i in range(1, 1000):
        if is_ArmstrongNumber(i):
            Armstr_num_list.append(i)
    print(Armstr_num_list)

    num = int(input('请输入一个整数：'))
    print('距离 %d 最近的阿姆斯特朗数：%d' %(num, closest_ASN(num)))
