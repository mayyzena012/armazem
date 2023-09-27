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

print('='*30)
#listas
num = [1,2,5,6,7]
num[2] = 3
num.append(8)
num.sort
num.sort(reverse=True)
num.insert(4,12)
num.pop(1)
num.remove(2)
print(num)
print(f'a lista tem {len(num)} elementos')

valores = []
valores.append(12)
valores.append(5)
valores.append(6)

for p, v in enumerate(valores):
    print(f'Encontrei o valor {v} na posicao {p}')

val = list()
for w in range(0,5):
    val.append(int(input('Digite valor: ')))
    print(val)

a = [1,2,3,4,5]
b = a[:]
b[2] = 12
print(a)
print(b)

#lista parte 2

galera = [['yuri',19],['mayra',20],['juliano',17]]
print(galera[2][1])

for p in galera:
    print(f'nome {p[0]}')
    print(f'idade {p[1]}')

gal = list()
dado = list()

for a in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gal.append(dado[:])
    dado.clear()

print(gal)
totmai = 0
totmen = 0
for a in gal:
    if a[1] >= 21:
        print(f'pessoas com mais {a[0]} 21')
        totmai +=1
    else:
        print(f'{a[0]} pessoas com menos de 21')
        totmen = 0


