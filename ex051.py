#

#desenvolva um programa que leia o primeiro termo e a razao de uma PA. No final, mostre os 10 primeiros termos dessa progressao

primeiro_termo = int(input('digite o primeiro termo '))
razao = int(input('digite a razao '))

for a in range(10):
    termo = primeiro_termo + a * razao
    print(f'{termo}', end= ' -> ')
