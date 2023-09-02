#

print('Seja bem vindo a Hamburgueria Mayyzena')
print('Aqui você podera fazer seu pedido')
print('Atenção!')
escolha = 0

def escolha_burger(escolha):
    print('Ok então você quer um '+ escolha)

while escolha != 6:
    escolha = int(input('''Escolha um hamburguer do nosso cardápio: 
    \n [1] X Burger Tradicional \n [2] X Salada \n [3] X Burger Cheddar \n [4] X burger Bacon \n [5] X Burger Duplo \n [6] Encerrar '''))
    if escolha == 1:
        escolha_burger('X Burger Tradicional')
    elif escolha == 2:
        escolha_burger('X Salada')
    elif escolha == 3:
        escolha_burger('X Burger Cheddar')
    elif escolha == 4:
        escolha_burger('X Burger Bacon')
    elif escolha == 5:
        escolha_burger('X Burger Duplo')
    elif escolha == 6:
        print('Você cancelou seu pedido, que pena!')
    molho = int(input('Escolha seu molho'))
