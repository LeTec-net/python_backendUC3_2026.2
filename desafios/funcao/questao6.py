def menu():
    while True:
        print("1 - Somar")
        print("2 - Subtrair")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            print("Você escolheu Somar.")

        elif opcao == 2:
            print("Você escolheu Subtrair.")

        elif opcao == 0:
            print("Saindo...")
            break

        else:
            print("Opção inválida.")


menu()