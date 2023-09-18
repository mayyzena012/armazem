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
print('Cod nome gols total')
print('-'*30)
for posicao,jogador in enumerate(registro):
    print(f' {posicao:<2} {jogador["nome"]:<5} {jogador["gols"]}')
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