#numeros pares sao divisiveis por 2 = 0
#numeros impares NAO sao divisveis por 2 = 1

for m in range(1,51):
    if m % 2 == 0:
        print(m)


for n in range(2, 51, 2):
    print(n, end=' ')
