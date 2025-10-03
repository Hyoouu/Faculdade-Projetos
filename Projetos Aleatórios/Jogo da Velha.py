import random

matriz = [['' for _ in range(3)] for _ in range(3)]
for linha in matriz: 
    print(linha)

while True:
    linha = int(input("Digite a linha(de 0 a 2): "))
    coluna = int(input("Digite a coluna(de 0 a 2): "))
    if linha <0 or linha >2 or coluna <0 or coluna >2:
        print("Valor inválido, tente novamente.")
        continue
    valor = matriz[linha][coluna]
    print(valor)

    escolha2 = ['O']
    linha2 = random.randint(0, 2)
    coluna2 = random.randint(0, 2)
    valor2 = matriz[linha2][coluna2]
    print(valor2)

    if valor == '':
        matriz[linha][coluna] = "X" 
        for linha in matriz:
            print(linha)
    elif valor2 == '':
        matriz[linha2][coluna2] = "O"
        for linha in matriz:
            print(linha)

    elif valor == "X" or valor == "O": 
        print("Posição já ocupada, tente novamente.")
        