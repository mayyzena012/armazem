#jogo de jokenpo mayyzenapapel

# PEDRA mata TESOURA
# TESOURA mata PAPEL
# PAPEL mata PEDRA

from random import choice
from colorama import *
from time import sleep

print('_____________BEM VINDO AO JOGO MAIS DIFICL DA MAYYZENA_____________')

while True:
    escolha_jogador = input(f'''{Fore.GREEN} -------- Digite sua escolha --------
    [PEDRA], [PAPEL] OU [TESOURA]??? \n {Fore.RESET}''').strip().upper()

    escolhas = ['PEDRA', 'PAPEL', 'TESOURA']

    escolha_computador = choice(escolhas).upper()

    if escolha_jogador == escolha_computador:
        print(Fore.YELLOW +  '-=' * 35)
        print(Fore.YELLOW + f'ISSO E UM EMPATE!! Voce escolheu {escolha_jogador} e o computador escolheu {escolha_computador}')  
        print('-=' * 35)
    elif (escolha_jogador == 'PAPEL' and escolha_computador == 'TESOURA') or (escolha_jogador == 'TESOURA' and escolha_computador == 'PEDRA') or (escolha_jogador == 'PEDRA' and escolha_computador == 'PAPEL'):
        print(Fore.RED + '-=' * 35)
        print(Fore.RED + f'VOCE PERDEU!! o computador escolheu {escolha_computador} e voce escolheu {escolha_jogador}')
        print('-=' * 35)
    elif (escolha_jogador == 'PAPEL' and escolha_computador == 'PEDRA') or (escolha_jogador == 'TESOURA' and escolha_computador == 'PAPEL') or (escolha_jogador == 'PEDRA' and escolha_computador == 'TESOURA'):
        print(Fore.CYAN + '-=' * 35)
        print(Fore.CYAN + f'VOCE GANHOU!! o computador escolheu {escolha_computador} e voce escolheu {escolha_jogador}')
        print('-=' * 35)
    else:
        print(Fore.BLUE +'-=' * 35)
        print(Fore.BLUE + 'voce digitou ERRADO, so temos opcoes de PEDRA, PAPEL E TESOURA!')
        print('-=' * 35)
    
