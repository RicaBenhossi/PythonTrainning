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


"""Adicionando novos itens à uma lista (Criar índices)"""
ListaExemplo.append('Item 4 (NOVO ITEM)')
print(ListaExemplo[3])


"""Exibindo o tamanho da lista"""
print(len(ListaExemplo))
print(ListaExemplo)

"""Fatiamento de Lista"""