#

o = [388,403]

dados = dict()

pessoas = {'nome':'Guastvo','Sexo':'M','Idade':22}
print(pessoas)
print(f'{pessoas["nome"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for k in pessoas.keys():
    print(k)

for k,i in pessoas.items():
    print(f'{k} = {i}')