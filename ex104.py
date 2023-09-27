#
def leiaInt(num):
    ok = False
    value = None
    while True:
        n = input(num)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Digite um valor inteiro')
        if ok:
            break
    return valor

n = leiaInt('Digite um numero')
print(f'voce digitou o numero {n}')