#

lista = list()

while True:
    nome = (input('Digite o nome do aluno: '))
    nota1 = (float(input('Digite a primeira nota: ')))
    nota2 = (float(input('Digite a segunda nota: ')))
    media = (nota1 + nota2) / 2
    lista.append([nome,[nota1,nota2], media])
    c = input('Voce quer continuar [S/N]? ').upper()[0]
    if c == 'N':
        break

for p, a in enumerate(lista):
    print(f'{p:<2} {a[0]:.<30}Media: {a[2]}')


while True:
    o = int(input('Digite o numero do aluno q vc quer: (999 interrompe) '))
    if o == 999:
        break
    if o <=len(lista) - 1:
        print(f'nome {lista[o][0]} notas {lista[o][1]}')


print(lista)

