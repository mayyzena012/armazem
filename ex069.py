#
cont = 0
fem = 0
masc = 0
ida = 0
SEXO_MASCULINO = ('homem', 'm', 'masculino', 'h')
SEXO_FEMININO = ('mulher', 'feminino', 'f')
while True:
    idade = int(input('Digite sua idade '))
    sexo = input('Digite seu sexo ').lower()
    pergunta = input('Voce quer continuar S/N? ').upper()
    cont += 1
    if sexo in SEXO_MASCULINO:
        masc += 1
    if idade == 18:
        ida += 1
    if sexo in SEXO_FEMININO:
        if idade<20:
            fem += 1
    if pergunta == 'N':
        print('Programa encerrado.')
        print(f'Voce digitou {cont} pessoas. {masc} sao homens, {ida} tem 18 anos e {fem} mulheres tem menos de 20 anos')
        break