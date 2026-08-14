produtos = {
    "1": {
        "nome": "Espada de Ferro",
        "preco": 500,
        "categoria": "Arma",
        "lendario": False
    },

    "2": {
        "nome": "Arco Élfico",
        "preco": 800,
        "categoria": "Arma",
        "lendario": False
    },

    "3": {
        "nome": "Poção de Vida",
        "preco": 100,
        "categoria": "Poção",
        "lendario": False
    },

    "4": {
        "nome": "Escudo do Guardião",
        "preco": 700,
        "categoria": "Armadura",
        "lendario": False
    },

    "5": {
        "nome": "Excalibur",
        "preco": 5000,
        "categoria": "Arma",
        "lendario": True
    },

    "6": {
        "nome": "Livro de magia das trevas",
        "preco": 10000,
        "categoria": "Magia",
        "lendario": True
    }
}

inventario = {}
saldo = 5200

while True:

    print("\n=== LOJA DE RPG ===")
    print("1 - Ver produtos")
    print("2 - Consultar produto")
    print("3 - Comprar")
    print("4 - Vender item")
    print("5 - Ver inventário")
    print("6 - Ver saldo")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    # VER PRODUTOS
    if opcao == "1":

        print("\n--- PRODUTOS ---")

        for codigo, produto in produtos.items():

            if produto["lendario"]:
                tipo = "⭐ LENDÁRIO"
            else:
                tipo = ""

            print(
                f"{codigo} - {produto['nome']} | "
                f"R$ {produto['preco']:.2f} | "
                f"{produto['categoria']} {tipo}"
            )

    # CONSULTAR PRODUTO
    elif opcao == "2":

        codigo = input("Digite o código do produto: ")

        if codigo in produtos:

            produto = produtos[codigo]

            print(f"\nNome: {produto['nome']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print(f"Categoria: {produto['categoria']}")

            if produto["lendario"]:
                print("⭐ Este é um item LENDÁRIO!")

        else:
            print("Produto inexistente.")

    # COMPRAR
    elif opcao == "3":

        codigo = input("Digite o código do produto: ")

        if codigo not in produtos:

            print("Produto inexistente.")

        else:

            produto = produtos[codigo]

            quantidade = int(input("Digite a quantidade: "))

            preco_total = produto["preco"] * quantidade

            # DESCONTO
            if quantidade >= 5:
                desconto = preco_total * 0.10
                preco_final = preco_total - desconto

                print("Desconto de 10% aplicado!")

            else:
                preco_final = preco_total

            if saldo >= preco_final:

                saldo -= preco_final

                if codigo in inventario:
                    inventario[codigo]["quantidade"] += quantidade

                else:
                    inventario[codigo] = {
                        "nome": produto["nome"],
                        "quantidade": quantidade
                    }

                print(f"Você comprou {quantidade}x {produto['nome']}.")
                print(f"Valor da compra: R$ {preco_final:.2f}")
                print(f"Saldo restante: R$ {saldo:.2f}")

            else:

                print("Saldo insuficiente.")

    # VENDER
    elif opcao == "4":

        codigo = input("Digite o código do item que deseja vender: ")

        if codigo not in inventario:

            print("Você não possui esse item.")

        else:

            quantidade = int(input("Quantidade para vender: "))

            if quantidade <= inventario[codigo]["quantidade"]:

                produto = produtos[codigo]

                valor_venda = produto["preco"] * quantidade * 0.70

                saldo += valor_venda

                inventario[codigo]["quantidade"] -= quantidade

                print(f"Você vendeu {quantidade}x {produto['nome']}.")
                print(f"Você recebeu: R$ {valor_venda:.2f}")

                if inventario[codigo]["quantidade"] == 0:
                    del inventario[codigo]

            else:

                print("Você não possui essa quantidade.")

    # INVENTÁRIO
    elif opcao == "5":

        print("\n=== INVENTÁRIO ===")

        if len(inventario) == 0:

            print("Seu inventário está vazio.")

        else:

            for codigo, item in inventario.items():

                print(
                    f"{item['nome']} - "
                    f"Quantidade: {item['quantidade']}"
                )

    # SALDO
    elif opcao == "6":

        print(f"\nSeu saldo: R$ {saldo:.2f}")

    # SAIR
    elif opcao == "7":

        print("Até a próxima aventura!")
        break

    else:

        print("Opção inválida.")                      