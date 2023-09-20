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
print(f'{"cod nome":<} {"gols":^18} {"total":>}')
print('-'*40)
for joga in range(0, len(registro)):
    print(f'{joga} {str(registro[joga]["nome"]):<5} {registro[joga]["gols"]:>6}  ')
print('-'*40)

while True:
    escolha = ' '
    escolha = int(input('Qual jogador voce quer ver? '))
    
    if escolha <= len(registro) - 1:
        #socorro
        print('socorro')

        for partida, golz in enumerate():
            print(f'No jogo {partida} fez {golz}')
    else:
        print('numero invalido')

    if escolha == 999:
        break


