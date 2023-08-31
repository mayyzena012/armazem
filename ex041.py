#

idade = int(input('digite a sua idade para saber sua categoria de natacao no ARTES PISCINAS AZUL TURQUESA'))

if idade<=9:
    print(f'Voce tem {idade} anos, sua categoria e MIRIM')
elif idade<=14:
    print(f'Voce tem {idade} anos, sua categoria e INFANTIL')
elif idade<=19:
    print(f'Voce tem {idade} anos, sua categoria e JUNIOR')
elif idade<=20:
    print(f'Voce tem {idade} anos, sua cateogria e SENIOR')
else:
    print(f'Voce tem {idade} anos, sua categoria e MASTER!')
    