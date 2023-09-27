#

jogador = dict()
registro = list()
gols = list()
soma = 0 

while True:
    print('-'*30)
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input('N de partidas jogadas: '))

    for numero_partida in range(jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {numero_partida}? ')))

    jogador['total'] = sum(gols)
    jogador['gols'] = (gols[:])
    gols.clear()
    registro.append(jogador.copy())

    continuar = input('Voce quer continuar? [S/N] ').upper()[0]

    if continuar == 'N':
        break

print('-='*20)
print('cod ', end='')
for chave in jogador.keys():
    print(f'{chave:<13}', end ='')
print()
print('-'*50)
for key, valor in enumerate(registro):
    print(f'{key:<3}', end= '')
    for valo in valor.values():
        print(f'{str(valo):<13}', end='')
    print()
print('-'*50)

while True:
    escolha = ' '
    escolha = int(input('Qual jogador voce quer ver? '))
    
    if escolha == 999:
        break
    if escolha >= len(registro):
        print('ERRO. Nao tem esse jogador')
    else:
        print(f'DADOS DO JOGADOR {registro[escolha]["nome"]}: ')
        for partida, golz in enumerate(registro[escolha]['gols']):
            print(f'        Na partida {partida} fez {golz} gols!')

