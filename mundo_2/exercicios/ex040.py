#


nota1 = float(input('digite sua nota em portugues'))
nota2 = float(input('digite sua nota em espanhol'))

media = (nota1+nota1) / 2

if media<5.0:
    print(f'sua media foi {media} VOCE FOI REPROVADO!! BURRO!')
elif media<=6.9:
    print(f'sua media foi de {media} voce esta de RECUPERACAO, melhore!')
else:
    print(f'parabens sua media foi {media} voce foi APROVADO!! Continue assim!')

