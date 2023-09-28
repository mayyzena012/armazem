#funções

def aumentar(value=0, aumentu=0,show=True):
    au = value + (value * aumentu / 100)
    if show:
        return raio_moedizador(au)
    return au

def diminuir(value, diminui,show=True):
    di = value - (value * diminui / 100)
    if show:
        return raio_moedizador(di)
    return di

def dobro(value,show=True):
    do = value * 2
    if show:
        return raio_moedizador(do)
    return do

def metade(value,show=True):
    me = value / 2
    if show:
        return raio_moedizador(me)
    return me

def raio_moedizador(value,moeda="R$"):
    return f"{moeda}{value:.2f}".replace(".",",")

def leiaDinheiro(enter):
    validacao = False
    while not validacao:
        entrada = input(enter).replace(",",".")
        if entrada.isalpha() or entrada == " ":
            print(f"\033[31m{entrada} nao e valido, digite um valor\033[33m")
        else:
            validacao = True
            return float(entrada)
