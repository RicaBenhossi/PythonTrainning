"""
Este arquivo é para lembrar os comandos mais básicos de python.
Segue abaixo os comandos.
"""
------------------------------------------------------------------------------------
"""
Variáveis não precisam de declaração de tipo.
"""

vInteiro = 6
vFloat = 10.87
vBooleano = True
vLista = ['item 1', 'item2'] # ARRAY
vChave = {'Item1 ': 10, 'Item2' :50} # ARRAY com Índices
vString = "Essa é uma String"
    #CUIDADO: o Python interpreta o apóstrofo como fechamento de string. Corriga com \
    #Exemplo de código com erro: vTextoApostrofo = 'There's a problem Huston!''

    vTextoApostrofo = 'There\'s a problemm Huston!''
    print (vTextoApostrofo)

    #O índice de caracteres do Python começa com 0.
    """
    +---+---+---+---+---+---+
    | P | Y | T | H | O | N |
    +---+---+---+---+---+---+
    0   1   2   3   4   5
    """
    vTexto = "Python"
    print(vTexto[4])
    print(vTexto[1])
    print(vTexto[0])
    print(vTexto)

------------------------------------------------------------------------------------
"""
Exibe algo na tela

SINTAXE - print(O_que_se_deseja_exibir)
"""

print('Hello World')

# Concatenação de string
print("Teste" + " de cotatenação " + "de " + "Strings")

# Concatenação/Formatação de String usado % (MELHOR JEITO)
string1 = "Camelot"
string2 = "besta"
print ("Não vamos à %s. É um lugar %s pra dedéu." % (string1, string2))

------------------------------------------------------------------------------------
"""
Métodos de String
"""

# len() traz o número de caracteres de um string.
vTexto = "len"
print(len(vTexto))

# lower() coloca todos os caracteres em minúsculo.
vTexto = "TESTE"
print(vTexto.lower())

# upper() coloca todos os caracteres em maiúsculo.
vTexto = "teste"
print(vTexto.upper())

# str() converte outra variáve em tipo Sting. No exemplo o número 2 se transforma em "2"
vNumero = 2
print(str(vNumero))

# A notação com ponto como em lower e upper é necessária pois estes métodos só funcionam com STRING
# Já os métodos str() e len() fincionam com outros tipos de variáves.


------------------------------------------------------------------------------------
""" 
Quebrar comando longo em linhas - Use \ 
"""

print('This is te longest command line I have ever seen in python \
in my entire life. God, this never endes...')

------------------------------------------------------------------------------------
"""
Operadores Matemáticos
"""

addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9

#Exponenciação
eggs = 10 ** 2
print(eggs)

#Resto da divisão ineteria
RestoDiv = 9 % 2
print (RestoDiv)

------------------------------------------------------------------------------------
"""
Condicionais e Fluxo de Controle

Sinalizadores de comparação

Igual à (==)
Diferente de (!=)
Menor que (<)
Menor igual à (<=)
Maior que (>)
Maior igual à (>=)
"""
------------------------------------------------------------------------------------
"""
Comandos IF e ELIF

A identação é importante em python pois ela delimita o fim do bloco de comando.

SINTAXE -   if condicao:
                comando
            elif condicao2:
                comando
            else:
                comando
"""

num = int(input("Digite um número: "))
if num < 10:
    print("O número digitado é menor que 10")
elif num > 10:
    print("O número digitado é maior que 10")
else:
    print("O número digitado é 10")

------------------------------------------------------------------------------------
"""
FUNÇÕES

As funções podem ter 1 ou mais parâmetros e um retorno, mas NÃO É OBRIGATÓRIO

Sintaxe
def nome_da_funcao(paramtro):
    instruções
    return valor
chamada da função
"""

# Função sem passagem de parâmetros
def teste():
    print("Teste de função")
teste()

# Função com passagem de parâmetros
def teste_parametro(numero):
    numero *= 2
    print("O dobro do número digitado é %s" % (numero))

teste_parametro(10)

# Função com retorno
def mutiplica(num1, num2):
    return num1 * num2

------------------------------------------------------------------------------------
""" 
Laço de Repetição FOR

SINTAXE - for contador in limite: 
               comando a cada contador 
"""

# Para exibir o conteúdo da LISTA, use a variável de controle
names = ['Adam', 'Alex', 'Mariah', 'Martine', 'Columbus']
for item in names:
    print(item)

------------------------------------------------------------------------------------
"""
Laço de Repetição while

SINTAXE -   while condição:
                comando
"""

count = 0
while count < 10:
    print "Ola, sou um while e a contagem e", count
    count += 1

------------------------------------------------------------------------------------
""" 
Comando RANGE 
"""

# O comando range possui 3 formas:
# range(STOP)
x = ['num1', 'num2', 'num3', 'num4', 'num5']
for y in range(3):
    print(x[y])

# range(START, STOP)
x = ['num1', 'num2', 'num3', 'num4', 'num5']
for y in range(1, 4):
    print(x[y])

# range(START, STOP, STEP)
x = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6']
for y in range(1, 6, 2):
    print(x[y])

------------------------------------------------------------------------------------
""" 
Comando JOIN

Usado paea adicionar carcateres aos itens da lista

SINTAXE - 'o que se quer adicionar'.join(variável)
"""
nome = ['Jose, que', 'Maria, que', 'Joao, que', 'Antonia, que nao', 'ninguem']
print(' amava '.join(nome))

------------------------------------------------------------------------------------
"""
Importar bibliotecas
As bibliotecas possuem diversas classes e pode-se importar a biblioteca toda, ou apenas
a classe desejada. 

*** Para mais bibliotecas e funções prontas, cheque o arquivo FUNCOEPREDEFINIDAS.py ***

SINTAXE
importar a bilbioteca toda:
from modulo import *
importar somente algumas classes daquela biblioteca:
from modulo import classe1, classe2, classe3...
"""
# Importar a biblioteca TODA
from datetime*

# Importar a classe datetime da bibioteca datetime Python
from datetime import datetime

------------------------------------------------------------------------------------
"""
Data e Hora.
"""

#Atribuindo a hora atual à uma variavél
datahora = datetime.now() 
print(datahora)

# Desmembrando a data.
print(datahora.year)
print(datahora.month)
print(datahora.day) 

# Formatando data
print("%s/%s/%s" % (datahora.day, datahora.month, datahora.year))

# Desmembrando e fomatando a hora
print("%s:%s:%s" % (datahora.hour, datahora.minute, datahora.second)) 

# Data e hora formatados.
print("%s/%s/%s %s:%s:%s" % (datahora.day, datahora.month, datahora.year, datahora.hour, datahora.minute, datahora.second))