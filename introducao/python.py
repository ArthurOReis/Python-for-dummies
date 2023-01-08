# O Python possui uma série de comandos e funções, onde será demonstrado

print()

# 'print()' -> Printa mensagens que podem ser escritos dentro de aspas, nos parênteses, tanto em forma de string como boolean, int, double, float...

print("Hello, world!")
print(123)
print(3.21)

# Também pode printar valores de variáveis.

variavel_a = "Variável"
variavel_b = 123
variavel_c = True
variavel_d = 0.5

# Variáveis são elementos que guardam valores dentro deles, onde os mesmos podem ser de qualquer tipo
# Também podem guardar sequências, onde no mundo Python há três tipos de sequências
# Porém o que diferencia Python das outras linguagens é o fato de poder guardar valores diferentes em uma única sequência

variavel_f = [1, 2, 3, 4] #Lista/List
variavel_e = {1, 2, 3, 4} #Dicionário/Dictionary
variavel_g = (1, 2, 3, 4) #Tupla/Tuple

# Os três tipos de sequências apesar de iniciarem no index '0' como muitas linguagens de programação, trazem características distintas:

# Lista: Sequência acompanhada de index com valores que podem ser mudados
# Dicionário: Sequência de chaves que representam a index e armazenam um valor nelas
# Tupla: Sequência acompanhada de index com valores únicos que não podem ser alterados

# Dado as variáveis, é possível criar algoritmos com elas, através de condições e funções:

# If: Verifica se a condição recebida é verdadeira:

if variavel_f: # Se variavelF for 'True'
    print(variavel_f) # Printe variavelF
    
# Else: É o retorno que envia se a condição 'if' for falsa:

if variavel_f == variavel_c: # Se variavelF for igual a variavelC
    print(variavel_f) # Printe variavelF
else: # Senão
    print(variavel_c) # Printe variavelE

# Elif: É outra condição antes do 'else' que faz outra verificação caso o primeiro 'if' seja inválido:

if 1 == 1.1: # Se 1 for igual a 1.1
    print("1 é igual a 1.1!") # Printe essa mensagem
    
elif 1 == 1.0: # Porém se 1 for igual a 1.0
    print("1 é igual a 1.0!") # Printe essa mensagem
    
else: # Caso nenhuma nenhuma das condições acima forem verdadeiras
    print("1 é igual a 1!") # Printe essa mensagem

# Outro tipo de condição são loopings que terminam se uma condição for verdadeira, sendo elas 'for' e 'while'
# For: Estrutura de repetição que itera sobre elementos de uma sequência (Como uma string, uma lista, tupla ou dicionário):

banana = "Banana" # Variável 'banana' com valor string "Banana"

for letra in banana: # Para cada letra em banana
    print(letra) # Printe as letras
    
tuplas = ('tupla1', 'tupla2', 'tupla3') # Variável 'tuplas' com valor de uma sequência de tupla

for tupla in tuplas: # Para cada tupla em 'tuplas'
    print(tupla) # Printe todas 'tupla' em tuplas
    
informacoes_pessoais = {'Nome': 'Arthur', 'Idade': 16, 'Cidade': 'São Paulo'} # Variável 'informacoes_pessoais' com chaves e seus valores

for chave, valor in informacoes_pessoais.items(): # Para cada chave e valor listado em 'informacoes_pessoais'
    print("{}:{}".format(chave, valor)) # Printe todas as chaves e valores
    
# Porém o 'for' não precisa necessariamente antes criar uma variável para ser inicializada
# É possível fazer uma contagem progressiva usando o método 'range()', que se inicia por padrão no index '0'

for i in range(10): # Para cada variável 'i' em uma índice de 10 números
    print(i) # Printe 10 vezes 'i', aumentando seu valor a cada 'print(i)'