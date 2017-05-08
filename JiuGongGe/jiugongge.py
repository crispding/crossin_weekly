# -*- coding: utf-8 -*-

from itertools import permutations
from numpy import array, reshape

def Jiugongge():
    result = []
    L = [x for x in range(1, 10)]
    P = permutations(L, 9)
    for item in P:
        if sum(item[0:3]) == sum(item[3:6]) == sum(item[6:9]) and \
        sum(item[0::3]) == sum(item[1::3]) == sum(item[2::3]) and \
        sum(item[0::4]) == sum(item[2:7:2]):
            result.append(item)
    for rst in result:
        rst_array = array(rst)
        print(rst_array.reshape(3, 3))
        print('')
    print('Number:', len(result))

Jiugongge()
