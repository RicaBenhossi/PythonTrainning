"""
Este arquivo é para lembrar os comandos mais básicos de python.
Segue abaixo os comandos.
"""
###############################################################################

"""
Exibe algo na tela

SINTAXE - print(O_que_se_deseja_exibir)
"""

print('Hello World')

# Concatenação de string
print('Teste' + ' de cotatenação ' + 'de ' + 'Strings')

# Concatenação/Formatação de String usado % (MELHOR JEITO)
string1 = 'Camelot'
string2 = 'besta'
print('Não vamos à %s. É um lugar %s pra dedéu.' % (string1, string2))

# Ao colocar , (vírgula) pode-se dar o comando com mais de uma variável
x = 'teste de print '
y = 'com virgula.'
print(x, y)

###############################################################################
"""
Quebrar comando longo em linhas - Use \
"""

print('This is te longest command line I have ever seen in python \
in my entire life. God, this never endes...')

###############################################################################
"""
Operadores Matemáticos
"""

addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9

# Exponenciação
eggs = 10 ** 2
print(eggs)

# Resto da divisão ineteria
RestoDiv = 9 % 2
print(RestoDiv)

###############################################################################
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

###############################################################################
"""
Variáveis não precisam de declaração de tipo.
"""

vInteiro = 6
vFloat = 10.87
vBooleano = True
vLista = ['item 1', 'item2']  # ARRAY
vDicionario = {'Item1 ': 10, 'Item2': 50}  # ARRAY com Índices
vString = 'Essa é uma String'
# CUIDADO: o Python interpreta o apóstrofo como fechamento de string.
# Corriga com \
# Exemplo de código com erro: vTextoApostrofo = 'There's a problem Huston!''

vTextoApostrofo = 'There\'s a problemm Huston!'
print(vTextoApostrofo)

# O índice de caracteres do Python começa com 0.
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

###############################################################################
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

# str() converte outra variáve em tipo Sting. No exemplo o número 2 se
# transforma em "2"
vNumero = 2
print(str(vNumero))

# A notação com ponto como em lower e upper é necessária pois estes métodos
# só funcionam com STRING
# Já os métodos str() e len() fincionam com outros tipos de variáves.

"""
SPLIT

O comando split separa o conteúdo da string no ponto onde encontra o caracter
setado como parâmetro, transformando em uma lista.
SINTAXE: variável.split('parametro')
"""

text = 'Test of command split on a string'
print(text.split(' '))

###############################################################################
"""
Data e Hora
"""

# Atribuindo a hora atual à uma variavél
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
print("%s/%s/%s %s:%s:%s" % (datahora.day, datahora.month, datahora.year,
                             datahora.hour, datahora.minute, datahora.second))

###############################################################################
"""
LISTAS
"""

# Alterando valor de uma posição da lista
ListaExemplo = ['Item 1', 'Item 2', 'Item 3']
print(ListaExemplo[2])
ListaExemplo[2] = 'Item 3 (ALTERADO)'
print(ListaExemplo[2])


# Adicionando novos itens à uma lista, criando um novo índice (APPEND)
ListaExemplo.append('Item 4 (NOVO ITEM)')
print(ListaExemplo[3])

# Removendo um item da lista (.REMOVE )
ListaExemplo = ['Item 1', 'Item 2', 'Item 3']
ListaExemplo.remove('Item 1')

# Removendo um item da lista pelo ÍNDICE (.POP)
ListaExemplo = ['Item 1', 'Item 2', 'Item 3']
ListaExemplo.pop(1)
print(ListaExemplo)

# Exibindo o tamanho da lista
print(len(ListaExemplo))
print(ListaExemplo)

# Fatiamento de Lista - o intervalo vai de X(INCLUSIVE) até Y(EXCLUSIVE),
# ou seja, um intevalo de 2 à 5 exibe os valores de índice 2, 3 e 4.
mala_de_viagem = ['Camisa', 'Calca', 'Blusa', 'Tenis', 'Bermuda', 'Bone']
print('Fatia1' + str(mala_de_viagem[0:2]))
print('Fatia2' + str(mala_de_viagem[2:3]))
print('Fatia3' + str(mala_de_viagem[4:6]))
print('Fatia4' + str(mala_de_viagem[1:5]))
print('Fatia5' + str(mala_de_viagem[0:4]))

# O Fatiamento também pode ser feito em STRING, uma vez que elas nada mais sāo
# do que uma lista de caracteres

# Pegar de um índice até o fim
fatia_string = 'Treinamento Python'
print(fatia_string[12:])

# Pegar do começo até um determinado índice (EXCLUSIVE)
print(fatia_string[:11])

# Pegar um intervalo
print(fatia_string[4:13])

# Buscando os índices de um determinado item dentro de uma lista (.INDEX)
mala_de_viagem = ['Camisa', 'Calca', 'Blusa', 'Tenis', 'Bermuda', 'Bone']
print(mala_de_viagem.index('Blusa'))

# Inserindo um item em um índice específico (.INSERT)
mala_de_viagem.insert(1, 'Jaqueta')
print(mala_de_viagem[1])

###############################################################################
"""
ENUMERATE

ENUMERATE fornece um índice correspondente a cada elemento na lista que você
está percorrendo

SINTAXE - enumarate(variável)
"""

choices = ['pizza', 'massa', 'salada', 'nachos']

print('Suas opcoes sao:')
for index, item in enumerate(choices):
    print(index + 1, item)

###############################################################################
"""
ZIP

ZIP permite percorre duas ou mais listas simultaneamente. Ele criará pares de
elementos quando são usadas várias listas, e param no fim da lista mais curta.

SINTAXE - for a,b in zip(lista1, lista2)
              commando
"""

list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print(a)
    else:
        print(b)

###############################################################################
"""
DICIONÁRIO
"""

# Adicionando novas chaves e atribuindo valores a elas
menu = {}  # Iniciar uma Chave vazia
menu['Salada cesar'] = 10.00
menu['Filet Parmegiana'] = 80.00
menu['Lentrecote'] = 100.00
print('O L\'entrecote custa: ' + str(menu['Lentrecote']))

# Remover uma chave (DEL)
animais_do_zoo = {'Unicornio': 'Casa de Algodao Doce',
                  'Preguica': 'Exibicao da Floresta Tropical',
                  'Tigre de Bengala': 'Casa da Selva',
                  'Fradinho do Atlantico': 'Exibicao Artica',
                  'Pinguim Saltador da Rocha': 'Exibicao Artica'}
print(animais_do_zoo)
print()
del animais_do_zoo['Fradinho do Atlantico']
animais_do_zoo['Leao'] = 'Safari Park'
print(animais_do_zoo)

# Pode-se utilizar Listas dentro de Dicionários
inventory = {
    'gold': 500,
    'pouch': ['silex', 'barbante', 'pedra preciosa'],
    'backpack': ['xilofone', 'adaga', 'saco de dormir', 'pedaco de pao'],
    'Comida': {'Salsicha': 3, 'Bacon': 8, 'Feijao': 4, 'Coca Cola': 10}}
inventory['pocket'] = ['concha', 'amora estranha', 'sujeira']
inventory['backpack'].sort()
inventory['backpack'].remove('adaga')
inventory['gold'] += 50
print(inventory)

###############################################################################
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


###############################################################################
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
LAÇO DE REPETIÇÃO FOR

SINTAXE - for contador in limite:
               comando a cada contador
"""

# Para exibir o conteúdo da LISTA, use a variável de controle
names = ['Adam', 'Alex', 'Mariah', 'Martine', 'Columbus']
for item in names:
    print(item)

###############################################################################
"""
LAÇO DE REPETIÇÃO FOR / ELSE

Similar ao IF/ELSE mas nesse caso o else SÓ SERÁ EXECUTADO SE O FOR EXECUTAR
INTEIRO. Se houver um BREAK por exemplo ele não será executado.
SINTAXE -   for contador in limite:
                comando a cada contador
            else:
                commando
"""

fruits = ['banana', 'maca', 'laranja', 'vagem', 'pera', 'uva']

print('Voce tem...')
for f in fruits:
    if f == 'vagem':
        print('O vagem nao e uma fruta!')
    print('A', f)
else:
    print('Uma excelente selecao de frutas!')

###############################################################################
"""
LAÇO DE REPETIÇÃO WHILE

SINTAXE -   while condição:
                comando
"""

count = 0
while count < 10:
    print('Ola, sou um while e a contagem e', str(count))
    count += 1

# Pode ter uma condição mais dinâmica como no exemplo abaixo
resposta = input('Gosta de Goiaba? (s/n): ').upper()
while (resposta != 'n' and resposta != 's'):
    resposta = input('Responda s para SIM e n pra NÃO. Digite novamente.')
print('Resposta registrada')

###############################################################################
"""
LAÇO DE REPETIÇÃO WHILE / ELSE

Similar ao IF/ELSE mas nesse caso o else SEMPRE SERÁ EXECUTADO AO FIM DO WHILE
SINTAXE -   while condição:
                comando
            else:
                comando
"""

count = 0
while count < 10:
    print('Ola, sou um while e a contagem e', count)
    count += 1
else:
    print('Depois de executado, cai no ELSE')

###############################################################################
"""
Comando BREAK

O comando BREAK serve para interromper a execução de um laço.
"""
x = 0
while x < 10:
    if (x * 2 == 8):
        print('parou no BREAK')
        break
    else:
        print('Passou fora do break')
        x += 1

###############################################################################
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

###############################################################################
"""
Comando JOIN

Usado para adicionar carcateres aos itens da lista

SINTAXE - 'o que se quer adicionar'.join(variável)
"""
nome = ['Jose, que', 'Maria, que', 'Joao, que', 'Antonia, que nao', 'ninguem']
print(' amava '.join(nome))

###############################################################################
"""
Importar bibliotecas
As bibliotecas possuem diversas classes e pode-se importar a biblioteca toda,
ou apenas a classe desejada.
*** Para mais bibliotecas e funções prontas, cheque o arquivo
    FUNCOEPREDEFINIDAS.py ***

SINTAXE
importar a bilbioteca toda:
from modulo import *
importar somente algumas classes daquela biblioteca:
from modulo import classe1, classe2, classe3...
"""
# Importar a biblioteca TODA
from datetime *

# Importar a classe datetime da bibioteca datetime Python
from datetime import datetime

###############################################################################
