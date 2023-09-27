#
#74
from random import randint

n = (randint(1,4),randint(1,5),randint(1,5),randint(1,5),randint(1,5))

print(f'a sequencia gerada foi {n}')
print(f'o maior valor foi {max(n)} e o menor foi {min(n)}')

#75
num = (int(input('digite um numero ')),
       int(input('digite um numero ')),
       int(input('digite um numero ')),
       int(input('digite um numero ')))

print('os numeros pares foram', end= ' ')
for d in num:
    if d % 2 == 0:
        print(d, end= ' ')


print(f' \n o numero 9 apareceu {num.count(9)}',)
if 3 in num:
    print(f'a posicao que foi digitado o valor 3 foi {num.index(3)}')
else:
    print('valor 3 nao foi digitado')

