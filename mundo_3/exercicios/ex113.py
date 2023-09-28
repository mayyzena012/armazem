#

def leiaInt(enter):
    entrada = input(enter)
    return int(entrada)

def leiaFloat(enter):
    entrada = input(enter)
    return float(entrada)

real = 0
while True:
    try:
        inteiro = leiaInt("Digite um numero inteiro: ")
        real = leiaFloat("Digite um numero real: ")
    except (ValueError, NameError):
        print("ERRO. Digite um numero inteiro!")\
   
    except FloatingPointError:
        print("Digite um numero real valido: ")
            
    except KeyboardInterrupt:
        print("\n Usuario nao digitou esse numero")
        print(f"Valor inteiro = {inteiro} Valor real = {real}")
        break
    else:
        print(f"Valor inteiro = {inteiro} Valor real = {real}")
        break