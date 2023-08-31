#

print('BEM VINDO AO PROGRAMA DE SABER SE VOCE E GORDO')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc<18.5:
    print(f'desnutrido, comer mais, abaixo do peso. Seu IMC e {imc:.2f}')
elif imc<=25:
    print(f'Ta ok ate em, voce esta no peso ideal, seu IMC e {imc:.2f}')
elif imc<=30:
    print(f'caramba ta comendo muito em, voce esta com sobrepeso, seu imc e {imc:.2f}')
elif imc<=40:
    print(f'CARAMBA tu ta enorme compadre, voce esta com obesidade, seu imc e {imc:.2f}')
else:
    print(f'Meu deus voce ja pode participar dos quilos mortais, voce esta com obesidade morbida, seu imc e {imc:.2f}')