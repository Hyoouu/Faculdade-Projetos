# Estruturas de Dados - Listas em Python

# Estrutura - lista
array = [1,2,3,4,5,6,7,8,9,10]
def inverter_array(arr):
    array_invertido = arr[::-1]
    return array_invertido

print(inverter_array(array))

def imprimir_pares(arr):
    pares = [num for num in arr if num % 2 == 0 ]
    return pares

print(imprimir_pares(array))

def imprimir_media(arr):
    media = sum(arr)/len(arr)
    return media

print(imprimir_media(array))

def encontrar_maior_menor(arr):
    maior = max(arr)
    menor = min(arr)
    meio = len(arr) // 2
    return menor, meio, maior

print(encontrar_maior_menor(array))

array2 = [1,1,2,2,3,3,4,4,5]

def remover_duplicador(arr):
    arr_sem_duplicados = list(set(arr))
    return arr_sem_duplicados

print(remover_duplicador(array2))

#Estrutura - Tupla

tupla = ("Nome", "Gustavo", "Idade", 25, "Cidade", "São Paulo")

def acessar_tupla(tupla):
    nome = tupla[0:2]
    idade = tupla[2:4]
    cidade = tupla[4:6]
    return nome, idade, cidade

print(acessar_tupla(tupla))

# Estrutura - Dicionário

# Dicionário com 3 chaves (Nome, Nota, Idade) e cada chave tem uma tupla com 3 valores
dict = {"Nome": ("Gustavo", "Ana", "Carlos"), "Nota": (9.5, 8.0, 7.5), "Idade": (25, 22, 23)}

def acessar_dicionario(dicionario):
    # Extrai as tuplas do dicionário para variáveis separadas
    nomes = dicionario["Nome"]    # Pega a tupla de nomes: ("Gustavo", "Ana", "Carlos")
    notas = dicionario["Nota"]    # Pega a tupla de notas: (9.5, 8.0, 7.5)
    idades = dicionario["Idade"]  # Pega a tupla de idades: (25, 22, 23)

    dados_separados = []  # Lista vazia para armazenar os dicionários de cada pessoa
    for i in range(len(nomes)):  # Loop que vai de 0 até o tamanho da tupla de nomes (3)
        pessoa = {  # Cria um dicionário para cada pessoa com seus dados
            "Nome": nomes[i],   # Pega o nome na posição i da tupla de nomes
            "Nota": notas[i],   # Pega a nota na posição i da tupla de notas
            "Idade": idades[i]  # Pega a idade na posição i da tupla de idades
        }
        dados_separados.append(pessoa)  # Adiciona o dicionário da pessoa na lista
    return dados_separados  # Retorna a lista com os dicionários de todas as pessoas

# Imprime cada pessoa em uma linha separada
pessoas = acessar_dicionario(dict)
for pessoa in pessoas:
    print(pessoa)
