#adsadasdasdada

jogador = dict()
gols = list()

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input('N de partidas jogadas: '))
jogador['partidas'] = partidas

total = 0
for numero_partida in range(partidas):
    gols.append(int(input(f'quantos gols na partida {numero_partida}? ')))
    jogador['gols'] = gols[:]

for gol in gols:
    total += gol
    jogador['total_gols'] = total

print('-='*20)
print(f'Jogador {jogador["nome"]} jogou {partidas} partidas!')

print('-='*20)
for partida,golz in enumerate(gols):
    print(f'Marcando na partida {partida}, fez {golz} gols!')
print(f'Marcando um total de {total} gols!')

