# -*- coding: utf-8 -*-

"""
验证哥德巴赫猜想
实现一段代码，输入一个大于 2 的偶数 k，输出两个质数 m、n，满足 m + n == k。
"""

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

def is_primes(n):
    for i in range(2, int(n/2)):
        if n % i == 0:
            return False
    return True

def Goldbach(k):
    if k > 2 and k % 2 == 0:
        for m in primes():
            n = k - m
            if is_primes(n):
                print(m, n)
                return True
        print('No matched result.')
        return False
    else:
        print('Input error, not even number given.')

if __name__ == '__main__':
    Goldbach(1234)
    Goldbach(123456)
    Goldbach(12345678)
    Goldbach(123)
