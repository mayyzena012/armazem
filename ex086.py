#
from random import randint

lista = list()
cont = 0
while True:
    num = randint(1,60)
    if num not in lista:
        lista.append(num)
        cont+=1
    if cont>=6:
        break

print(lista)

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input('Digite um numero: '))

par = 0
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^4}]', end='')
    if matriz[l][c]%2==0:
        par += matriz[l][c]

soma = matriz[l[0][2]]+matriz[c]