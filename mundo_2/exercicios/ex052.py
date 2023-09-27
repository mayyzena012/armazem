#

num = int(input('digite um numero para verificar se ele e primo'))

for a in range(1,num + 1):
    primo = num % a
    print(a)

if primo == 0:
    print(f'o numero {num} e um numero primo!')
else:
    print(f'o numero {num} nao e um numero primo')

print(primo)


frase = input('digite uma frase para verificar se um palindromo').strip().lower()

palin = frase[::-1]
print(palin)

if frase == palin:
    print('esta palavra e um palindromo')
else:
    print('esta palavra nao e um palindromo')