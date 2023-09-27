#35 anos de contribuicao

cadastro = dict()

print('-='*25)
print('{:^50}'.format('CADASTRO PORTAL DO TRABALHADOR'))
print('-='*25)

cadastro['nome'] = str(input('Nome: '))
nasc = int(input('Ano Nascimento: '))
cadastro['carteira'] = int(input('N Carteira de Trabalho: '))

idade = 2023 - nasc
cadastro['idade'] = idade

if cadastro['carteira'] != 0:
    ano_cadastro = int(input('Ano de contratacao: '))

    cadastro['contrato'] = ano_cadastro

    aposentadoria = ano_cadastro + 35
    aposentadoria_idade = aposentadoria - nasc

    cadastro['aposentadoria'] = aposentadoria_idade
    cadastro['salario'] = int(input('Salario: '))
else:
    print('Programa encerrado. Usuario nao possui carteira de trabalho.')

print(f'Nome: {cadastro["nome"]} com idade de {cadastro["idade"]} anos')
print(f'CTPS numero: {cadastro["carteira"]} contratado pela primeira vez em {cadastro["contrato"]}')
print(f'Com salario de: {cadastro["salario"]}')
print(f'Se aposentara em {aposentadoria} com {cadastro["aposentadoria"]} anos')


