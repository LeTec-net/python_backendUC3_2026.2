dia = input("Digite um dia da semana: ").lower()

match dia:
    case "segunda":
        print("Dia de semana")
    case "terça":
        print("Dia de semana")
    case "quarta":
        print("Dia de semana")
    case "quinta":
        print("Dia de semana")
    case "sexta":
        print("Dia de semana")
    case "sábado":
        print("Final de semana")
    case "domingo":
        print("Final de semana")
    case _:
        print("Dia inválido")