#exercicio 115
from banco import *



while True:
    print(linha())
    escolha = opcoes(["Criar Arquivo","Cadastrar Pessoas","Pessoas Cadastradas","Sair"])
    print(linha())


    if escolha == 1:
        print(linha())
        criarArquivo()
        print(linha())
    elif escolha == 2:
        nome = leiaNome("Nome: ")
    elif escolha == 3:
        print(linha())
        print(lerArquivo())
        print(linha())
    elif escolha == 4:
        break
    else:
        print("Opcão invalida. Essa não tem")