#funcoes eba!

def til(txt):
    print('-'*30)
    print(txt)
    print('-'*30)

til('MAYRA PROGRAMADORAH')
til('JULIANO CAMINHOES')

def soma(a, b):
    print(f' a = {a} b = {b}')
    s = a+b
    print(f'A soma de A + B e {s}')

soma(4, 5)
soma(b=3, a=7)
soma(5, 6)
soma(1,4)

def contador(*num):
    tam = len(num)
    print(f'recebi os valores {num} e sao ao todo {tam} numero')
contador(2,1,6)
contador(3,4,6,2,1)

def dobra(lista):
    pos = 0
    while pos <len(lista):
        lista[pos] *= 2
        pos += 1

valores = [6,7,8,9,1,3,5]
dobra(valores)
print(valores)

def soma(*valores):
    sum = 0
    for num in valores:
        sum += num
    print(f'A soma dos valores {valores} e {sum}')

soma(5,2,5)
soma(1,2,8)
