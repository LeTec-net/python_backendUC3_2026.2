class aluno:
    def __init__(self, nome):
        self.nome = nome

    def estudar(self):
        print("O aluno está estudando.")

aluno1 = aluno("João")

print(aluno1.nome)
aluno1.estudar()