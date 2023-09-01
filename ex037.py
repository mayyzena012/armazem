#exercicio 37
#escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversao, 1 para binario, 2 para octal e 3 para hexadecimal

num = int(input('digite um numero'))
escolha = int(input('digite \n 1 para converter este numero em binario \n 2 para converter em octal \n 3 para converter em hexadecimal').strip())

if escolha == 1:
    numero_binario = bin(num)[2:]
    print(numero_binario)
elif escolha == 2:
    numero_octal = oct(num)[2:]
    print(numero_octal)
elif escolha == 3:
    numero_hexa = hex(num)[2:]
    print(numero_hexa)
else:
    print('numero invalido tente novamente')


