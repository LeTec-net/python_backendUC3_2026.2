valorCompra = input("Informe o valor da compra:\n")

try:
    valor = float(valorCompra)

    if valor > 100:
        print("Desconto aplicado!")

except ValueError:
    print("Valor ivalido.")