#area de testes

lanche = ('hamburguer','suco','pudim', 'sorvete')
print(lanche[1])

for a in lanche:
    print(a)

for cont in range(0,len(lanche)):
    print(f'eu vou comer {lanche[cont]}')

for pos, comida in enumerate(lanche):
    print(f'eeu vou comer {comida} na posicao {pos}')

print(sorted(lanche))

a = (1,2,4)
b = (2,5,6)
c = a+b
print(c)
print(c.count(5))
print(c.index(5))