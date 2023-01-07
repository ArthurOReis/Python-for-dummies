# O Python possui uma série de comandos e funções, onde será demonstrado

print()

# 'print()' -> Printa mensagens que podem ser escritos dentro de aspas, nos parênteses, tanto em forma de string como boolean, int, double, float...

print("Hello, world!")
print(123)
print(3.21)

# Também pode printar valores de variáveis.

variavelA = "Variável"
variavelB = 123
variavelC = True
variavelD = 0.5

# Variáveis são elementos que guardam valores dentro deles, onde os mesmos podem ser de qualquer tipo
# Também podem guardar sequências, onde no mundo Python há três tipos de sequências
# Porém o que diferencia Python das outras linguagens é o fato de poder guardar valores diferentes em uma única sequência

variavelF = [1, 2, 3, 4] #Lista/List
variavelE = {1, 2, 3, 4} #Dicionário/Dictionary
variavelG = (1, 2, 3, 4) #Tupla/Tuple

# Os três tipos de sequências apesar de iniciarem no index '0' como muitas linguagens de programação, trazem características distintas:

# Lista: Sequência acompanhada de index com valores que podem ser mudados
# Dicionário: Sequência de chaves que representam a index e armazenam um valor nelas
# Tupla: Sequência acompanhada de index com valores únicos que não podem ser alterados

# Dado as variáveis, é possível criar algoritmos com elas, através de condições e funções:

# If: Verifica se a condição recebida é verdadeira:

if variavelF: # Se variavelF for 'True'
    print(variavelF) # Printe variavelF
    
# Else: É o retorno que envia se a condição 'if' for falsa:

if variavelF == variavelC: # Se variavelF for igual a variavelC
    print(variavelF) # Printe variavelF
else: # Senão
    print(variavelC) # Printe variavelE

# Elif: É outra condição antes do 'else' que faz outra verificação caso o primeiro 'if' seja inválido:

if 1 == 1.1:
    print("1 é igual a 1.1!")
elif 1 == 1.0:
    print("1 é igual a 1.0!")
else:
    print("1 é igual a 1!")

# Outro tipo de condição são loopings que terminam se uma condição for verdadeira,

#i = 0    
#while i < 100:
#    i += 1
#    print(i) 