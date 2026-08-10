class Pessoa:
    #Atributos do objetos
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Ana",25)
p2 = Pessoa("Maria",56)

print("Idade",p2.idade)
print("Idade:",p1.idade)