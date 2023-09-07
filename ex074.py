#

from random import randint

s = [randint(1,5) for a in range(5)]
print(s)
maior = max(s)
menor = min(s)
print(maior,menor)