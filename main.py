def pedra_papel_tesoura():

    while True:
        try:


            import random

            print("=== Pedra Papeal Tesoura ===")

            opcoes = ["pedra", "papel", "tesoura"]
            maquina = random.choice(opcoes)

            usuario = str(input("pedra, papel ou tesoura: "))

            if usuario == maquina:
                print(f"{usuario} X {maquina}")
                print("Empate")
                continuar = str(input("Deseja continuar (s/n): "))
                if continuar == "s":
                    continue
                else:
                    print("Programa encerrando")
                    break


            elif usuario == "pedra" and maquina == "tesoura":
                print(f"{usuario} X {maquina}")
                print("Parabens voce venceu")
                continuar = str(input("Deseja continuar (s/n): "))
                if continuar == "s":
                    continue
                else:
                    print("Programa encerrando")
                    break


            elif usuario == "tesoura" and maquina == "papel":
                Print(f"{usuario} X {maquina}")
                print("Parabens Voce venceu")
                continuar = str(input("Deseja continuar (s/n): "))
                if continuar == "s":
                    continue
                else:
                    print("Programa encerrando")
                    break

            elif usuario == "papel" and maquina == "pedra":
                Print(f"{usuario} X {maquina}")
                print("Parabens voce venceu")
                continuar = str(input("Deseja continuar (s/n): "))
                if continuar == "s":
                    continue
                else:
                    print("Programa encerrando")
                    break


            else:
                print(f"{usuario} X {maquina}")
                print("Voce perdeu")
                continuar = str(input("Deseja continuar (s/n): "))
                if continuar == "s":
                    continue
                else:
                    print("Programa encerrando")
                    break

        except ValueError:
            print("Valor digitado incorreto!")
            continuar = str(input("Deseja continuar (s/n): "))
            if continuar == "s":
                continue
            else:
                print("Programa encerrando")
                break


pedra_papel_tesoura()