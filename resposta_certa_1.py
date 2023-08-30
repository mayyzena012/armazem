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
    print(f'PROCESSANDO...')
    sleep(5)
    print('Parabens sua resposta esta correta e eu também te amo, amor')
else:
    'nao' and 'não' in resposta
    print('VOCÊ É MALUCA?????')
    print(f'CUIDADO COM SUAS RESPOSTAS... E TOME')
    sleep(5)
    print(f'seu sistema será desligado como punição')
    sleep(5)
    #os.system("shutdown /s /t 1")
    

