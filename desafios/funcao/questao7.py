def validar_senha():
    senha = input("Digite a senha: ")

    while senha != "python123":
        print("Senha incorreta.")
        senha = input("Digite a senha novamente: ")

    print("Senha correta! Acesso permitido.")

validar_senha()    