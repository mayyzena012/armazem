#exercicio 115
from banco import *


print(lerArquivo())

while True:
    escolha = opcoes(["Criar Arquivo","Cadastrar Pessoas","Pessoas Cadastradas","Sair"])


    if escolha == 1:
        print(linha())
        criarArquivo()
        print(linha())
    elif escolha == 2:
        pass
    elif escolha == 3:
        print(lerArquivo())
    elif escolha == 4:
        break
    else:
        print("Opcão invalida. Essa não tem")