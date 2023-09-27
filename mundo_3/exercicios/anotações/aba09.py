#anotacoes aula 21

def contador(i,f,p):
    """
    -> faz uma contagem e mostra na tela.
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem 
    :return: sem retorno
    """
    c = i
    while i <= f:
        print(f'{c}', end=' ')
        c+=p
    print('fim')

help(contador)

def somar(a,b,c=0):
    s = a+b+c
    print(f'A soma vale {s}')
    return s

somar(3,5)
r1 = somar(4,5)
r2 = somar(1,6)
print(f'os calculos deram {r1} {r2}')


def funcao():
    n1 = 4
    print(f'N1 no escopo local da funcao vale {n1}')

n1 = 1
funcao()
print(f'N1 no escopo global fora da funcao vale {n1}')

def numeros(b):
    global a
    a = 10
    b = 1
    c = 1
    print(f'Os numeros {a}, {b}, {c}')

a = 5
numeros(a)

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input('Digite um numero: '))
print(par(num))
if par(num):
    print('e par')
else:
    print('e impar')
