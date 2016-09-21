"""
Este arquivo é para lembrar os comandos mais básicos de python.
Segue abaixo os comandos.
"""

#Exibe algo na tela
print("Hello World")

#Variáveis não precisam de declaração de tipo.
var_inteiro = 6
var_float = 10.87
my_boolean = True

#A identação é importante em python pois ela delimita o fim do bloco de comando.
"""
Exemplo de código com erro IndentationError: expected an indented block
def spam():
eggs = 12
return eggs

print spam()
"""

def spam():
    eggs = 12
    return eggs

print (spam())

#Operadores Matemáticos básicos
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

"""
Strings
"""

vTexto = "Teste de string"

#CUIDADO: o Python interpreta o apóstrofo como fechamento de string. Corriga com \
#Exemplo de código com erro:
"""
vTextoApostrofo = "There's a problem Huston!"
"""
vTextoApostrofo = "There\'s a problemm Huston!"
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

# Pode-se exibir uma stung sem armazená-la m variáveis.
print("Teste de exibição de string sem variável.")

# Concatenação de string
print("Teste" + " de cotatenação " + "de " + "Strings")

# Concatenação/Formatação de String usado % (MELHOR JEITO)
string1 = "Camelot"
string2 = "besta"
print ("Não vamos à %s. É um lugar %s pra dedéu." % (string1, string2))

# Método também funciona com Input.
# **** O método INPUT sempre retorna STRING. É necessário converter para putro tipo se necessário.
nome = input("Qua o seu nome?  ")
idade = input("Qual a sua idade?  ")

print ("Olá %s. Bom saber que você tem %s anos de idade." % (nome, idade))

"""
Importar bibliotecas
As bibliotecas possuem diversas classes e pode-se importar a biblioteca toda, ou apenas
a classe desejada.

sintaxe
importar a bilbioteca toda:
from modulo import *
importar somente algumas classes daquela biblioteca:
from modulo import classe1, classe2, classe3...
"""

# Importar a classe datetime da bibioteca datetime Python
from datetime import datetime

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
"""
Comandos IF e ELIF
"""
# If e Elif (elseif)
num = int(input("Digite um número: "))
if num < 10:
    print("O número digitado é menor que 10")
elif num > 10:
    print("O número digitado é maior que 10")
else:
    print("O número digitado é 10")

""" Quebrar comando longo em linhas - Use \ """
print('This is te longest command line I have ever seen in python \
in my entire life. God, this never endes...')

""" Comando RANGE """

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

""" 
Comando JOIN

Usado paea adicionar carcateres aos itens da lista

SINTAXE - 'o que se quer adicionar'.join(variável)
"""
nome = ['Jose, que', 'Maria, que', 'Joao, que', 'Antonia, que nao', 'ninguem']
print(' amava '.join(nome))
