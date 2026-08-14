soma = 0

while True:
    num = int(input("Digite um número (0 para parar): "))

    if num == 0:
        break

    soma = soma + num

print("Soma:", soma)