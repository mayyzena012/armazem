#


num = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

print(num[1])

n = int(input('Digite um numero entre 0 e 20: '))
while True:
    while n >= 21:
        n = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
    if n == 0:
        print(f'o numero {n} se chama {num[0]}')
    elif n == 1:
        print(f'o numero {n} se chama {num[1]}')
    elif n == 2:
        print(f'o numero {n} se chama {num[2]}')
    elif n ==3:
        print(f'o numero {n} se chama {num[3]}')
    elif n ==4:
        print(f'o numero {n} se chama {num[4]}')
    elif n ==5:
        print(f'o numero {n} se chama {num[5]}')
    elif n ==6:
        print(f'o numero {n} se chama {num[6]}')
    elif n ==7:
        print(f'o numero {n} se chama {num[7]}')
    elif n ==8:
        print(f'o numero {n} se chama {num[8]}')
    elif n ==9:
        print(f'o numero {n} se chama {num[9]}')
    elif n ==10:
        print(f'o numero {n} se chama {num[10]}')
    elif n ==11:
        print(f'o numero {n} se chama {num[11]}')
    elif n ==12:
        print(f'o numero {n} se chama {num[12]}')
    elif n ==13:
        print(f'o numero {n} se chama {num[13]}')
    elif n ==14:
        print(f'o numero {n} se chama {num[14]}')
    elif n ==15:
        print(f'o numero {n} se chama {num[15]}')
    elif n ==16:
        print(f'o numero {n} se chama {num[16]}')
    elif n ==17:
        print(f'o numero {n} se chama {num[17]}')
    elif n ==18:
        print(f'o numero {n} se chama {num[18]}')
    elif n ==19:
        print(f'o numero {n} se chama {num[19]}')
    elif n ==20:
        print(f'o numero {n} se chama {num[20]}')
    break

