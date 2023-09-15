#35 anos de contribuicao

cadastro = dict()

print('-='*25)
print('{:^50}'.format('CADASTRO PORTAL DO TRABALHADOR'))
print('-='*25)
cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano Nascimento: '))
idade = 2023 - nasc
cadastro['idade'] = idade

cadastro['carteira'] = int(input('N Carteira de Trabalho: '))
if cadastro['carteira'] != 0:
    cadastro['contrato'] = int(input('Ano de contratacao: '))
    cadastro['salario'] = int(input('Salario: '))
else:
    print('sabonte')

con = 2023 - cadastro['contrato'] 
print(cadastro)
