import random

matriz = [['' for _ in range(3)] for _ in range(3)]
turno = 0
rodada = 0
inicio = random.randint(0, 1)
modo = int(input("--------------------------\n1 - Jogador vs Computador\n2 - Jogador vs Jogador\nEscolha o modo de jogo: "))

print("----------------\nInício do Jogo!\n----------------")
for linha in matriz:
    print(linha)

while True:

    # ...código do modo Jogador vs Computador...
    if modo == 1:

        turno += 1
        print(f"{'-'*10}\nTurno {turno}")

        if inicio == 0:
            print("----------------\nSua vez de jogar!\n----------------")
            while True:
                try:
                    linha = int(input("Digite a linha(de 0 a 2): "))
                    coluna = int(input("Digite a coluna(de 0 a 2): "))
                except ValueError:
                    print("Valor inválido, tente novamente.")
                    continue
                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print("Valor inválido, tente novamente.")
                    continue
                if matriz[linha][coluna] == "X" or matriz[linha][coluna] == "O":
                    print("----------------\nPosição já ocupada, tente novamente.")
                elif matriz[linha][coluna] == '':
                    matriz[linha][coluna] = "X"
                    print("----------------")
                    for linha in matriz:
                        print(linha)
                    break
            if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" or \
               matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" or \
               matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" or \
               matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" or \
               matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" or \
               matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" or \
               matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" or \
               matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
                print(f"Você venceu em {rodada} rodadas!")
                break
            elif all(matriz[linha][coluna] != '' for linha in range(3) for coluna in range(3)):
                print("Deu Velha!")
                break
            inicio = 1

        elif inicio == 1:
            print("----------------\nVez do Computador!\n----------------")

            while True:
                linha2 = random.randint(0, 2)
                coluna2 = random.randint(0, 2)
                if matriz[linha2][coluna2] == "X" or matriz[linha2][coluna2] == "O":
                    print("----------------\nPosição já ocupada, tente novamente.")
                    continue
                elif matriz[linha2][coluna2] == '':
                    matriz[linha2][coluna2] = "O"
                    for linha in matriz:
                        print(linha)
                    break

            if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" or \
               matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" or \
               matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" or \
               matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" or \
               matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" or \
               matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" or \
               matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" or \
               matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
                print(f"Você perdeu em {rodada} rodadas!")
                break
            elif all(matriz[linha][coluna] != '' for linha in range(3) for coluna in range(3)):
                print("Deu Velha!")
                break
            inicio = 0

        if turno % 2 == 0:
            rodada += 1
            print(f"{'-'*10}\nRodada test{rodada}\n{'-'*10}")

    # ...código do modo Jogador vs Jogador...
    elif modo == 2:
        pass

        if inicio == 0:

            while True:
                try:
                    linha = int(input("Digite a linha(de 0 a 2): "))
                    coluna = int(input("Digite a coluna(de 0 a 2): "))
                except ValueError:
                    print("Valor inválido, tente novamente.")
                    continue
                if linha < 0 or linha > 2 or coluna < 0 or coluna > 2:
                    print("Valor inválido, tente novamente.")
                    continue
                if matriz[linha][coluna] == "X" or matriz[linha][coluna] == "O":
                    print("Posição já ocupada, tente novamente.")
                elif matriz[linha][coluna] == '':
                    matriz[linha][coluna] = "X"
                    for linha in matriz:
                        print(linha)

                    break
            if matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X" or \
               matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X" or \
               matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X" or \
               matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X" or \
               matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X" or \
               matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X" or \
               matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X" or \
               matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X":
                print(f"Você venceu em {rodada} rodadas!")
                break
            elif all(matriz[linha][coluna] != '' for linha in range(3) for coluna in range(3)):
                print("Deu Velha!")
                break
            inicio = 1

        elif inicio == 1:

            while True:
                try:
                    linha2 = int(input("Digite a linha(de 0 a 2): "))
                    coluna2 = int(input("Digite a coluna(de 0 a 2): "))
                except ValueError:
                    print("Valor inválido, tente novamente.")
                    continue
                if linha2 < 0 or linha2 > 2 or coluna2 < 0 or coluna2 > 2:
                    print("Valor inválido, tente novamente.")
                    continue
                if matriz[linha2][coluna2] == "X" or matriz[linha2][coluna2] == "O":
                    print("Posição já ocupada, tente novamente.")
                elif matriz[linha2][coluna2] == '':
                    matriz[linha2][coluna2] = "O"
                    for linha in matriz:
                        print(linha)
                    break

            if matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O" or \
               matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O" or \
               matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O" or \
               matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O" or \
               matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O" or \
               matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O" or \
               matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[2][2] == "O" or \
               matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O":
                print(f"Você perdeu em {rodada} rodadas!")
                break
            elif all(matriz[linha][coluna] != '' for linha in range(3) for coluna in range(3)):
                print("Deu Velha!")
                break
            inicio = 0

        if turno < 9:
            turno += 1
        print(f"{'-'*10}\nRodada test{rodada}\n{'-'*10}")
