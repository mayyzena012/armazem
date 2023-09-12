#
lista = list()
dado = list()
while True:
    dado.append(input('Digite o nome do aluno: '))
    dado.append(float(input('Digite a primeira nota: ')))
    dado.append(float(input('Digite a segunda nota: ')))
    c = input('Voce quer continuar [S/N]? ').upper()[0]
    lista.append(dado[:])
    dado.clear()
    if c == 'N':
        break
print(lista[0][1]+lista[0][2])
print(lista)