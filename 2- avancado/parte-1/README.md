# Parte 1: Funções e 'name = main'

## Função

No Python, assim como outras linguagens de programação, é comum ter ações repetidas para chegar no resultado esperado, porém manualmente escrever essas ações mais de uma vez não é uma boa prática. Por isso existe às funções, que possuem a funcionalidade de ter linhas de códigos prontas para serem usadas quando a função for chamada em algum momento.

Comandos como "print()", "input()", "int()" e entre outros... São funções build-in que fazem parte da biblioteca Python.

## Como criar uma função

Como regra universal da programação, uma função precisa de um nome, receber ou não parâmetros e retornar algo, e isso não difere no python. Logo, na prática, uma função pythonica se inicia com 'def', seguido de um nome para função, parênteses para receber ou não parâmetro e 'return' para retornar um valor, ficando:

~~~python
def main(): #Definindo uma função chamado "main" sem nenhum parâmetro
    #<Uma quantia de linha de códigos>#
    return #<Um valor>#
~~~

#### No caso de uma função com parâmetro(s), ele executa e retorna conforme os parâmetros recebidos, como, por exemplo:

~~~python
def dois_numeros(numeroa,numerob): #A função 'dois_numero' espera receber dois parâmetros (numeroa e numeroa)
    resultado = print(numeroa+numerob) #O resultado é um print da soma dos parâmetros
    return resultado #Em seguida vai retornar o valor do rersultado

dois_numeros(2, 2) #A função é chamada e recebe dois números
~~~
### Resultado:
```
4

Process finished with exit code 0
```


Dessa forma, pode-se criar funções que lhe auxiliarão bastante nos seus projetos:
```python
def separa_lista(lista: list):
    for elemento in lista:
        print(elemento)

lista = ['Fábio', 'Clara', 'Dennis', 'João', 'Daniela', 'José']
separa_lista(lista)
```
### Resultado:
```
Fábio
Clara
Dennis
João
Daniela
José

Process finished with exit code 0
```

## Importando funções criadas

Digamos que queira utilizar as funções criadas em outro arquivo do mesmo diretório.

Nesse caso, como mostrado na linha 100 do [Python-for-dummies/1-introducao/python.py](https://github.com/ArthurOReis/Python-for-dummies/blob/main/1-%20introducao/python.py), pode-se importar a função de um arquivo, como no exemplo abaixo:

### arquivo_1:
~~~python
def separa_lista(lista: list):
    for elemento in lista:
        print(elemento)
~~~

### arquivo_2:
~~~python
from arquivo_1 import separa_lista

lista = ['Fábio', 'Clara', 'Dennis', 'João', 'Daniela', 'José']
separa_lista(lista)
~~~

### Resultado:
```
Fábio
Clara
Dennis
João
Daniela
José

Process finished with exit code 0
```

## " __ name __ == __ main __ "

É comum após criar funções, testá-las para observar se tudo funciona de acordo com esperado, e com funcionamento, é comum importar para outro arquivo para utiliza seja qual for o projeto. Porém, pode acontecer dos testes da função importada serem exibidas indesejadamente no arquivo que estáimportando a função:

### arquivo_1
~~~python
def subtracao(num1: float, num2: float): #Função 'subtracao' que recebe dois parâmetros do tipo float
    return print(num1 - num2)

teste1 = subtracao(6,3)
teste2 = subtracao(10,3)

~~~

### Output quando rodar arquivo_1:
```
3
7

Process finished with exit code 0
```

### arquivo_2
~~~python
from arquivo_1 import subtracao

teste1 = subtracao(2,1)
~~~

### Output quando rodar arquivo_2:
```
3
7
1

Process finished with exit code 0
```

Para que isso não aconteça, existe uma condição 'if' que realiza o trabalho de não executar os testes indesejáveis em outros arquivos:

### arquivo_1
~~~python
def subtracao(num1: float, num2: float):
    return print(num1 - num2)

if __name__ == '__main__':
    teste1 = subtracao(6,3)
    teste2 = subtracao(10,3)
~~~

### Output quando rodar arquivo_1:
```
3
7

Process finished with exit code 0
```

### arquivo_2
~~~python
from arquivo_1 import subtracao

teste1 = subtracao(2,1)
~~~

### Output quando rodar arquivo_2:
```
1

Process finished with exit code 0
```
Para entender o que aconteceu, é preciso saber o que é módulo, que resumidamente é um arquivo Python com comandos e funções que pode ser usado em outro programa da mesma linguagem.
E por padrão, os módulos são chamados '__ main __', mas ao importar esse módulo em outro local, ele passa a se chamar pelo nome recebido do arquivo.

Sabendo disso, é possível saber se o arquivo que está usando é importado ou não através da variável ' __ name __ ', e printando ela (*print(__ name __)*), vai ser exibido ou '__ main __', ou o nome do arquivo importado.

Por fim, usar a condição 'if' sobre name e main pode trazer algumas vantagens, como o fato de caso o módulo for executado quando for importado, não irá mostrar variáveis inesperadas, além de poder realizar testes de forma com que não afete o arquivo que está importando o módulo.
