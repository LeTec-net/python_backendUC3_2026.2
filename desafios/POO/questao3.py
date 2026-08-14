class contador:
    def __init__(self):
        self.valor = 0

    def aumentar(self):
        self.valor = self.valor + 1

    def diminuir(self):
        self.valor = self.valor - 1

contador1 = contador()

contador1.aumentar()
contador1.aumentar()
contador1.aumentar()
contador1.diminuir()

print("Contador 1:", contador1.valor)