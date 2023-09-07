#

colocados = ('Botago','Palmeiras','Gremio','Flamengo','Fluminense','Bragantino','Atletico PR','Fortaleza','Atletico MG','Cuiaba','Sao Paulo','Cruzeiro','Corinthians','Internacional','Goias','Bahia','Santos','Vasco','America mg','Coritiba')

print(f'os cinco primeiros colocados sao {colocados[0:5]}')
print('-'*100)
print(f'os times que estao na zona de rabaixamento sao {colocados[16:]}')
print('-'*100)
print(sorted(colocados))
print('-'*100)
index = colocados.index('Santos')
print(f'O time do Santos esta na colocao {index}')