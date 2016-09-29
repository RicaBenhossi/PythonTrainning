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

""" Planning a Trip """

def hotel_cost(night):
    return 140 * night
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city ==  "Pittsburgh":
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

print ("O Valor Total da Viagem é de: " + str(trip_cost("Los Angeles", 5, 600)))