# *Criando um jogo*

Com o entendimento dos assuntos envolvendo Python, como [introdução](https://github.com/ArthurOReis/Python-for-dummies/blob/main/1-%20introducao/python.py) e [parte 1 do python avançado](https://github.com/ArthurOReis/Python-for-dummies/blob/main/2-%20avancado/parte-1/README.md), vamos aplicar esse conhecimento na criação de um jogo de adivinhação de números.

## ***Inicializando uma introdução***

Quando iniciamos um programa, é recomendado trazer uma introdução a um usuário para ambientá-lo dentro, e de preferência bem chamativa, sendo a forma que o jogo vai ser inicializado:

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")
~~~

Em seguida, cria-se uma variável 'número_secreto' onde vai ficar armazenado um número para ser descoberto, seguido de um input para que o usuário consiga adivinhar o número que vai ter o seu valor salvo numa variável, e por fim confirmar o input através de outro print: 

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98 #+

chute = input("Adivinhe o número secreto: ") #+

print("Seu chute foi o número ", chute) #+
~~~

Com o chute e o número secreto, é necessário fazer uma ligação entre esses números para que o jogo funcione, dito isso, vamos usar a condição 'if' e comparar os dois valores recebidos, e para ser válido, é preciso converter o input em int, e por fim um print sinalizando fim de jogo:

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98

chute = int(input("Adivinhe o número secreto: "))

print("Seu chute foi o número ", chute)

if chute == numero_secreto: #+
    print("Você acertou!") #+
else: #+
    print("Você errou!") #+

print("Fim de jogo") #+
~~~

O jogo já está em forma, mas dá para melhorar adicionando mais opções para o jogo, como um sinalizador através de um print para descobrir a distância entre o chute e o número secreto através de um 'if' dentro do 'else', e facilitando as condições, elas podem ser atribuidas a uma variável, ficando:

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98

chute = int(input("Adivinhe o número secreto: "))

igual = chute == numero_secreto #+
maior = chute > numero_secreto #+
menor = chute < numero_secreto #+

print("Seu chute foi o número ", chute)

if igual: #+
    print("Você acertou!") #+
else: #+
    if maior: #+
        print("Seu chute foi maior que o número secreto") #+
    elif menor: #+
        print("Seu chute foi menor que o número secreto") #+
        
print("Fim de jogo")
~~~

Criando as possibilidades de acerto e erro, seria viável criar uma quantia de tentativas que o usuário pode ter para tentar chutar o número secreto, para isso nós precisamos mostrar quantas tentativas existem e um sistema que válida a jogada através delas, e para isso, usa-se o 'while':

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98
total_tentativas = 3 #+
chance = 1 #+

while chance <= total_tentativas: #+
    print("Tentativa", chance, "de", total_tentativas) #+
    chute = int(input("Adivinhe o número secreto: "))

    igual = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if igual:
        print("Você acertou!")
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")
    chance += 1 #+

print("Fim de jogo")
~~~

### OPCIONAL

Caso queira formatar o string do print de tentativas, de forma com que seja mais pythônico, pode-se usar a propriedade '.format()', que por ordem da esquerda para direita, traz as variáveis no texto através dos '{}' que simbolizam a posição do valor que vai receber:

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98
total_tentativas = 3 #+
chance = 1 #+

while chance <= total_tentativas: #+
    print("Tentativa {} de {}".format(chance, total_tentativas)) #+ #A saída vai ser 'Tentativa 1 de 3'
    chute = int(input("Adivinhe o número secreto: "))

    igual = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if igual:
        print("Você acertou!")
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")
    chance += 1

print("Fim de jogo")
~~~

Agora, caso o código parecer grande, é possível diminuí-lo de algumas formas, sendo elas substituindo o 'while' por 'for range', que vai fazer com que 'para cada chance em total de tentativas, execute o jogo', dessa forma, não será mais preciso adicionar mais um valor à chance, pois o looping faz isso:

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98
total_tentativas = 3 #+
#-

for chance in range(1, total_tentativas + 1): #+
    print("Tentativa {} de {}".format(chance, total_tentativas))
    chute = int(input("Adivinhe o número secreto: "))

    igual = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if igual:
        print("Você acertou!")
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")

print("Fim de jogo")
~~~

Reformulando um pouco o jogo, seria bom definir para o usuário qual é o limite mínimo e máximo para chutar o número, e também parar o jogo independentemente da quantia de chances quando o número secreto for acertado, usando a propriedade 'break':

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98
total_tentativas = 3 #+

for chance in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(chance, total_tentativas))
    chute = int(input("Adivinhe um número entre 1 e 100: ")) #+

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

print("Fim de jogo")
~~~

Com a possibilidade do número secreto ser de 1 a 100, é possível que o jogador insira um número acima ou abaixo dos limites, para esse cenário, usa-se uma condição 'if' e outra palavra-chave similar ao 'break', sendo 'continue', que nesse contexto, vai invalidar o input do chute acima de 100 e abaixo de 1:

~~~python
print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = 98
total_tentativas = 3

for chance in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(chance, total_tentativas))
    chute = int(input("Adivinhe um número entre 1 e 100: "))
    
    if chute < 1 or chute > 100: #+
        print("Você deve chutar um número de 1 a 100!") #+
        continue #+

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

print("Fim de jogo")
~~~

Com o intuito de tornar o desafio do jogo maior e aleatório, no lugar de selecionar e colocar um número secreto manualmente, há uma maneira gerar um número aleatório que seja entre 1 e 100. Primeiramente, importa-se 'random', que quando chamado, gera um número aleatório de 0.0 a 1.0 (Exemplo: 0.045723894...), para fazer com que o random gerado tenha um limite de 1 a 100, é preciso usar a propriedade 'randrange', que define especificadamente o valor mínimo e o máximo que pode ser gerado:

~~~python
import random #+

print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = random.randrange(1, 101) #+ #O limite máximo é 101 pois é o valor máximo e que não pode ser gerado
total_tentativas = 3

for chance in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(chance, total_tentativas))
    chute = int(input("Adivinhe um número entre 1 e 100: "))
    
    if chute < 1 or chute > 100: #+
        print("Você deve chutar um número de 1 a 100!") #+
        continue #+

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

print("Fim de jogo")
~~~

Mas para que o jogo não seja completamente desafiador, pode-se implementar o sistema de dificuladade, para isso, a variável total tentativas por padrão vai ser zero, seguido de um print mostrando as dificuldades e um input para selecionar, por fim, dependendo da dificuldade escolhida, uma quantia de chances serão dadas conforme a escolha:

~~~python
import random

print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0 #+

print("Escolha o nível de dificuldade!") #+
print("[1] Fácil - [2] Médio - [3] Difícil") #+

nivel = int(input("Escolha seu nível!: ")) #+ #Não se esqueça de converter o input em int
if nivel == 1: #+
    total_tentativas = 20 #+
if nivel == 2: #+
    total_tentativas = 10 #+
if nivel == 3: #+
    total_tentativas = 5 #+
    
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
        print("Você acertou!")
        break
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")

print("Fim de jogo")
~~~

Com os níveis de dificuldade criados, não seria incomum também implementar uma pontuação, que nesse caso vai se inicializar com valor de 1000, e para cada chute errado, a pontuação é subtraída pela diferença entre o número secreto e o chute. Caso o chute for maior que o número secreto, é possível converter a diferença para ser positivo usando a função 'abs()' (função absoluta):

~~~python
import random

print("*-------------------------------*")
print("Bem vindo ao jogo da adivinhação!")
print("*-------------------------------*")

numero_secreto = random.randrange(1, 101)
total_tentativas = 0
pontos = 1000 #+

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
        print("Você acertou e fez {} pontos!".format(pontos)) #+
        break
    else:
        if maior:
            print("Seu chute foi maior que o número secreto")
        elif menor:
            print("Seu chute foi menor que o número secreto")
        pontos_perdidos = abs(numero_secreto - chute) #+
        pontos = pontos - pontos_perdidos #+

print("Fim de jogo")
~~~