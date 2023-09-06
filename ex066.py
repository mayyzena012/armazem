#
soma = cont = 0
while True:
    num = int(input('digite um numero '))
    if num >= 999:
        break
    cont += 1
    soma += num
print(f'voce digitou {cont} numeros e a soma entre eles foi {soma}')