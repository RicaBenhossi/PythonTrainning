""" IMPORTAR BILBIOTECAS E FUNÇÕES """
# Importação Genéricas importa a bilbioteca TODA. Usar sempre BIBLIOTECA.FUNCAO
import math
print(math.sqrt(25))

# Importar função específica: Usar FROM BIBLIOTECA IMPORT FUNCAO
from math import sqrt
print(sqrt(16))

-------------------------------------------------------------------------------
""" FUNÇÕES """

""" Randomizar valores - RANDINT(LOW, HIGH) """
from random import randint
x = randint(1, 9)
print(x)

""" Maior número da sequência """
def biggest_number(*args):
    print (max(args))
    return max(args)
biggest_number(-10, -5, 5, 10)

""" Menor número da sequência """
def smallest_number(*args):
    print (min(args))
    return min(args)
smallest_number(-10, -5, 5, 10)

""" Módulo de um número (distância até 0) """
def distance_from_zero(arg):
    print (abs(arg))
    return abs(arg)
distance_from_zero(-10)

""" Ver o tipo de variável de um dado. """
print(type(2))
print(type(2.8))
print(type("teste"))