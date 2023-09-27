#101


def voto(ano):
    global idade
    idade = 2023 - ano
    if idade == 16 or idade == 17 or idade > 70:
        return 'OPCIONAL'
    elif idade >= 18 and idade < 70:
        return 'OBRIGATORIO'
    elif idade < 16:
        return 'NEGADO'
    

print('-'*30)
ano = int(input('Digite seu ano de nasc: '))
voto(ano)
print(f'Com {idade} anos. O voto e {voto(ano)}')
print('-'*30)
print('')

