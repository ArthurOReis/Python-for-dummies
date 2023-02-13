# Parte 2: ***Orientação a Objetos***

## Introdução

Orientação a Objetos é um paradigma/modelo presente em muitas linguagens de programação, como Java, C++, Go, Ruby... E também Python. O motivo da sua popularidade se dá por trazer organização, classificação, manipulação e abstração de objetos, onde os mesmos incorporam estruturas de dados e um conjunto de funções que os manipulam.

~~~python
# Criando um Objeto para representar uma conta bancária
Conta = {"ID": 123.456.789-10, "Titular": "Arthur Reis", "Saldo": 1300.0, "Limite": 10000.0}

~~~

Como mostrado, por um dicionário, foi possível criar um objeto contendo dados, porém, isso está longe de ser uma prática de Orientação a Objetos, logo, será mostrado abaixo cada recurso que compõe o modelo.

## Classe

***PO****: Programação Orientada a Objetos

Sendo uma regra universal, para a criação de um arquivo que suporta **POO***, é preciso ter uma classe, pois é onde fica toda a estrutura do objeto, como os atributos, método construtor e outras funções relacionadas.
Por padrão, o nome das classes começam **sempre** com letra maiúscula:

~~~python

class Conta:
    
    #Atributos
        
    #Método construtor
    
    #Funções

~~~

Testando a classe, mesmo vázia, ainda é possível obter resultados:

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

~~~python

class Conta:
    

~~~

