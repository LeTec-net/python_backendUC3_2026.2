class livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True

livro1 = livro("Jogos Vorazes")

print(livro1.titulo)
print(livro1.disponivel)