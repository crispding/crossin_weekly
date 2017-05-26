# -*- coding: utf-8 -*-

def yanghui(m, n):

    if m < n:
        print('invalid query')
        return -1
    elif m < 2 or n == 0 or m == n:
        return 1
    else:
        return yanghui(m-1, n-1) + yanghui(m-1, n)

def generate_yh(m):

    for i in range(m):
        for j in range(i+1):
            print(yanghui(i, j), end=' ')
        print('')

if __name__ == '__main__':
    # print(yanghui(6, 3))
    # print(yanghui(5, 6))
    # generate_yh(100)
