#bem vindo ao jogo da resposta certa

import os
from time import sleep

print('-=-'*30)
print('Olá, Ana! Seja bem vinda a um teste extremamente dificil sobre nossa relação!')
print('-='*40)
print('Este teste é perigoso e você deve responder ele com cuidado')
print('Responda com atenção as próximas perguntas!!')
print('-=-'*40)

resposta = str(input('Você me ama?')).strip().lower()

if 'sim' in resposta:
    print('PROCESSANDO...')
    sleep(5)
    print('Parabens sua resposta esta correta e eu também te amo, amor')
else:
    'nao' and 'não' in resposta
    print('VOCÊ É MALUCA?????')
    print('CUIDADO COM SUAS RESPOSTAS... E TOME')
    sleep(5)
    print('seu sistema será desligado como punição')
    sleep(10)
    os.system('shutdown /s /t 1')

resposta2 = input('você vai desinstalar o Valorant?')

if 'sim' in resposta2:
    print('Ok, então, valorante será destruido do seu PC')
    print('PROCESSANDO...')
    sleep(5)
    input('Obrigada por participar amor, digite algo para sair do programa :D')
else:
    'nao' and 'não' in resposta2
    print(f'COMO ASSIM? VOCE VAI DIZER {resposta2}??')
    print('pois você sera punida agora!')
    print('seu sistema sera desligado em punição! E TOME!')
    sleep(10)
    os.system('shutdown /s /t 1')
