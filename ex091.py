#
from random import randint

jogadores = dict()


for j in range(1,6):
    jogadores[f'jogador{j}'] = randint(1,6)

for k,v in jogadores.items():
    print(f'{k} tirou no dado o valor [ {v} ]')

for i in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{i} tirou {jogadores[i]}')
print(jogadores)

