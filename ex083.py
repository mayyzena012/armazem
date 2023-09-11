#

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
        