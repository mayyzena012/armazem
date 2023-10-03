#exercicio 115
from banco import *
from time import sleep


while True:
    cabeca("PROGRAMA DE CADASTRO")
    sleep(1)
    escolha = opcoes(["Criar Arquivo","Cadastrar Pessoas","Pessoas Cadastradas","Sair"])


    if escolha == 1:
        print(linha())
        criarArquivo()
    elif escolha == 2:
        print("Digite Nome e Idade das pessoas a cadastrar")
        nome = leiaNome("Nome: ")
        idade = leiaIdade("Idade: ")
    elif escolha == 3:
        print("Consultando pessoas cadastradas", flush=True)
        sleep(0.5)
        print(lerArquivo())
        print(linha())
        print("Mostrando lista de pessoas cadastradas.")
    elif escolha == 4:
        print("Programa ENCERRADO.")
        break
    else:
        print("Opcão invalida. Essa não tem")