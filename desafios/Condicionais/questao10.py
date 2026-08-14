print("1 - Opção 1")
print("2 - Opção 2")
print("3 - Opção 3")
print("4 - Opção 4")
print("5 - Opção 5")

escolha = int(input("Escolha uma opção de 1 a 5: "))

if escolha >= 1 and escolha <= 5:
    print("Número escolhido:", escolha)
else:
    print("Opção inválida.")