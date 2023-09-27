#caixa eletronico simulator

print('='*30)
print('{:^30}'.format('BANCO MAYYZENA'))
print('='*30)

valor = int(input('Qual valor voce quer sacar? R$ '))

totcd = 0
n50 = n20 = n10 = n1 = 0
while True:
    if valor>=50:
        valor -=50
        n50+=1
    elif valor>=20:
        valor-=20
        n10+=1
    elif valor>=10:
        valor-=10
        n10+=1
    elif valor>=1:
        valor-=1
        n10+=1
    print(f'para sacar {valor} foram usadas ')
    print(f'{n50} notas de 50')
    print(f'{n20} notas de 20')
    print(f'{n10} notas de 10')
    print(f'{n1} notas de 1')
    break