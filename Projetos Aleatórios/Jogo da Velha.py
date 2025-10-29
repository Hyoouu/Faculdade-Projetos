import random

matriz = [['' for _ in range(3)] for _ in range(3)]
turno = 0
rodada = 0
inicio = random.randint(0, 1)
fim_jogo = False  # Variável para controlar o fim do jogo
modo = int(input("--------------------------\n1 - Jogador vs Computador\n2 - Jogador vs Jogador\nEscolha o modo de jogo: "))
def verificar_vitoria(simbolo):

    # Verificar linhas horizontais
    for i in range(3):
        if matriz[i][0] == simbolo and matriz[i][1] == simbolo and matriz[i][2] == simbolo:
            return True

    # Verificar linhas verticais
    for i in range(3):
        if matriz[0][i] == simbolo and matriz[1][i] == simbolo and matriz[2][i] == simbolo:
            return True

    # Verificar diagonal principal
    if matriz[0][0] == simbolo and matriz[1][1] == simbolo and matriz[2][2] == simbolo:
        return True

    # Verificar diagonal secundária
    if matriz[0][2] == simbolo and matriz[1][1] == simbolo and matriz[2][0] == simbolo:
        return True

    return False

def verificar_velha():
    return all(matriz[i][j] != '' for i in range(3) for j in range(3))

print(f"{'-'*10}\nInício do Jogo!\n{'-'*10}")
for linha in matriz:
    print(linha)

while True:
    if fim_jogo:  # Se o jogo acabou, sai do loop principal
        break

    # ...código do modo Jogador vs Computador...
    if modo == 1:
        turno += 1
        print(f"{'-'*10}\nTurno {turno}")

        if inicio == 0:
            print(f"{'-'*10}\nSua vez de jogar!\n{'-'*10}")
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
                    print(f"{'-'*10}\nPosição já ocupada, tente novamente.")
                    continue
                elif matriz[linha][coluna] == '':
                    matriz[linha][coluna] = "X"
                    print("----------------")
                    for linha in matriz:
                        print(linha)
                    if verificar_vitoria("X"):
                        print(f"{'-'*10}\nVocê venceu em {rodada} rodadas!\n{'-'*10}")
                        fim_jogo = True  # Marca o fim do jogo
                        break
                    if verificar_velha():
                        print(f"{'-'*10}\nDeu Velha!\n{'-'*10}")
                        fim_jogo = True  # Marca o fim do jogo
                        break
                    break  # Sai do loop apenas para passar a vez
            if not fim_jogo:  # Só muda o início se o jogo não acabou
                inicio = 1

        elif inicio == 1:
            print(f"{'-'*10}\nVez do Computador!\n{'-'*10}")
            while True:
                linha2 = random.randint(0, 2)
                coluna2 = random.randint(0, 2)
                if matriz[linha2][coluna2] == "X" or matriz[linha2][coluna2] == "O":
                    continue
                elif matriz[linha2][coluna2] == '':
                    matriz[linha2][coluna2] = "O"
                    for linha in matriz:
                        print(linha)
                    if verificar_vitoria("O"):
                        print(f"{'-'*10}\nVocê perdeu em {rodada} rodadas!\n{'-'*10}")
                        fim_jogo = True  # Marca o fim do jogo
                        break
                    if verificar_velha():
                        print(f"{'-'*10}\nDeu Velha!\n{'-'*10}")
                        fim_jogo = True  # Marca o fim do jogo
                        break
                    break  # Sai do loop apenas para passar a vez
            if not fim_jogo:  # Só muda o início se o jogo não acabou
                inicio = 0

        if turno % 2 == 0:
            rodada += 1
            if not fim_jogo:
                print(f"{'-'*10}\nRodada {rodada}")

    # ...código do modo Jogador vs Jogador...
    elif modo == 2:
        turno += 1
        print(f"{'-' * 10}\nTurno {turno}")

        if inicio == 0:
            print(f"{'-' * 10}\nVez do Jogador 1!\n{'-' * 10}")
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
                    print(f"{'-'*10}\nPosição já ocupada, tente novamente.")
                    continue
                elif matriz[linha][coluna] == '':
                    matriz[linha][coluna] = "X"
                    for linha in matriz:
                        print(linha)
                    if verificar_vitoria("X"):
                        print(f"{'-'*10}\nJogador 1 venceu em {rodada} rodadas!")
                        fim_jogo = True
                        break
                    if verificar_velha():
                        print(f"{'-'*10}\nDeu Velha!")
                        fim_jogo = True
                        break
                    break
            if not fim_jogo:
                inicio = 1

        elif inicio == 1:
            print(f"{'-' * 10}\nVez do Jogador 2!\n{'-' * 10}")
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
                    print(f"{'-'*10}\nPosição já ocupada, tente novamente.")
                    continue
                elif matriz[linha2][coluna2] == '':
                    matriz[linha2][coluna2] = "O"
                    for linha in matriz:
                        print(linha)
                    if verificar_vitoria("O"):
                        print(f"{'-'*10}\nJogador 2 venceu em {rodada} rodadas!")
                        fim_jogo = True
                        break
                    if verificar_velha():
                        print(f"{'-'*10}\nDeu Velha!")
                        fim_jogo = True
                        break
                    break
            if not fim_jogo:
                inicio = 0

        if turno % 2 == 0:
            rodada += 1
            print(f"{'-' * 10}\nRodada {rodada}")
