def somar():
    soma = 0

    while True:
        numero = int(input("Digite um número (0 para parar): "))

        if numero == 0:
            break

        soma += numero

    return soma


resultado = somar()

print("A soma é:", resultado)