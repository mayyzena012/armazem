#


soma = cont = media = 0
resposta = 'S'

while resposta in 'Ss':
    num = int(input('digite um numero '))
    resposta = input('voce quer digitar mais algum numero S/N? ').upper()[0]
    cont += 1
    media += num
    if resposta == 'N':
        print('encerrado')
        print(f'')
        print(media)
        
    
