#

from datetime import date
atual = date.today().year
ano_nasc = int(input('digite a sua idade para saber sua categoria de natacao no ARTES PISCINAS AZUL TURQUESA'))
idade = atual - ano_nasc

if idade<=9:
    print(f'Voce tem {idade} anos, sua categoria e MIRIM')
elif idade<=14:
    print(f'Voce tem {idade} anos, sua categoria e INFANTIL')
elif idade<=19:
    print(f'Voce tem {idade} anos, sua categoria e JUNIOR')
elif idade<=25:
    print(f'Voce tem {idade} anos, sua cateogria e SENIOR')
else:
    print(f'Voce tem {idade} anos, sua categoria e MASTER!')
    