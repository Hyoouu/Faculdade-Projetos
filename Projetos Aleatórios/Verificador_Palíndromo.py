palavra = str(input("Digite uma palavra: "))

def verificar_palindromo(palavra):
    palavra = palavra.lower()
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        print(f"É um palíndromo: {palavra_invertida}")
        return True
    else:
        print(f"Não é um palíndromo: {palavra_invertida}")
        return False

print(verificar_palindromo(palavra))
