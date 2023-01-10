# Parte 1: Funções e 'name = main'

## Função

No Python, assim como outras linguagens de programação, é comum ter ações repetidas para chegar no resultado esperado, porém manualmente escrever essas ações mais de uma vez não é uma boa prática. Por isso existe às funções, que possuem a funcionalidade de ter linhas de códigos prontas para serem usadas quando a função for chamada em algum momento.

Comandos como "print()", "input()", "int()" e entre outros... São funções build-in que fazem parte da biblioteca Python.

## Como criar uma função

Como regra universal da programação, uma função precisa de um nome, receber ou não parâmetros e retornar algo, e isso não difere no python. Logo, na prática, uma função pythonica se inicia com 'def', seguido de um nome para função, parênteses para receber ou não parâmetro e 'return' para retornar um valor, ficando:

~~~python
def main():
    #<Uma quantia de linha de códigos>#
    return #<Um valor>#
~~~

No caso de uma função com parâmetro(s), ele executa e retorna conforme os parâmetros recebidos, como, por exemplo:

~~~python
def dois_numeros(numeroa,numerob): #A função 'dois_numero' espera receber dois parâmetros (numeroa e numeroa)
    resultado = print(numeroa+numerob) #O resultado é um print da soma dos parâmetros
    return resultado #Em seguida vai retornar o valor do rersultado

dois_numeros(2, 2) #A função é chamada e recebe dois números
~~~
Resultado:
```Python console session
4

Process finished with exit code 0
```

Dessa forma, você pode criar funções que te auxiliarão bastante em seus projetos:
