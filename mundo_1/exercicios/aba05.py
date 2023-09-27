#outras linhas


#print('\033[4;36mola mundo\033]m')
rodando = True
while rodando:

    valorcasa = float(input('qual o valor da casa que voce deseja?'))
    salario = float(input('qual seu salario?'))
    anos = int(input('em quantos anos voce quer pagar a casa?'))

    excedente = salario * 30 / 100
    meses = anos * 12 
    prestacao = valorcasa / meses

    if prestacao>excedente:
        print('EMPRESTIMO NEGADO!')
        rodando = False
    else:
        print(f'A prestacao mensal a ser paga sera de R${prestacao:.2f} em {anos} ano(s) durante {meses} meses(s)')
        rodando = False

