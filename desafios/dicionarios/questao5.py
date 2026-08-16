funcionarios = [
    {
        "id": 1,
        "nome": "Valdir",
        "cargo": "gerente"
    },

    {
        "id": 2,
        "nome": "José",
        "cargo": "suporte"
    },

    {
        "id": 3,
        "nome": "Maria",
        "cargo": "analista"
    }
]

for funcionario in funcionarios:
    print(
        "id:", funcionario["id"],
        "- nome:", funcionario["nome"],
        "- cargo", funcionario["cargo"]
    )