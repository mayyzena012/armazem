#aqui comca outra atividade

preco =float(input('qual preco'))

novo = preco - (preco * 5 / 100)

print(f"o valor do produto avaliado em {preco} e {novo} com 5% de desconto")

salario =float(input('qual o salario do funcionario?'))

re = salario + (salario * 5 / 100)

print(f'o salario de valor {salario} sera {re} com 15% de aumento')

dinheiro =float(input('quanto de dinheiro tem R$'))

r = dinheiro / 3.27

print(f'pode se comprar U${r:.2f} com R${dinheiro:.2f}')