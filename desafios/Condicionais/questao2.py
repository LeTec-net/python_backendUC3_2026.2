
idade = input("Digite sua idade:\n")

try:
    idade = int(idade)
    if idade < 0:
        print("idade invalida!Por favor, insira um número positivo.")
    elif idade < 18:
        print("Você não pode acessar esse conteúdo!")
    else:
        print("Seja bem vindo, acesso liberado!")
except ValueError:
    print("Entrada inválida.Por favor, insira um número inteiro.")
#exe 2
try:
    numero = int(input("Digite um numero:"))
    print(100/numero)
except ZeroDivisionError:
    print("Digite um número diferente de zero.")
except ValueError:
    print("Digite qualquer número, não texto!!")
'''