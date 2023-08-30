#iniciando 

nome = str(input('digite seu nome para ser analisado')).strip()

print('analisano seu nome')
print(f'seu nome com maisculas e{nome.upper()}')
print(f'seu nome com minusculas e{nome.lower()}')
print('seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('seu primeiro nome tem ao todo {} letras'.format(nome.find(' ')))

cid = str(input('qual sua cidade de nascimento?')).strip()
print(cid[:5].upper() == 'SANTO')

nom = str(input('digite seu nome completo:')).strip()
print('seu nome tem silva {}'.format('silva' in nom.lower()))

a = str(input('digite uma frase qualquer:')).upper().strip()
print('a letra a aparece {} vezes'.format(a.count('A')))
print('a letra a aparece na posicao {} pela primeria vez'.format(a.find('A')))
print('a letra a aparece na posicao {} pela ultima vez'.format(a.rfind('A')+1))

nome1 = str(input('digite seu nome completo para ser analisado:')).strip()
m = nome1.split()
print(f'seu primeiro nome e {m[0]}')
print(f'seu segundo nome e {m[-1]}')
