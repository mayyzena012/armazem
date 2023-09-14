#
from random import randint

jogadores = dict()


jogadores['jogador 1'] = randint(1,6)
jogadores['jogador 2'] = randint(1,6)
jogadores['jogador 3'] = randint(1,6)
jogadores['jogador 4'] = randint(1,6)

for k,v in jogadores.items():
    print(f'{k} tirou no dado o valor [ {v} ]')

for i in sorted(jogadores, key=jogadores.get):
    print(f'{i} tirou {jogadores[i]}')
print(jogadores)

