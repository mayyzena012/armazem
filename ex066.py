#
soma = cont = num = 0
while True:
    soma += num
    cont += 1
    num = int(input('digite um numero '))
    if num >= 999:
        break
print(f'voce digitou {cont} numeros e a soma entre eles foi {soma}')