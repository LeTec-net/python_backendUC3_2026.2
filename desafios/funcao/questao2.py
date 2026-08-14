def maior(a, b):
    if a > b:
        return a
    else:
        return b


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

resultado = maior(numero1, numero2)

print("O maior número é:", resultado)