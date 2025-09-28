while True:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_preferencia = int(input("Digite o ano que você quer saber sua idade: "))
    idade_correspondente = ano_preferencia - ano_nascimento

    print(f"Sua idade no ano escolhido será: {idade_correspondente} anos.")

