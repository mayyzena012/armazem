#bem vindo ao jogo da resposta certa

import os
from time import sleep

def reticencias(quantidade:int):
    for a in range(0,quantidade):
        print(".",end="",flush=True) # o end="" é para ele não pular a linha após printar, o flush nem me indague, só sei que bugava quando usava junto com o time sem deixar True
        sleep(0.5)

print('-=-'*30)
print('Olá, Ana! Seja bem vinda a um teste extremamente dificil sobre nossa relação!')
print('-='*40)
print('Este teste é perigoso e você deve responder ele com cuidado')
print('Responda com atenção as próximas perguntas!!')
print('-=-'*40)



while True:
    RESPOSTAS_VALIDAS = ("sim","claro","óbvio")
    RESPOSTAS_NEGATIVAS = ("não","nao","jamais","nunca", "de jeito nenhum","nem fudendo")
    resposta = input('Você me ama?: ').strip().lower()
    if resposta in RESPOSTAS_VALIDAS:
        print('PROCESSANDO',end="")
        reticencias(10)
        print('\nParabens sua resposta esta correta e eu também te amo, amor!')
        break
    elif resposta in RESPOSTAS_NEGATIVAS:
        print('PROCESSANDO',end="")
        reticencias(10)
        print('VOCÊ É MALUCA?????')
        print('CUIDADO COM SUAS RESPOSTAS... E TOME')
        sleep(4)
        print('seu sistema será desligado como punição')
        sleep(15)
        #os.system('shutdown /s /t 1')
        break
    else: 
        print("responda direito, vagabunda!\n")


while True:
    RESPOSTAS_VALIDAS = ("sim","claro","óbvio","vou")
    RESPOSTAS_NEGATIVAS = ("não","nao","jamais","nunca", "de jeito nenhum","nem fudendo")

    resposta = input('você vai desinstalar o Valorant?')

    if resposta in RESPOSTAS_VALIDAS:
        print('Ok, então, valorante será destruido do seu PC')
        print('PROCESSANDO',end="")
        reticencias(10)
        input('\nObrigada por participar amor, digite enter para sair do programa :D')
        break
    elif resposta in RESPOSTAS_NEGATIVAS:
        print(f'COMO ASSIM? VOCE VAI DIZER {resposta}??')
        print('pois você sera punida agora!')
        print('seu sistema sera desligado em punição! E TOME!')
        sleep(10)
        #os.system('shutdown /s /t 1')
        break
    else: 
        print("responda direito, vagabunda! \n")


=======
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

