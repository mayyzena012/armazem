#


sexo = input('digite seu sexo F/m: ').strip().upper()
while sexo not in 'MF':
    sexo = input('Valor invalido digite novamente')


print(f'voce escolheu o sexo {sexo} validado com sucesso')