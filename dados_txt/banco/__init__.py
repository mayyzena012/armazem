from time import sleep

arq = "dados_txt/banco/cadastro.txt"

def linha(tam = 40):
    return "~" * tam

def cabeca(txt):
    print(linha())
    print(txt.center(40))
    print(linha())

def leiaInt(enter):
    while True:
        try:
            entrada = int(input(enter))
            return entrada
        except ValueError:
            print("ERRO. Insira um valor valido")
        except KeyboardInterrupt:
            print("\n O usuario não escolheu nada")
            return 4

def leiaNome(enter):
    try:
        entrada = str(input(enter))
    except ValueError:
        print("ERRO. Digite um nome valido")
    except KeyboardInterrupt:
        print("Erro")
    arquivo = open(arq, "a")
    arquivo.writelines(f"\n {entrada}")
    arquivo.close()
    return entrada

def leiaIdade(enter):
    try:
        entrada = int(input(enter))
    except:
        print("ERRO. Digie um valor valido")
    try:
        idade = str(entrada)
        arquivo = open(arq, "a")    
        arquivo.write(f" {idade:>10} anos")
        #return idade
    except:
        print("Erro. Invalido")
       

def criarArquivo():
    try:
        arquivo = open(arq,"wt+")
        sleep(1)
        print("Arquivo criado com sucesso")
        arquivo.close()
    except:
        print("Houve um erro ao criar o arquivo")

def lerArquivo():
    try: 
        arquivo = open(arq, "rt")
        cabeca("PESSOAS CADASTRADAS")
        sleep(0.5)
        lista = arquivo.read()
        return lista
    except:
        print("ERRO ao abrir o arquivo")

def escreverArquiv():
    try:
        arquivo = open(arq, "wt")
    except:
        print("ERRO ao escrever no arquivo")

def opcoes(lista):
    for posicao, objeto in enumerate(lista):
        print(f"{posicao + 1} - {objeto}")
    escolha = leiaInt("Sua opcão: ")
    return escolha

    