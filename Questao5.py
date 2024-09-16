
#Exercício 5: Escreva um programa que jogue "pedra, papel ou tesoura" contra o usuário. O jogo deve continuar até o usuário escolher parar, e retornar o número de vitórias do usuário, da máquina, e empates.


import random


vitorias_usuario = 0
vitorias_maquina = 0
empates = 0


def determinar_vencedor(usuario, maquina):
    if usuario == maquina:
        return "empate"
    elif (usuario == "pedra" and maquina == "tesoura") or \
         (usuario == "papel" and maquina == "pedra") or \
         (usuario == "tesoura" and maquina == "papel"):
        return "usuario"
    else:
        return "maquina"


while True:

    escolha_usuario = input("Escolha pedra, papel ou tesoura (ou 'parar' para encerrar): ").lower()


    if escolha_usuario == 'parar':
        break


    if escolha_usuario not in ["pedra", "papel", "tesoura"]:
        print("Escolha inválida, tente novamente.")
        continue


    escolha_maquina = random.choice(["pedra", "papel", "tesoura"])


    print(f"Você escolheu: {escolha_usuario}")
    print(f"A máquina escolheu: {escolha_maquina}")


    resultado = determinar_vencedor(escolha_usuario, escolha_maquina)

    if resultado == "empate":
        print("Empate!")
        empates += 1
    elif resultado == "usuario":
        print("Você venceu!")
        vitorias_usuario += 1
    else:
        print("A máquina venceu!")
        vitorias_maquina += 1

    print(f"Placar: Você {vitorias_usuario} - {vitorias_maquina} Máquina - Empates {empates}\n")


print("Jogo encerrado.")
print(f"Placar final: Você {vitorias_usuario} - {vitorias_maquina} Máquina - Empates {empates}")