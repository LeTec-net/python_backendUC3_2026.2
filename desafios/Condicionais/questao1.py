login = input("Digite seu login:\n")
senha = input("Digite sua senha:\n")

if login == "admin" and senha == "123456":
    print("Acesso permitido")
else:
    print("Acesso negado, login ou senha incorretos")

