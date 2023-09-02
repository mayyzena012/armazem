#

n1 = int(input('digite um numero'))
n2 = int(input('digite mais um numero'))



opcao = 0
soma = 0
maior = 0

while opcao != 5:
    opcao = int(input('escolha entre as opcoes \n [1] soma \n [2] multiplicar \n [3] maior \n [4] novos numeros \n [5] sair do programa'))
    if opcao == 1:
        soma += n1+n2
        print(f'A soma dos numeros {n1} e {n2} sao {soma}')
    elif opcao == 2:
        mult = n1*n2
        print(f'a multiplicao resulta em {mult}')
    elif opcao == 3:
        maior > n1 and n2
        maior = n1 and n2
        print(f'o numero maior e {maior}')
    elif opcao == 4:
        n1 = int(input('digite um numero'))
        n2 = int(input('digite mais um numero'))
    elif opcao == 5:
        print('programa encerrado')
    else:
        print('programa encerrado')
    
        