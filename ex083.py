#

galera = [['yuri',19],['mayra',20],['juliano',17]]
print(galera[2][1])

for p in galera:
    print(p[0])
    print(p[1])

gal = list()
dado = list()

for a in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    gal.append(dado[:])
    dado.clear()

print(galera)
totmai = 0
totmen = 0
for p in galera:
    if p[1] >= 21:
        print(p[0])
        totmai +=1
    else:
        print(p[0])
        totmen = 0