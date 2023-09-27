#minha solucao
def ficha(nome,gols=0):
    if nome == '':
        print(f'Jogador <desconhecido> marcou 0 gols no campeonato')
    else:
        print(f'jogador {nome} marcou {gols} gols no campeonato')
        
print('Analise do campeonato')
nom = input('Nome jogador: ')
gol = input('Quantidade de Gols: ')

ficha(nom, gol)


#solucao do professor
def card(player="<unknown>", goal=0):
    print(f"Player {player} scored {goal} goals in champions league")


name = str(input("Player name: "))
goals = str(input("Number of goals: "))
if goals.isnumeric():
    goals = int(goals)
else:
    g = 0
if name.strip() =="":
    card(goal=goals)
else:
    card(name,goals)

