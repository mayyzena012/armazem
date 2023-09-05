#
tabuada = 0
while True:
    num = int(input('Digite um numero para ver sua tabuada '))
    if num<=-1:
        break
    else:
        for a in range(1,10 +1):
            tabuada = num * a
            print(f'|{num} x {a} = {tabuada}|')

print('acabou')