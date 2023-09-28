import dado

def resumo(value, aumento, diminui):
    print('-'*40)
    print(f"Preco analisado:\t{dado.raio_moedizador(value)}")
    print(f"Dobro do preco:\t\t{dado.dobro(value)}")
    print(f"Metade do preco:\t{dado.metade(value)}")
    print(f"{aumento} de aumento:\t\t{dado.aumentar(value, aumento)}")
    print(f"{diminui} de reducao:\t\t{dado.diminuir(value, diminui)}")
    print('-'*40)