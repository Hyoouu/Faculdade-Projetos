import random

matriz = [['' for _ in range(3)] for _ in range(3)]
for linha in matriz: 
    print(linha)

while True:
    while True:
     linha = int(input("Digite a linha(de 0 a 2): "))
     coluna = int(input("Digite a coluna(de 0 a 2): "))
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
    if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" :
          print("Você venceu!")
          break
    
    while True:
     linha2 = random.randint(0, 2)
     coluna2 = random.randint(0, 2)
     if linha2 <0 or linha2 >2 or coluna2 <0 or coluna2 >2 :
         print("Valor inválido, tente novamente.")
     if matriz[linha2][coluna2] == "X" or matriz[linha2][coluna2] == "O": 
         print("Posição já ocupada, tente novamente.")
         continue
     if matriz[linha2][coluna2] == '':
         matriz[linha2][coluna2] = "O"
         for linha in matriz:
             print(linha)
         break
     
     if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" :
          print("Você venceu!")
          break
    