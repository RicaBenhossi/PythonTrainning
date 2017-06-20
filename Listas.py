"""
LISTAS

Comandos e funções relacionadasa listas.
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

###############################################################################
"""
Elaborando listas com uma lógica

Listas podem ser feitas e preenchidas automaticamente de acordo com uma lógica
"""

evens_to_50 = [i for i in range(51) if i % 2 == 0]
print(evens_to_50)

print('A' ^ 'B')


cubes_by_four = [(x ** 3) for x in range(1, 11) if ((x ** 3) % 4 == 0)]
print(cubes_by_four)

###############################################################################
"""
Fatiamento de listas
"""

# Fatiamento de Lista. Padrão list = [INICIO DA LISTA:FIM DA LISTA:PASSO DA LISTA]
# Omitindo Índices
to_five = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']


# Exibe D e E
print(to_five[3:])

# Exibe A e B
print(to_five[:2])

# Exibe A, C, E
print(to_five[::2])

# Exibe
print(to_five[1:8:4])

# Invertendo a lista
backwards = to_five[::-1]
print(backwards)

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
SORTED

Organiza a lista de forma crescente.
SINTAXE - sortred(lista)
"""

lista = [2, 8, 4, 3, 6, 7, 1]
print(sorted(lista))

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
