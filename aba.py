#area de testes

import math

num = float(input('digite um numero'))

print(f'o valor inteiro de {num} e {(math.trunc(num))}')

x = float(input('cateto oposto'))
y = float(input('cateto adjacente'))

hip = math.hypot(x, y)

print(f'a hipotenusa e {hip:.2f}')

x1 = float(input('angulo qualquer'))

re1 = math.cos(math.radians(x1))
re2 = math.tan(math.radians(x1))
re3 = math.sin(math.radians(x1)) 

print(f'{re1:.2f} {re2:.2f} {re3:.2f}')

import random

n1 = str(input('primeiro aluno'))
n2 = str(input('segundo aluno'))
n3 = str(input('terceiro aluno'))
n4 = str(input('quarto aluno'))

lista = [n1, n2, n3, n4]
random.suffle(lista)

print(f'o aluno escolhido foi{random.choice([n1, n2, n3, n4])}')
print(f'a ordem de trabalho sera {lista}')