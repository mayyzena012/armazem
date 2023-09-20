#

aluno = dict()

aluno['nome'] = str(input('Digite o nome: ')).upper()
aluno['media'] = float(input(f'Digite a media de {aluno["nome"]}: '))

for k,v in aluno.items():
    print(f'{k} = {v}')

if aluno['media'] < 7:
    aluno['situacao'] = 'REPROVADO'
    print(f'A situacao e {aluno["situacao"]}')
else:
    aluno['situacao'] = 'APROVADO'
    print(f'A situacao e {aluno["situacao"]}')
