#


soma = cont = media = maior = menor = 0
resposta = 'S'

while resposta in 'Ss':
    num = int(input('digite um numero '))
    resposta = input('voce quer digitar mais algum numero S/N? ').upper()[0]
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    if resposta == 'N':
        print('encerrado')
        print(f'')

media = soma / cont
print(f'dos numeros digitado o menor e {menor} e o maior e {maior} e a media deles sao {media:.2f} voce digitou {cont} numeros')