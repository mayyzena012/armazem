#adsadasdasdada

jogador = dict()
gols = list()

jogador['nome'] = input('Nome do jogador: ')
partidas = int(input('N de partidas jogadas: '))
jogador['partidas'] = partidas


for n in range(partidas):
    gols.append(int(input(f'quantos gols na partida {n}? ')))
    jogador['gols'] = gols


print(jogador)
print(gols)
