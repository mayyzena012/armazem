def leiaInt(enter):
    while True:
        try:
            entrada = int(input(enter))
            return entrada
        except ValueError:
            print("ERRO. Digite um valor valido")
        except KeyboardInterrupt:
            print("Nada foi digitado")


def linha(tam = 40):
    return "-" * tam

def cabeca(txt):
    print(linha())
    print(txt.center(40))
    print(linha())


def menu(lista):
    cabeca("MENU")
    for posicao, item in enumerate(lista):
        print(f"{posicao+1} - {item}")
    opcao = leiaInt("Digite sua opcao: ")
    return opcao




escolha = menu(["Cadastrar Pessoas","Ver Cadastrados","Sair"])
print(escolha)