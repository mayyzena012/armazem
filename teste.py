def calcular_area(comprimento, largura):
    area = comprimento * largura


comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))
largura_terreno = float(input("Digite a largura do terreno em metros: "))

resultado = calcular_area(comprimento_terreno, largura_terreno)

print(f"A área do terreno é {resultado} metros quadrados.")
