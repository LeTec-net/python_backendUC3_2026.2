import random


# ==========================
# FUNÇÕES
# ==========================

def mostrar_status(jogador):
    print("\n===== STATUS =====")
    print(f"Nome: {jogador['nome']}")
    print(f"Nível: {jogador['nivel']}")
    print(f"Experiência: {jogador['xp']}/{jogador['xp_proximo_nivel']}")
    print(f"Vida: {jogador['vida']}/{jogador['vida_maxima']}")
    print(f"Moedas: {jogador['moedas']}")
    print(f"Poções: {jogador['pocoes']}")


def mostrar_inventario(jogador):
    print("\n===== INVENTÁRIO =====")

    if len(jogador["inventario"]) == 0:
        print("Seu inventário está vazio.")
    else:
        for item, quantidade in jogador["inventario"].items():
            print(f"{item}: {quantidade}")


def ganhar_experiencia(jogador, xp):
    jogador["xp"] += xp

    print(f"Você ganhou {xp} XP!")

    if jogador["xp"] >= jogador["xp_proximo_nivel"]:

        jogador["nivel"] += 1
        jogador["xp"] -= jogador["xp_proximo_nivel"]

        jogador["xp_proximo_nivel"] += 50

        jogador["vida_maxima"] += 20
        jogador["vida"] = jogador["vida_maxima"]

        jogador["ataque"] += 5
        jogador["defesa"] += 2

        print("\n🌟 VOCÊ SUBIU DE NÍVEL! 🌟")
        print(f"Agora você está no nível {jogador['nivel']}!")
        print(f"Vida máxima: {jogador['vida_maxima']}")
        print(f"Ataque: {jogador['ataque']}")
        print(f"Defesa: {jogador['defesa']}")


def atacar(jogador, inimigo):

    dano = jogador["ataque"] - inimigo["defesa"]

    if dano <= 0:
        dano = 1

    dano = random.randint(dano - 2, dano + 2)

    if dano < 1:
        dano = 1

    inimigo["vida"] -= dano

    if inimigo["vida"] < 0:
        inimigo["vida"] = 0

    print(
        f"\n⚔️ {jogador['nome']} atacou "
        f"{inimigo['nome']} causando {dano} de dano!"
    )


def inimigo_ataca(jogador, inimigo):

    dano = inimigo["ataque"] - jogador["defesa"]

    if dano <= 0:
        dano = 1

    dano = random.randint(dano - 2, dano + 2)

    if dano < 1:
        dano = 1

    jogador["vida"] -= dano

    if jogador["vida"] < 0:
        jogador["vida"] = 0

    print(
        f"👹 {inimigo['nome']} atacou "
        f"{jogador['nome']} causando {dano} de dano!"
    )


def usar_pocao(jogador):

    if jogador["pocoes"] > 0:

        cura = 30

        jogador["vida"] += cura

        if jogador["vida"] > jogador["vida_maxima"]:
            jogador["vida"] = jogador["vida_maxima"]

        jogador["pocoes"] -= 1

        print(f"🧪 Você recuperou {cura} de vida!")

    else:
        print("❌ Você não possui poções.")


def combate(jogador, inimigo):

    print("\n========================")
    print(f"⚔️ UM {inimigo['nome'].upper()} APARECEU!")
    print("========================")

    while jogador["vida"] > 0 and inimigo["vida"] > 0:

        print("\n--- SEU TURNO ---")
        print("1 - Atacar")
        print("2 - Usar poção")
        print("3 - Ver status")

        opcao = input("Escolha uma ação: ")

        if opcao == "1":

            atacar(jogador, inimigo)

            if inimigo["vida"] <= 0:
                print(f"\n🏆 Você derrotou {inimigo['nome']}!")
                return True

        elif opcao == "2":

            usar_pocao(jogador)

        elif opcao == "3":

            mostrar_status(jogador)
            continue

        else:

            print("Opção inválida.")
            continue

        if inimigo["vida"] > 0:

            print("\n--- TURNO DO INIMIGO ---")

            inimigo_ataca(jogador, inimigo)

    return False


# ==========================
# JOGADOR
# ==========================

jogador = {
    "nome": "Thor",
    "nivel": 1,
    "xp": 0,
    "xp_proximo_nivel": 100,
    "vida": 100,
    "vida_maxima": 100,
    "ataque": 20,
    "defesa": 5,
    "moedas": 100,
    "pocoes": 3,

    "inventario": {
        "Poção de Vida": 3
    }
}


# ==========================
# INIMIGOS
# ==========================

inimigos = [

    {
        "nome": "Slime",
        "vida": 40,
        "ataque": 10,
        "defesa": 3,
        "xp": 60,
        "moedas": 20
    },

    {
        "nome": "Goblin",
        "vida": 60,
        "ataque": 15,
        "defesa": 5,
        "xp": 100,
        "moedas": 35
    },

    {
        "nome": "Orc",
        "vida": 90,
        "ataque": 20,
        "defesa": 8,
        "xp": 120,
        "moedas": 60
    }
]


# ==========================
# FASES
# ==========================

fase = 1

print("================================")
print("       ⚔️ AVENTURA RPG ⚔️")
print("================================")

jogador["nome"] = input("Digite o nome do seu personagem: ")

while fase <= len(inimigos) and jogador["vida"] > 0:

    print("\n==============================")
    print(f"          FASE {fase}")
    print("==============================")

    inimigo = inimigos[fase - 1].copy()

    venceu = combate(jogador, inimigo)

    if venceu:

        jogador["moedas"] += inimigo["moedas"]

        print(f"💰 Você encontrou {inimigo['moedas']} moedas!")

        ganhar_experiencia(jogador, inimigo["xp"])

        print(f"⭐ Você ganhou {inimigo['xp']} XP!")

        mostrar_status(jogador)

        fase += 1

        if fase <= len(inimigos):
            print("\n➡️ Preparando próxima fase...")

    else:

        print("\n💀 Você foi derrotado!")
        break


if jogador["vida"] > 0 and fase > len(inimigos):

    print("\n🏆🏆🏆")
    print("PARABÉNS!")
    print("Você completou todas as fases!")
    print("🏆🏆🏆")

    mostrar_status(jogador)

else:

    print("\n===== FIM DE JOGO =====")