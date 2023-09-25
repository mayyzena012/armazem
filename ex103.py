#
def ficha(nome,gols=0):
    if nome == '':
        print(f'Jogador <desconhecido> marcou 0 gols no campeonato')
    else:
        print(f'jogador {nome} marcou {gols} gols no campeonato')
        
print('Analise do campeonato')
nom = input('Nome jogador: ')
gol = input('Quantidade de Gols: ')

ficha(nom, gol)

