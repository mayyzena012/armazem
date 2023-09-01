#

soma = 0

for a in range(6):
    q = int(input('digite um numero'))
    if q % 2 == 0:
        soma += q
print(f'a soma ds numeros pares e {soma}')