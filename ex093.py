#adsadasdasdada

jogador = dict()
gols = list()

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input('N de partidas jogadas: '))
jogador['partidas'] = partidas

total = 0
for n in range(partidas):
    gols.append(int(input(f'quantos gols na partida {n}? ')))
    jogador['gols'] = gols

for gol in gols:
    total += gol
    jogador['total_gols'] = total

print('-='*20)
print(f'Jogador {jogador["nome"]} jogou {partidas} partidas!')

print('-='*20)
for p,g in enumerate(gols):
    print(f'Marcando na partida {p}, fez {g} gols!')
print(f'Marcando um total de {total} gols!')

