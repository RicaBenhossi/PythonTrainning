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

""" Planning a Trip """


def hotel_cost(night):
    return 140 * night


def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475


def rental_car_cost(days):
    if days >= 7:
        return (days * 40) - 50
    elif days >= 3:
        return (days * 40) - 20
    else:
        return days * 40


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


print("O Valor Total da Viagem é de: " + str(trip_cost("Los Angeles", 5, 600)))


###############################################################################
"""
Funções Anônimas


Em Python é avceito Programação Funcional, que permite passar funções como Variáveis
ou Valores. Essas funções não precisam de nome (Função Anônima ou Lambda)
"""

numbers = [10, 33, 21, 4]
print(list(filter(lambda a: a * 2, numbers)))

# Para usar filter e lambda com uma lista, precisa colocar a exibção (print) do conteúdo do filter detro da função LIST.
# Sintaxe: print(list(filter(lamda, lista)))
squares = [x ** 2 for x in range(1, 11)]
print(list(filter(lambda x: x in range(30, 71), squares)))
