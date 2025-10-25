import random

matriz = [['' for _ in range(3)] for _ in range(3)]
for linha in matriz: 
    print(linha)

while True:
 
 if random.randint(0, 1 ) == 0:
    while True:
     try:
      linha = int(input("Digite a linha(de 0 a 2): "))
      coluna = int(input("Digite a coluna(de 0 a 2): "))
     except ValueError:
        print("Valor inválido, tente novamente.")
        continue
     if linha <0 or linha >2 or coluna <0 or coluna >2 :
         print("Valor inválido, tente novamente.")
         continue
     if  matriz[linha][coluna] == "X" or matriz[linha][coluna] == "O": 
         print("Posição já ocupada, tente novamente.")
     elif matriz[linha][coluna] == '':
          matriz[linha][coluna] = "X" 
          for linha in matriz:
             print(linha)
          break
    if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" or\
       matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" or\
       matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" or\
       matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" or\
       matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" or\
       matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" or\
       matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" or\
       matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
       print("Você venceu!")
       break
    elif all(matriz[linha][coluna] != '' for linha in range(3) for coluna in range(3)):
        print("Deu Velha!")
        break
 else:
    while True:
     linha2 = random.randint(0, 2)
     coluna2 = random.randint(0, 2)
     if matriz[linha2][coluna2] == "X" or matriz[linha2][coluna2] == "O": 
         print("Posição já ocupada, tente novamente.")
         continue
     elif matriz[linha2][coluna2] == '':
         matriz[linha2][coluna2] = "O"
         for linha in matriz:
             print(linha)
         break

    if   matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" or\
         matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" or\
         matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" or\
         matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" or\
         matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" or\
         matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" or\
         matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" or\
         matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
         print("Você perdeu!")
         break
    elif all(matriz[linha][coluna] != '' for linha in range(3) for coluna in range(3)):
        print("Deu Velha!")
        break
     