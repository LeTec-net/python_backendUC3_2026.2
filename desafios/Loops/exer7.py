numeros = [-1, 2, -3, 4]
soma = 0

for n in numeros:
    if n < 0:
        continue

    soma = soma + n

print("Soma:", soma)