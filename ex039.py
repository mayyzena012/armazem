#

nascimento = int(input('digite sua data de nascimento para verificar'))

calculo = 2023 - nascimento

if calculo<18:
    print(f'voce tem apenas {calculo} anos, ainda nao chegou sua hora de sofrer e tomar banho gelado, mas ESTA CHEGANDO! Braco forte, mao amiga!')
elif calculo == 18:
    print(f'voce infelizmente tem {calculo} anos, se fodeu chegou a hora de comer feijao frio, braco forte, mao amiga!!!')
else:
    print(f'voce ja tem {calculo} anos, vai procurar um emprego. Seu tempo de alistamente ja passou')