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


###############################################################################
"""
Funções Anônimas


Python permite Programação Funcional, que permite passar funções como Variáveis 
ou Valores. Essas funções nãoprecisam de nome (Função Anônima)
"""


def by_three(x):
    return x % 3 == 0


print(by_three)

my_list = list(range(0, 16))
print(filter(lambda x: x % 3 == 0, my_list))
