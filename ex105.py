#socorro
def notas(*notas,situ=False):
    """
    -> Função para analisar notas e situações de alunos.
    :parem notas: recebe uma ou mais notas
    :parem situ: serve pra saber se quer que a situacao do aluno seja mostrada
    :return: vai retornar as informacoes sobre as notas
    """
    nota = {}
    nota['tam'] = len(notas)
    nota['maior_nota'] = max(notas)
    nota['menor_nota'] = min(notas)
    media = 0
    for n in notas:
        media += n
        med = media / len(notas)
    nota['media'] = med
    if situ:
        if nota['media'] >= 7:
            nota['situacao'] = 'BOA'
        elif nota['media'] == 5 or 6:
            nota['situacao'] = 'razoavel'
        else:
            nota['situacao'] = 'ruim'
    return nota




resp = notas(4.5, 4.6, 8.1, 7.5, 9.4,situ=True)
print(resp)