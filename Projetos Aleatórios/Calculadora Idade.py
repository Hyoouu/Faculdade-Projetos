while True:
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    ano_preferencia = int(input("Digite o ano que você quer saber sua idade: "))
    idade_correspondente = ano_preferencia - ano_nascimento

    if idade_correspondente < 0 :
        print("Erro: O ano de de idade estimada deve ser maior que o ano de nascimento.") 
    else:
        print(f"Sua idade no ano escolhido será: {idade_correspondente} anos.")

