def pedra_papel_tesoura():

    import random

    print("=== Pedra Papeal Tesoura ===")

    opcoes = ["pedra", "papel", "tesoura"]
    maquina = random.choice(opcoes)

    usuario = str(input("pedra, papel ou tesoura: ")).lower

    if usuario == maquina:
        print(f"{usuario} X {maquina}")
        print("Empate")
    elif usuario == "pedra" and maquina == "tesoura":
        print(f"{usuario} X {maquina}")
        print("Parabens voce venceu")
    elif usuario == "tesoura" and maquina == "papel":
        Print(f"{usuario} X {maquina}")
        print("Parabens Voce venceu")
    elif usuario == "papel" and maquina == "pedra":
        Print(f"{usuario} X {maquina}")
        print("Parabens voce venceu")
    else:
        print(f"{usuario} X {maquina}")
        print("Voce perdeu")


pedra_papel_tesoura()