#
val = list()
while True:
    val.append(int(input('digite um numero ')))
    while True:
        p = str(input('Voce quer continuar [S/N]? ')).upper()[0]
        if p == 'S' or 'N':
            break
    
    if p == 'N':
        break

par = list()
impar = list()
for a in val:
    if a % 2 == 0:
        par.append(a)
    elif a % 2 == 1:
        impar.append(a)
    
print(f'A lista completa e {val}')
print(f'os numeros pares sao {par}')
print(f'os numeros impares sao {impar}')