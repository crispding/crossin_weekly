#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def is_ArmstrongNumber(n):

    ori_num = n
    cubic_sum = 0
    exp = len(str(n))

    try:
        while n > 0:
            m = n % 10
            cubic_sum += m**exp
            n = n // 10
        if ori_num == cubic_sum:
            return True
        else:
            return False
    except TypeError as e:
        return '必须为整数类型。', e


def Near_Ams_Num(n):
    forward, backward = n, n
    while True:
        if is_ArmstrongNumber(forward):
            return forward
        elif is_ArmstrongNumber(backward):
            return backward
        forward += 1
        backward -= 1


if __name__ == '__main__':

    # print(is_ArmstrongNumber(8208))

    ASN_List = []
    for i in range(1, 1000):
        if is_ArmstrongNumber(i):
            ASN_List.append(i)
    print('1000以内的阿姆斯特朗数为：', ASN_List)

    num = int(input('请输入一个整数：'))
    print('距离 %d 最近的阿姆斯特朗数：%d' % (num, Near_Ams_Num(num)))
