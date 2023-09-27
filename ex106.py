#sistema interactive help
##
## -> essa foi minha solucao maluca e inviavel
'''''
def linhaInterativa(texto):
    tam = len(texto)
    print("~"*tam)
    print(texto)
    print("~"*tam)

def ajuda(*args):
    for arg in args:
        if arg == 'INPUT':
            linhaInterativa("\033[44m Acessando o manual do comando 'input' \033[40m")
            print(input.__doc__)
        elif arg == "LEN":
            linhaInterativa("Acessando o manual do comando 'len'")
            print(len.__doc__)
        elif arg == "PRINT":
            linhaInterativa("Acessando o manual do comando 'print'")
            print(len.__doc__)
        elif arg == "MATH":
            linhaInterativa("Acessando o manual do comando 'math'")
            import math
            print(math.__doc__)
        elif arg == "OS":
            linhaInterativa("Acessando o manual do comando 'os'")
            import os
            print(os.__doc__)
        elif arg == 'DATETIME':
            linhaInterativa("Acessando o manual do comando 'datetime'")
            import datetime
            print(datetime.__doc__)
    return args

while True:
    linhaInterativa('\033[42m SISTEMA DE AJUDA PyHelp!! \033[40m')
    escolha = str(input('-> Função ou Biblioteca: '))
    ajuda(escolha)
    print(ajuda(escolha))
    if escolha.upper() == 'FIM':
        break
'''''

#solucao do professor
cores = ('\033[m', #0 sem cor
        '\033[0;30;42m', #1 verde
        '\033[0;30;44m', #2 azul
        '\033[0;30;45m', #3 roxo
         );
def ajuda(arg):
    titulo(f"Acessando o manual \'{arg}\'", 4)
    print(cores[3])
    help(arg)
    print(cores[0], end='')

def titulo(msg,cor=0):
    tam = len(msg)
    print(cores[0], end='')
    print('='*tam)
    print(f'{msg}')
    print('='*tam)
    print(cores[0], end='')

while True:
    titulo('SISTEMA DE AJUDA PyHelp', 2)
    escolha = input("-> Funcao ou Biblioteca > ")
    if escolha.upper() == 'FIM':
        break
    else:
        ajuda(escolha)


