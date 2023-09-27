#
from random import randint
print('----- Jogo de adivinhacao da Mayra no Python versao 2.0 -----')

escolha_computador = randint(0,10)
escolha_jogador = int(input('Digite um numero para tentar adivinhar!'))
total = 0

while escolha_computador != escolha_jogador:
        print('Tente Novamente! Voce errou')
        escolha_jogador = int(input('Digite um numero para tentar adivinhar!'))
        escolha_computador = randint(0,10)
        total += 1
        if escolha_jogador == escolha_computador: 
                print(f'PARABENS vc ganhou! voce escolhe {escolha_jogador} e o computador escolheu {escolha_computador} e voce rodou {total}')
    

computador = randint(0,10)
acertou = False
palpites = 0
while not acertou:
        print('Tente Novamente! Voce errou')
        jogador = int(input('Digite um numero para tentar adivinhar!'))
        palpites += 1
        if jogador == computador:
            acertou = True
            print(f'PARABENS vc ganhou! voce escolhe {jogador} e o computador escolheu {computador} e voce rodou {total}')