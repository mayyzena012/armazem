#
soma = 0
maior = 0
menor = 0
cont = 0
maior_idade_homem = 0
nome_maior_idade = 0

SEXO_MASCULINO = ('homem', 'm', 'masculino', 'h')
SEXO_FEMININO = ('mulher', 'feminino', 'f')
for a in range(4):
    print(f'---- {a} PESSOA ----')
    nome = input('nome:').strip().lower()
    idade = int(input('idade: '))
    sexo = input('SEXO - F/M: ').strip().lower()
    soma += idade
    if a == 0 and sexo in SEXO_MASCULINO:
        maior_idade_homem = idade
        nome_maior_idade = nome
    if sexo in SEXO_MASCULINO and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_maior_idade = nome
    if sexo in SEXO_FEMININO and idade<20:
        cont += 1 

print(f'o mais velho entre homens tem {maior_idade_homem} e seu nome {nome_maior_idade}')
print(f'existem {cont} mulheres com menos de 20')

media = soma / 4
print(media)

