class pessoa:
    quantitade = 0

    def __init__(self):
        pessoa.quantidade = pessoa.quantidade + 1

pessoa1 = pessoa()
pessoa2 = pessoa()
pessoa3 = pessoa()

print(pessoa.quantidade)