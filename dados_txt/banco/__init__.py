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
        

def criarArquivo():
    try:
        arquivo = open(arq,"wt+")
        print("Arquivo criado com sucesso")
        arquivo.close()
    except:
        print("Houve um erro ao criar o arquivo")

def lerArquivo():
    try: 
        arquivo = open(arq, "rt")
        cabeca("PESSOAS CADASTRADAS")
        lista = arquivo.read()
        return lista
    except:
        print("ERRO ao abrir o arquivo")

def opcoes(lista):
    for posicao, objeto in enumerate(lista):
        print(f"{posicao + 1} - {objeto}")
    print(linha())
    escolha = leiaInt("Sua opcão: ")
    print(linha())
    return escolha

    