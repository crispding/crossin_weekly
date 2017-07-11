# -*- coding: utf-8 -*-

def generateMatrix(n):
    A, low = [], n*n+1
    while low > 1:
        low, high = low - len(A), low
        A = [list(range(low, high))] + list(zip(*A[::-1]))  # python33 语法 与27会有差别
        # print(A)
    return A

if __name__ == '__main__':
    # print(generateMatrix(4))
    n = int(input('Input Number: '))
    res = generateMatrix(n)
    for i in res:
        for j in i:
            print(j, end='\t')
        print('\n')
