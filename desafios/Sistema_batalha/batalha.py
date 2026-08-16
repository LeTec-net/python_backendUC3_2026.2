import random

def calcular_dano(ataque, defesa):
    dano = ataque - defesa

    if dano <= 0:
        dano = 0

    # Dano aleatório
    dano = random.randint(dano - 3, dano + 3)

    if dano < 0:
        dano = 0

    return dano

def atacar(atacante, defensor):

    # Chance de esquiva
    esquiva = random.randint(1, 100)

    if esquiva <= defensor["esquiva"]:
        print(f'{defensor["nome"]} desviou do ataque!')
        return

    dano = calcular_dano(
        atacante["ataque"],
        defensor["defesa"]
    )

    # Ataque crítico
    critico = random.randint(1, 100)

    if critico <= 20:
        dano *= 2
        print("💥 ATAQUE CRÍTICO!")

    defensor["vida"] -= dano

    if defensor["vida"] <= 0:
        defensor["vida"] = 0

    print(
        f'{atacante["nome"]} atacou '
        f'{defensor["nome"]} causando {dano} de dano'
    )

    print(
        f'Vida de {defensor["nome"]}: '
        f'{defensor["vida"]}'
    )


def usar_pocao(personagem):

    if personagem["pocoes"] > 0:

        cura = 30
        personagem["vida"] += cura

        if personagem["vida"] > personagem["vida_maxima"]:
            personagem["vida"] = personagem["vida_maxima"]

        personagem["pocoes"] -= 1

        print(
            f'{personagem["nome"]} usou uma poção '
            f'e recuperou {cura} de vida!'
        )

        print(
            f'Vida: {personagem["vida"]}/'
            f'{personagem["vida_maxima"]}'
        )

    else:
        print("Você não possui poções!")


def usar_magia(atacante, defensor):

    custo = 20

    if atacante["mana"] < custo:
        print("❌ Mana insuficiente!")
        return

    atacante["mana"] -= custo

    dano = atacante["magia"]

    defensor["vida"] -= dano

    if defensor["vida"] <= 0:
        defensor["vida"] = 0

    print(
        f'✨ {atacante["nome"]} lançou uma magia '
        f'e causou {dano} de dano!'
    )

    print(
        f'Vida de {defensor["nome"]}: '
        f'{defensor["vida"]}'
    )

    print(
        f'Mana de {atacante["nome"]}: '
        f'{atacante["mana"]}'
    )


jogador = {
    "nome": "Thor",
    "vida": 100,
    "vida_maxima": 100,
    "ataque": 25,
    "defesa": 10,
    "esquiva": 20,
    "pocoes": 3,
    "mana": 60,
    "magia": 35
}

inimigo = {
    "nome": "Slime",
    "vida": 80,
    "vida_maxima": 80,
    "ataque": 25,
    "defesa": 10,
    "esquiva": 10,
    "pocoes": 0,
    "mana": 0,
    "magia": 0
}


print("==== BATALHA ====")

while jogador["vida"] > 0 and inimigo["vida"] > 0:

    print("\n--- Turno do Jogador ---")

    print("1 - Ataque")
    print("2 - Usar poção")
    print("3 - Usar magia")

    opcao = input("Escolha uma ação: ")

    if opcao == "1":

        atacar(jogador, inimigo)

    elif opcao == "2":

        usar_pocao(jogador)

    elif opcao == "3":

        usar_magia(jogador, inimigo)

    else:

        print("Opção inválida.")
        continue

    if inimigo["vida"] <= 0:
        print("\n🏆 Você venceu!!")
        break

    print("\n--- Turno do Inimigo ---")

    atacar(inimigo, jogador)

    if jogador["vida"] <= 0:
        print("\n💀 Você perdeu!!")
        break