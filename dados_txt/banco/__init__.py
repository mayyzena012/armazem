
#arquivo = open("cadastro","x")
def abrir():
    try:
        arquivo = open("cadastro.txt","rt")
    except:
        print("erro ao abrir o arquivo")
    else:
        return print(arquivo.read())

def nome(name):
    pass

def idade(age):
    pass

