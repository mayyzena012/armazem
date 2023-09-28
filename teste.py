

def aumentar(v,p):
    return str(f'R${v+(v*(p/100)):.2f} ')

def diminuir(v,p):
    return str(f'R${v*(1-(p/100)):.2f}')

def dobro(v):
    return str(f'R${v*2:.2f}')

def metade(v):
    return str(f'R${v/2:.2f}')

def resumo(v,a,d):
    v = float(v)
    a = float(a)
    d = float(d)

    def V(v):
        return str(f'R${v:.2f}')

    def linha(t):
        print('-'*t)
    s = 40
    linha(s)
    print(f'{"RESUMO DO VALOR":^40}')
    linha(s)

    print(f'PREÇO ANALIZADO:{V(v):>19}')
    print(f'DOBRO DO PREÇO:{dobro(v):>20}')
    print(f'METADE DO PREÇO:{metade(v):>18}')
    print(f'{a}% DE AUMENTO:{aumentar(v,a):>21}')
    print(f'{d}% DE REDUÇÃO:{diminuir(v,d):>19}')
    linha(s)


v = input('Digite o preço: R$')
resumo(v,10,13)
















