#
valores = list()
for a in range(5):
    valores.append(int(input(f'digite um valor para posicao {a} ')))

print(f'O maior valor digitado foi {max(valores)} na posicao {valores.index(max(valores))}')
print(f'O menor valor digitado foi {min(valores)} na posicao {valores.index(min(valores))}')