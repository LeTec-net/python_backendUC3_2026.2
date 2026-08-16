nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
setor = input("Digite seu setor: ")

funcionario = {
    "nome": nome,
    "idade": idade,
    "setor": setor
}

print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Setor:", funcionario["setor"])