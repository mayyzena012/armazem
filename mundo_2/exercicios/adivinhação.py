#meu jogo da adivinhação no Python!

from random import randint

num = randint(0,5)

print('jogo da advinhacao da Mayra no Python!')
resposta = int(input('descubra qual numero o computador escolheu, voce tem as opcoes de 0 a 5'))

if num==resposta:
    print('voce acertou parabens!!')
else:
    print(f'voce errou, tente novamente. eu pensei no numero {num}')


