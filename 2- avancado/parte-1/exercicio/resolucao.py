import random

print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000  # +

print("Escolha o nível de dificuldade!")
print("[1] Fácil - [2] Médio - [3] Difícil")

nivel = int(input("Escolha seu nível!: "))
if nivel == 1:
    total_tentativas = 20
if nivel == 2:
    total_tentativas = 10
if nivel == 3:
    total_tentativas = 5

for chance in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(chance, total_tentativas))
    chute = int(input("Adivinhe um número entre 1 e 100: "))

    if chute < 1 or chute > 100:
        print("Você deve chutar um número de 1 a 100!")
        continue

    igual = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if igual:
        print("Você acertou e fez {} pontos!".format(pontos))
        break
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

print("Fim de jogo")