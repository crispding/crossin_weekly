#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def romanToInt(s):
    rst = 0
    rd = dict(zip('IXCMVLD', (1, 10, 100, 1000, 5, 50, 500)))
    for a, b in zip(s, s[1:]+s[-1]):
        if a in 'IXC' and rd[a] < rd[b]:
            rst -= rd[a]
        else:
            rst += rd[a]
    return rst

def intToRoman(num):
    intList = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanList = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    rst = ''
    c = 0
    i = 0

    while num > 0:
        c = num // intList[i]
        num %= intList[i]
        while c > 0:
            rst += romanList[i]
            c -= 1
        i += 1
    return rst

if __name__ == '__main__':
    assert romanToInt('III') == 3
    assert romanToInt('IV') == 4
    assert romanToInt('VI') == 6
    assert romanToInt('XIX') == 19
    assert romanToInt('XLV') == 45
    assert romanToInt('MCMLXXX') == 1980
    assert romanToInt('CMXCIX') == 999

    print(romanToInt('MMCMLXXX'))
    print(intToRoman(997))
