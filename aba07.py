#

o = [388,403]

dados = dict()

pessoas = {'nome':'Guastvo','Sexo':'M','Idade':22}
print(pessoas)
print(f'{pessoas["nome"]}')
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

pessoas['nome'] = 'Leandro'
pessoas['peso'] = 65

for k in pessoas.keys():
    print(k)

for k,i in pessoas.items():
    print(f'{k} = {i}')

pessoas.copy()

estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('unidade federativa: '))
    estado['silga'] = str(input('sigla do estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'{k} = {v}')