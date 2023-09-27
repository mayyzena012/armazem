#

a = float(input('digite um valor de segmento'))
b = float(input('digite outro valor de segmento'))
c = float(input('digite mais um valor de segmento'))

if a == b == c:
    print('triangulo e equilatero')
elif (a == b and a != c) or (b == c and a != c) or (a == c and c != b):
    print('triangulo isosceles')
elif a != b != c:
    print('triangulo escaleno')
    


''''
if a < b + c and b < a + c and c < a + b:
    print(f'o triangulo de segmentos {a},{b} e {c}, FORMAM TRIANGULO')
else:
    print('o triangulo nao funciona')
    '''