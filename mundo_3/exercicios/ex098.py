#ex098
from time import sleep

def contagem(inicio, fim, passo):
    print(f'Contangem de {inicio} ate {fim} pulando de {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont += passo
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.5)
            cont -= passo
        print()
    #if inicio 

contagem(1,10,1)
contagem(10,0,2)

print('Contagem personalizada escolha seus numeros')
i = int(input('Escolha o inicio: '))
f = int(input('Escolha o fim: '))
p = int(input('Escolha o intervalo: '))
contagem(i,f,p)





