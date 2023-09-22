#exercicio 96

def linha():
    print('-'*30)


def area(largura, comprimento):
    area = largura * comprimento
    print(f'O terreno de {largura}m x {comprimento}m', end='')
    print(f' -> Tem a area do terreno de {area}m2')

linha()
print('{:^30}'.format('ANALISE DE TERRENOS'))
linha()
largura_valor = float(input('Largura(m): '))
comprimento_valor = float(input('Comprimento(m): '))
linha()
area(largura_valor, comprimento_valor)





