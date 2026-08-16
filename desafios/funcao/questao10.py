def login():
    tentativas = 0

    while tentativas < 3:
        senha = input("Digite a senha: ")

        if senha == "senha123":
            print("Login realizado com sucesso!")
            return
        else:
            print("Senha incorreta.")
            tentativas += 1

    print("Número máximo de tentativas atingido.")

login()