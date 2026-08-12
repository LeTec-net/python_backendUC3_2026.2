import random

numero_secreto = random.randint(1, 100)
tentativas = 0
max_tentativas = 7

print("=== JOGO DE ADIVINHAÇÃO ===")
print("Tente descobrir a número entre 1 e 100!")
print(f"Você tem {max_tentativas} tentativas.")

while tentativas < max_tentativas:
    palpite = int(input("Digite seu palpite: "))
    tentativas += 1

    if palpite == numero_secreto:

        if tentativas == 1:
            pontos = 100

        elif tentativas == 2:
            pontos = 80

        elif tentativas == 3:
            pontos = 60

        elif tentativas == 4:
            pontos = 40

        elif tentativas == 5:
            pontos = 20

        else:
            pontos = 0


        print("Parabéns! Você acertou!")
        print(f"Você acertou em {tentativas} tentativa(s).")
        print(f"Pontuação: {pontos} pontos.")
        break

    elif palpite < numero_secreto:
        print("O número secreto é maior.")

    else:
        print("O número secreto é menor.")
        print(f"Tentativas usadas: {tentativas}")

else:
    print("\n😓 Você perdeu!")
    print(f"O número secreto era {numero_secreto}.")
    print(f"Você usou as {max_tentativas} tentativas.")    
