#faca um programa que mostre na tela uma contangem regressiva para o estouro de fogs de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles

from time import sleep
print('FOGOS DE ARTIFICIO SERAO LANCADOS EM 10 SEGUNDOS')\

for a in range(10,0 - 1, -1):
    print(f'faltam apenas {a} segundos')    
    sleep(1)
print('KABOOOOOOOOOM! feliz ano novo eeeh!')