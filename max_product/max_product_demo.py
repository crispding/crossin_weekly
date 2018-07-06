def product(num):
    print(max([int(str(num)[0:i])*int(str(num)[i:]) for i in range(1,len(str(num)))]))


# 附加题
from itertools import permutations
def product_2(num):
    print(max([int(''.join(i)[0:j]) * int(''.join(i)[j:]) for i in permutations(str(num)) for j in range(1, len(''.join(i)))]))

product(123)
product_2(1234)
