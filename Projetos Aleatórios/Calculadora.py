
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b


if  a < 0 or b < 0 :
    print("Erro: Valores negativos não são permitidos.")
else:
    print(soma)
    print(subtracao)
    print(multiplicacao)
    print(divisao)