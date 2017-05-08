# -*- coding: utf-8 -*-

# from itertools import permutations
from numpy import array, mod, reshape, sum as np_sum, zeros

def magic_score(n = 3):
    # 罗伯特法求奇数阶幻方/楼梯法
    if n % 2 == 1:
        A = zeros([n, n])
        posX = 0
        posY = int(n / 2)
        for val in range(1, n**2+1):
            if int(A[posX, posY]):
                posX = mod(posX+2, n)
                posY = mod(posY-1, n)
            # 赋值并更新位置
            A[posX, posY] = int(val)
            posX = mod(posX-1, n)
            posY = mod(posY+1, n)
    print(A)
    # print(np_sum(A[1, :]))

magic_score(n = 7)
