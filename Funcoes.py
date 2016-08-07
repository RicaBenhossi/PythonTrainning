"""
FUNÇÕES

Sintaxe
def nome_da_funcao(paramtro):
    instruções
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

n1 = int(input("Digite um número"))
n2 = int(input("Digite outro número"))
print("O resultado é: " + str(mutiplica(n1, n2)))

# Função dentro de Função.
def cubo(num):
    return num ** 3

def portres(numero):
    if numero % 3 == 0:
        cubo(numero)
        return cubo(numero)
    else:
        return "False"
print("Função dentro de Função.")
print(portres(3))

"""
Importação de Funções
"""

# Importação genérica
import math
print("Importação genérica")
print(math.sqrt(25))

# Importação de apenas uma função de uma biblioteca
from math import sqrt
print("Importação de apenas uma função de uma biblioteca")
print(sqrt(25))

# Importações Universais
from math import *

""" Algumas funções bem úteis em python """

# Maior número da sequência
def biggest_number(*args):
    print (max(args))
    return max(args)
    
# Menor número da sequência
def smallest_number(*args):
    print (min(args))
    return min(args)

# Módulo de um número (distância até 0)
def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

# Ver o tipo de variável de um dado.
print(type(2))
print(type(2.8))
print(type("teste"))