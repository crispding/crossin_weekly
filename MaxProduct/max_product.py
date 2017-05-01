#!/usr/bin/env python3
 
"""
设定一个长度为 N 的数字串，将其分为两部分，找出一个切分位置，使两部分的乘积值最大，并返回最大值。
附加题：
输入的数字串可以重新打乱排列，比如输入 123 ，打乱排列之后会有 132，213，231，312，321 等情况，其他条件不变，求最大值。
"""

def product(num):
    l = len(str(num))
    result = []
    for i in range(l):
        p1 = num // 10**(i + 1)
        p2 = num % 10**(i + 1)
        m = p1 * p2
        result.append(m)
    return max(result)

import itertools

def product_2(num):
    result = []
    num_list = itertools.permutations(str(num))
    for i in num_list:
        num_join = int(''.join(i))
        result_i = product(num_join)
        result.append(result_i)
    return max(result)

print(product(1234))
print(product_2(12345))
