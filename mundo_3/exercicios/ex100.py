#
from random import randint

numeros = []

def sorteia(*randons):
    numeros.append(randons)

def somaPar():
    soma = 0
    for v in numeros:
        for num in v:
            if num % 2 == 0:
                soma += num
    print(f'A soma dos numeros pares sao {soma}')

sorteia(randint(1,10))
sorteia(randint(1,10))
sorteia(randint(1,10))
sorteia(randint(1,10))
sorteia(randint(1,10))

somaPar()
print(f'Os numeros sorteados foram...',end='')
for number in numeros:
    for n in number:
        print(f'{ n }',end=' ')
print()