#
def leiaInt(num):
    is_ok = False
    value = None
    while True:
        numero = input(f'{num}')
        if num.isnumeric():
            value = numero
            is_ok = True
        else:
            print('Digite um numero inteiro')
        if is_ok:
            break
    return value

n = leiaInt('Digite um numero')