"""
LISTAS

tipo de dado que pode armazenar uma coleção de dados (Array).
As listas começam com ÍNDICE 0.
"""

ListaTeste = ['Primeiro item', 'Segundo Item', 'Terceiro Item']
print(ListaTeste[0])
print(ListaTeste[1])
print(ListaTeste[2])


"""Alterando valor de uma posição da lista"""
ListaExemplo = ['Item 1', 'Item 2', 'Item 3']
print(ListaExemplo[2])
ListaExemplo[2] = 'Item 3 (ALTERADO)'
print(ListaExemplo[2])


"""Adicionando novos itens à uma lista, criando um novo índice (APPEND)"""
ListaExemplo.append('Item 4 (NOVO ITEM)')
print(ListaExemplo[3])


"""Exibindo o tamanho da lista"""
print(len(ListaExemplo))
print(ListaExemplo)

"""Fatiamento de Lista - o intervalo vai de X(INCLUSIVE) até Y(EXCLUSIVE), ou seja, 
um intevalo de 2 à 5 exibe os valores de índice 2, 3 e 4."""
mala_de_viagem = ['Camisa', 'Calca', 'Blusa', 'Tenis', 'Bermuda', 'Bone']
print('Fatia1' + str(mala_de_viagem[0:2]))
print('Fatia2' + str(mala_de_viagem[2:3]))
print('Fatia3' + str(mala_de_viagem[4:6]))
print('Fatia4' + str(mala_de_viagem[1:5]))
print('Fatia5' + str(mala_de_viagem[0:4]))