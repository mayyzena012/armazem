#
from time import sleep

from hamburgueria_teste.functions import *

print('===== Seja bem vindo a Hamburgueria Mayyzena =====')
print('\n')
print('==== Aqui você podera fazer seu pedido ====')
print('=== Escolha seu pedido de acordo com as opcoes a seguir ===')
print('\n')
print('Aguarde...')
sleep(2)

burger_escolhido = escolha_burger()
molho_escolhido = escolha_molho()
bebida_escolhida = escolha_bebida()



if pedido_cancelado == False:
    print('PEDIDO CANCELADO!')
else:
    print(f'Entao voce quer um um {burger_escolhido}', end= ' ')
    print(f'com {molho_escolhido}', end= ' ')
    print(f'e {bebida_escolhida}')



