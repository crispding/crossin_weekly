# -*- coding: utf-8 -*-

from itertools import permutations

countries = ['Ameria', 'Germany', 'England', 'France', 'Russia', 'Italy']
persons = ['A', 'B', 'C', 'D', 'E', 'F']

for res in permutations(persons, 6):
    if res[0] in 'AEC' or res[4] in 'AEC' or res[1] in 'AEC':
        continue
    if res[1] in 'BF':
        continue
    if res[3] == 'A' or res[5] == 'C':
        continue
    if res[0] == 'B' or res[3] == 'C':
        continue
    print(sorted(zip(res, countries), key=lambda t: t[0]))
