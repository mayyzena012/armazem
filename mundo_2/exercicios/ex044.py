#

preco = float(input('digite o valor do produto'))
condicao = int(input('digite o numero de como sera feito o pagamento. \n OPCOES \n 0 --- Dinheiro/cheque a vista --- \n 1 --- Cartao a vista --- \n 2 --- Ate 2x no cartao --- \n 3 --- 3x Ou mais com juros ---').strip())

if condicao == 0:
    dinheiro_preco = preco - (preco * 10 / 100)
    print(f'Voce esta pagando com a opcao 0 entao voce tera 10% de desconto e pagara somente R${dinheiro_preco}')
elif condicao == 1:
    cartao_preco = preco - (preco * 5 / 100)
    print(f'Voce esta pagando com a opcao 1 entao voce tera 5% de desconto e pagara somente R${cartao_preco}')
elif condicao == 2:
    print(f'Voce esta pagando com a opcao 2, entao voce ira pagar 2x no cartao o valor de {preco}')    
elif condicao == 3:
    cartao_3x = preco + (preco * 20 / 100)
    print(f'Voce esta pagando com a opcao 3 e o valor sera divido em 3x voce pagara 20% de juros, o valor sera {cartao_3x}')
else:
    print('socorro')