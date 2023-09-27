#

primeiro_termo = int(input('digite o primeiro termo '))
razao = int(input('digite a razao '))

termo = primeiro_termo
a = 1
while mais!=0:
    while a<=10:
        print(f'{termo}', end= ' -> ')
        termo += razao
        a += 1
    
    mais = int(input(' \n Quantos termos voce quer mostrar mais '))
    termo2 = mais
    if mais == ' ':
        while a <=termo2:
            print(termo2)
            termo2+= razao
            a +=1