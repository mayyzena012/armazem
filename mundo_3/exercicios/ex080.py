#

valores = list()
for v in range(5):
    s = (int(input('Digite um valor ')))
    if v == 0 or s > valores[-1]:
        valores.append(s)
    else:
        pos = 0
        while pos < len(valores):
            if s <= valores[pos]:
                valores.insert(pos,s)
                break
            pos+=1
        