#

maisnum = int(input('digite mais numeros '))

soma = 0
cont = 0
maisnum = 0
while maisnum != 999:
    #num = int(input('digite um numero '))
    soma += maisnum 
    cont += 1
    maisnum = int(input('digite mais numeros '))
    #print(f' {soma} {cont}')


print(f'Encerrou. A soma da quantidade de {cont} numeros digitados e {soma}')