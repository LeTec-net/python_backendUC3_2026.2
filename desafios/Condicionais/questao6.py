estoque = int(input("Quantidade disponível: "))
pedido = int(input("Quantidade pedida: "))

if pedido > estoque:
    print("Estoque insuficiente.")
else:
    print("Pedido confirmado.")