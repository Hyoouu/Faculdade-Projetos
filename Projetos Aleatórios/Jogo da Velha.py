import random

matriz = [['' for _ in range(3)] for _ in range(3)]
for linha in matriz: 
    print(linha)

while True:
    linha = int(input("Digite a linha(de 0 a 2): "))
    coluna = int(input("Digite a coluna(de 0 a 2): "))
    if linha <0 or linha >2 or coluna <0 or coluna >2 :
        print("Valor inválido, tente novamente.")
        continue
    valor = matriz[linha][coluna]
    print(valor)

    if valor == '':
        matriz[linha][coluna] = "X" 
        for linha in matriz:
            print(linha)


    escolha2 = ['O']
    linha2 = random.randint(0, 2)
    coluna2 = random.randint(0, 2)
    valor2 = matriz[linha2][coluna2]
    print(valor2)
    if valor2 == '':
        matriz[linha2][coluna2] = "O"
        for linha in matriz:
            print(linha)

    if valor == "X" or valor == "O": 
        print("Posição já ocupada, tente novamente.")

    vitoria = matriz[0][0] and matriz[0][1] and matriz[0][2] == ("X", "O") 

    if  matriz == vitoria: 
         print("Deu velha!")
         break
    
        