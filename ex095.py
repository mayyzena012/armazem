#

jogador = dict()
registro = list()

while True:
    print('-'*30)
    jogador['nome'] = input('Nome do jogador: ')
    jogador['partidas'] = int(input('N de partidas jogadas: '))
    jogador['total gols'] = 0
    jogador['gols'] = []

    for numero_partida in range(jogador['partidas']):
        jogador['gols'] = (int(input(f'quantos gols na partida {numero_partida}? ')))
        

    continuar = input('Voce quer continuar? [S/N] ').upper()[0]

    registro.append(jogador.copy())

    if continuar == 'N':
        break



print('-='*20)
print(f'{"cod nome":<} {"gols":^18} {"total":>}')
print('-'*30)
for joga in range(0, len(registro)):
    print(f' {joga:<2} {registro[joga]["nome"]:<5} {registro[joga]["gols"]:<5} {registro[joga]["total gols"]:<5}')
print('-'*30)

while True:
    escolha = ' '
    escolha = int(input('Qual jogador voce quer ver? '))
    
    if escolha <= len(registro) - 1:
        #socorro

        for partida, golz in enumerate():
            print(f'No jogo {partida} fez {golz}')
    else:
        print('numero invalido')

    if escolha == 999:
        break

print(registro)
print(jogador)