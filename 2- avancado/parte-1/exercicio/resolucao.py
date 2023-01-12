print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98
total_tentativas = 3

for chance in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(chance, total_tentativas))
    chute = int(input("Adivinhe um número entre 1 e 100: "))

    igual = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if igual:
        print("Você acertou!")
        break
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")
    chance += 1

print("Fim de jogo")