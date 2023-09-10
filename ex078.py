#
valores = list()
for a in range(5):
    valores.append(int(input(f'digite um valor para posicao {a} ')))

print(f'O maior valor digitado foi {max(valores)} na posicao ', end=' ')
for p,v in enumerate(valores):
    if v == max(valores):
        print(f'{p}...', end=' ')

print(f'\n O menor valor digitado foi {min(valores)} na posicao ', end=' ')
for p,v in enumerate(valores):
     if v == min(valores):
        print(f'{p}...', end=' ')
