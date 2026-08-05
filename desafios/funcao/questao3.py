def fatorial(numero):
    resultado = 1
    #multiplica de 1 até numero
    for i in range(1,numero+1):
        resultado *= i
    return resultado

#teste
print(fatorial(8))
print(fatorial(2))
print(fatorial(50))