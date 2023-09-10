#

prod = ('Microondas', 1200.95, 'Televisao', 2530.30,'Videogame', 4500.99, 'Sapato', 57.43, 'Saboneteira', 2.56)


print('-'*50)
print('{:^50}'.format('LISTA DE COMPRAS'))
print('-'*50)
print(f'{prod[0]:.<30}R${prod[1]}')
print(f'{prod[2]:.<30}R${prod[3]}')
print(f'{prod[4]:.<30}R${prod[5]}')
print(f'{prod[6]:.<30}R${prod[7]}')
print(f'{prod[8]:.<30}R${prod[9]}')


p = ('SABONETE','CIRURGIAO','MAIZENA','FUTEBOL','ENTORPECENTE','GIGATONICO','PROGRAMADOR','CONVERSAR','ESTUDANDO')
print(p)

for a in p:
    print(f'na palavra {a} temos')
    for letra in a:
        if letra.lower() in 'aeiou':
            print(letra, end= ' ')
