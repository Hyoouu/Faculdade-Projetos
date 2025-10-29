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



