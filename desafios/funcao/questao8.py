def contar_pares(inicio, fim):
    quantidade = 0

    for i in range(inicio, fim + 1):
        if i % 2 == 0:
            quantidade += 1

    return quantidade

print(contar_pares(1, 20))