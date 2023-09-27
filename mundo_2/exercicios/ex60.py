#
from math import factorial
num = int(input('digite um numero '))

fa = factorial(num)
print(fa)

c = num
f = 1
while c > 0:
    print(f'{c}', end=' ')
    f *= c
    c -= 1
    print(f'{f}', end= ' ')
    

    