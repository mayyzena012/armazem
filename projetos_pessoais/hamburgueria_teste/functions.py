#todos os defs


pedido_cancelado = True

def escolha_burger():
    global pedido_cancelado
    hamburger_escolha = ''
    while hamburger_escolha == '':
        escolha = int(input('''Escolha um hamburguer do nosso cardápio: 
        \n [1] X Burger Tradicional \n [2] X Salada \n [3] X Burger Cheddar \n [4] X burger Bacon \n [5] X Burger Duplo \n [6] Encerrar '''))
        if escolha == 1:
            hamburger_escolha = 'X Burger Tradicional'
        elif escolha == 2:
            hamburger_escolha = 'X Salada'
        elif escolha == 3:
            hamburger_escolha = 'X Burger Cheddar'
        elif escolha == 4:
            hamburger_escolha = 'X Burger Bacon'
        elif escolha == 5:
            hamburger_escolha = 'X Burger Duplo'
        elif escolha == 6:
            pedido_cancelado = False
            break
    return hamburger_escolha

def escolha_molho():
    global pedido_cancelado
    if not pedido_cancelado:
        return ''
    molho_escolha = ''
    while molho_escolha == '':
        molho = int(input('Escolha seu molho \n [1] Molho verde \n [2] Molho Bacon \n [3] Molho Especial \n [4] Sem molho '))
        if molho == 1:
            molho_escolha = 'Molho verde'
        elif molho == 2:
            molho_escolha = 'Molho Bacon'
        elif molho == 3:
            molho_escolha = 'Molho Especial'
        elif molho == 4:
            molho_escolha = 'Sem molho'
    return molho_escolha

def escolha_bebida():
    global pedido_cancelado
    if not pedido_cancelado:
        return ''
    bebida_escolha = ''
    while bebida_escolha == '':
        bebida = int(input('Escolha sua bebida \n [1] Guarana \n [2] Coca Cola \n [3] Sukita \n [4] Suco natural \n [5] Sem bebida '))
        if bebida == 1:
            bebida_escolha = 'Guarana'
        elif bebida == 2:
            bebida_escolha = 'Coca Cola'
        elif bebida == 3:
            bebida_escolha = escolha_sukita()
        elif bebida == 4:
            bebida_escolha = escolha_suco()
        elif bebida == 5:
            bebida_escolha = 'Sem bebida'
    return bebida_escolha

def escolha_sukita():
    sukita_escolha = ''
    while sukita_escolha == '':
        sukita = int(input('Escolha sua Sukita \n [1] Sukita Laranja \n [2] Sukita Uva '))
        if sukita == 1:
            sukita_escolha = 'Sukita Laranja'
        elif sukita == 2:
            sukita_escolha = 'Sukita Uva'
    return sukita_escolha


def escolha_suco():
    suco_escolha = ''
    while suco_escolha == '':
        suco = int(input('Escolha seu suco natural \n [1] Suco de Abacaxi \n [2] Suco de Laranja \n [3] Suco de Goiaba \n [4] Suco de Uva \n [5] Suco de Caju '))
        if suco == 1:
            suco_escolha = 'Suco de Abacaxi'
        elif suco == 2:
            suco_escolha = 'Suco de Laranja'
        elif suco == 3:
            suco_escolha = 'Suco de Goiaba'
        elif suco == 4:
            suco_escolha = 'Suco de Uva'
        elif suco == 5:
            suco_escolha = 'Suco de Caju'
    return suco_escolha