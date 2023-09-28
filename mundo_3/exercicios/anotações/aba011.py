#anotacoes do ultimo bloco de python

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print(f"Infelizmente tivemos um problema {erro.__class__}")
else:
    print(f"O resultado e{r}")
finally:
    print("volte sempre, tudo certo.")
