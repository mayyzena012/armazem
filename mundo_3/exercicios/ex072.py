#


num = ('zero', 'um', 'dois', 'tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


s = ' '
while True:
    n = int(input('Digite um numero entre 0 e 20: '))
    print(f'voce digitou o numero {num[n]}')
    while True:
        s = input('voce quer continuar S/N? ').upper()
        if s in 'S' or 'N':
            break
        else:
            print('invalido tente novamente')
            while True:
                if 0 <= n <=20:
                    break
                print('tente novamente ')
    if s == 'N':
        print('encerrado')
        break



