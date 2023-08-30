#mais uma tela

vel = float(input('Quanto voce estava de velocidade?'))

if vel>=81:
    print(f'voce foi multado em {((vel-80)*7):.2f}')
else:
    print('voce nao foi multado')

num1 = int(input('digite um numero'))

resultado = num1 % 2

if resultado==0:
    print(f'o numero {num1} e PAR!!')
else:
    print(f'o numero {num1} e IMPAR!!')

dis = int(input('qual foi a distancia da sua viagem?'))
if dis<=200:
    preco = dis * 0.50
else:
    preco = dis * 0.45
print(f'o preco a ser pagado sera R${preco:.2f}')

ano = int(input('digite um ano'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'o ano de {ano} e um ano BISSEXTO!')
else:
    print(f'o ano de {ano} NAO e um ano bissexto!')

#n0 = int(input('digite um numero'))
#n1 = int(input('digite outro numero'))
#n2 = int(input('digite mais um numero'))
#if n0>n1 and n2:
#    maior = n0
#if n1>n0 and n2:
 #   maior = n1
#if n2>n0 and n1:
#    maior = n2
#if n2<n0 and n1:
 #   menor = n2
#if n2<n0 and n1:
 #   menor = n2
#if n2<n0 and n1:
 #   menor = n2
#print(f'o numero menor e {menor} e o maior e {maior}')
    

valor = float(input('digite seu salario atual para verificar:'))
if valor>1250:
    aumento = (valor * 10) / 100 + valor
else:
    aumento = (valor * 15) / 100 + valor
print(f'o seu aumento sera de {aumento:.2f}R$')

a = float(input('digite um valor de segmento'))
b = float(input('digite outro valor de segmento'))
c = float(input('digite mais um valor de segmento'))

resultado = ('trianulo existe')

if a < b + c and b < a + c and c < a + b:
    print(f'o triangulo de segmentos {a},{b} e {c}, FORMAM TRIANGULO')
else:
    print('o triangulo nao funciona')


