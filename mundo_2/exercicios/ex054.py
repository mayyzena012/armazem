#

from datetime import date
tot = 0
tot1 = 0
atual = date.today().year 
for a in range(8):
    ano = int(input('digite sua data de nascimento'))
    idade = atual - ano
    if idade<=18:
        tot += 1
    else:
        tot1 += 1
print(f'temos o total de {tot} menores de idade e {tot1} maiores de idade')
       
maior = 0
menor = 0

for p in range(5):
    peso = float(input('digite o peso da {p} pessoa'))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'o maior peso lido foi {maior}')
print(f'o menor peso lido foi {peso}')
