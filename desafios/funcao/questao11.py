def numeros_impares(n):
    for i in range(1, n + 1):

        if i % 7 == 0:
            continue

        if i % 2 != 0:
            print(i)

numero = int(input("Digite até qual número deseja contar: "))

numeros_impares(numero)