# -*- coding: utf-8 -*-


def calc_count(h, f):
    '''
    h for heads, f for feets, c for cocks, r for rabbits
    '''
    for c in range(h + 1):
        r = h - c
        if c * 2 + r * 4 == f:
            return c, r
    return 0, 0


heads = int(input('heads number: '))
feets = int(input('feets number: '))
cocks, rabbits = calc_count(heads, feets)
if cocks == rabbits == 0:
    print('invalid input.')
else:
    print('cocks', cocks, 'rabbits', rabbits)
