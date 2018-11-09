# -*- coding: utf-8 -*-

import math
import numpy as np


def calc_pi(radius, precision):
    """
    返回圆周率 pi
    radius：圆的半径
    precision： 精确度(值越小结果越精确)
    """
    count = 0
    for x in np.arange(-radius, radius + 1, precision):
        for y in np.arange(-radius, radius + 1, precision):
            if math.sqrt(x**2 + y**2) <= radius:
                count += 1

    pi = count / (radius**2) * (precision**2)
    return pi


def calc_pi_by_Monte_Carlo(radius, precision):
    """
    返回圆周率 pi
    radius：圆的半径
    precision：生成的点的个数，越大越精确
    """
    inside = 0
    for i in range(precision):
        x = np.random.randint(-radius, radius + 1)
        y = np.random.randint(-radius, radius + 1)
        if math.sqrt(x**2 + y**2) <= radius:
            inside += 1
    pi = inside * 4 / precision
    return pi


if __name__ == "__main__":
    PI = calc_pi_by_Monte_Carlo(1000, 1000000)
    print(PI)
