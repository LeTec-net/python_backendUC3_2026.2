class produto:
    def __init__(self, preco):
        self.preco = preco

    def aplicar_desconto(self,percentual):
        self.preco = self.preco - (self.preco * percentual / 100)

produto1 = produto(100)
produto1.aplicar_desconto(10)

print(produto1.preco)