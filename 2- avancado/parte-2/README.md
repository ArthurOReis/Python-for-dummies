# Parte 2: ***Orientação a Objetos***

## Introdução

Orientação a Objetos é um paradigma/modelo presente em muitas linguagens de programação, como Java, C++, Go, Ruby... E também Python. O motivo da sua popularidade se dá por trazer organização, classificação, manipulação e abstração de objetos, onde os mesmos incorporam estruturas de dados e um conjunto de funções que os manipulam.

~~~python
# Criando um Objeto para representar uma conta bancária
Conta = {"ID": 123.456.789-10, "Titular": "Arthur Reis", "Saldo": 1300.0, "Limite": 10000.0}

~~~

Como mostrado, por um dicionário, foi possível criar um objeto contendo dados, porém, isso está longe de ser uma prática de Orientação a Objetos, logo, será mostrado abaixo cada recurso que compõe o modelo.

## Classe

***POO****: Programação Orientada a Objetos

Sendo uma regra universal, para a criação de um arquivo que suporta **POO***, é preciso ter uma classe, pois é onde fica toda a estrutura do objeto, como os atributos, método construtor e outras funções relacionadas.
Por padrão, o nome das classes começam **sempre** com letra maiúscula:

~~~python

class Conta:
    
    #Atributos
        
    #Método construtor
    
    #Funções

~~~

Testando a classe no Console Python, mesmo vázia, ainda é possível obter resultados:

~~~Python console session
>>> Conta()
<__main__.Conta object at 0x0000025540F7B090>
>>> conta = Conta()
>>> conta
<__main__.Conta object at 0x0000025540F7B090>
~~~

Ao criar um objeto, como no exemplo acima, ele é armazenado num espaço na memória da máquina, e mesmo se for armazenado numa variável, o seu "endereço" permanecerá o mesmo.

## Atributo

Para um objeto ter características, necessita-se de atributos que como esperado, traz um perfi, e dependendo de quantos atributos e quais os seus tipos, haverá inúmeras maneiras de trabalhar com eles, como além da construção, a manipulação e a estrutura do Objeto.

## Método construtor

Método construtor é a função que dá origem a um objeto, dentro dele, é possível setar parâmetros, que, são os atributos.
Linguagens que suportam **POO**, possuem as suas formas de criar um método construtor, no caso do Python, há uma função especial na biblioteca da linguagem que realiza a ação, chamada '__ init __', e junto disso, há uma palavra-chave usada tanto no parâmetro quanto no método internamente e a sua função é referênciar um objeto ou um atributo, o seu nome é 'self':

### Inicializando objeto apenas com 'self':

~~~python
class Conta:
    
    def __init__(self):
        print("Construindo objeto... Endereço {}".format(self))
~~~

### Console Python:

~~~Python console session
>>> conta = Conta()
Construindo objeto... Endereço <__main__.Conta object at 0x000001C38E13F650>
~~~

### Inicializando objeto apenas com atributos através do 'self':

~~~python
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... Endereço {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
~~~

### Console Python:

~~~Python console session
>>> conta = Conta(123, "Arthur Reis", 1000.0, 500.0)
Construindo objeto... Endereço <__main__.Conta object at 0x0000020187A46090>
~~~

### Na variável 'conta':

![img.png](imgs/img.png)

## Funções em POO

Para complementar a classe Conta, pode-se incluir funções que façam sentido e interajam com o objeto. Nesse contexto, é uma simulação de uma conta bancária, criando métodos relacionados com o que for procurado:

~~~python
class Conta:
    
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto... Endereço {}".format(self))
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print("O saldo de {} do titular {}".format(self.saldo, self.titular))

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor 
~~~

### Console Python:

~~~Python console session
>>> conta = Conta(123, "Arthur Reis", 1000.0, 500.0)
Construindo objeto... Endereço <__main__.Conta object at 0x00000216B359E750>
>>> conta.saca(100.0)
>>> conta.extrato()
O saldo de 900.0 do titular Arthur Reis
>>> conta.deposita(100.0)
>>> conta.extrato()
O saldo de 1000.0 do titular Arthur Reis
~~~

## Entendendo como realmente funciona POO internamente

Dado a introdução, é preciso entender o que acontece na máquina quando realizamos a ação de criar objetos e classes, para ter conhecimento de coisas como none e coletor de lixo.

![img.png](imgs/img2.png)

Ao criar um objeto com os seus parâmetros, todas as informações do mesmo serão armazenados num espaço na memória do computador, e quando ele é criado e atribuido a uma variável, o mesmo ocorre, mas a variável vai se tornar um referêncial (representado em forma de flecha no desenho) que aponta para esse mesmo objeto específico quando for chamado.

![img.png](imgs/img3.png)

É possível nesse cenário, repetição do objeto criado, e como mostrado no desenho, será internamente armazenado espaço para outro objeto idêntico ao anterior, e a variável começa a apontar para o mesmo.
Mas a Conta original, mesmo não tendo referência, continua a existir e ocupa memória desnecessariamente, causando vazamento de memória (Memory leak).

Em casos como esse, há um recurso disponível na linguagem que impede esse erro de acontecer, chamado coletor de lixo (Garbage collector), a sua função é limpar a memória, e na situação apresentada, ele vai pegar o objeto inutilizado que não é referênciado e elimina do local, assim evitando o problema.

## Referência e None

![img.png](imgs/img4.png)

Retornando às referências, quando se cria outra variável que aponta para um objeto já existente, não ocorre nenhum erro, pois no Python multireferêcia em um mesmo objeto é permitido.

Caso queira eliminar a variável que referencia ao objeto, basta atribuí-lo a palavra chave "None", que ao ser usado, é desvinculado do objeto:

![img.png](imgs/img5.png)