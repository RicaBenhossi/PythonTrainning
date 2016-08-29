"""
LISTAS

tipo de dado que pode armazenar uma coleção de dados (Array).
As listas começam com ÍNDICE 0.
"""

ListaTeste = ['Primeiro item', 'Segundo Item', 'Terceiro Item']
print(ListaTeste[0])
print(ListaTeste[1])
print(ListaTeste[2])


""" Alterando valor de uma posição da lista """
ListaExemplo = ['Item 1', 'Item 2', 'Item 3']
print(ListaExemplo[2])
ListaExemplo[2] = 'Item 3 (ALTERADO)'
print(ListaExemplo[2])


""" Adicionando novos itens à uma lista, criando um novo índice (APPEND) """
ListaExemplo.append('Item 4 (NOVO ITEM)')
print(ListaExemplo[3])


""" Exibindo o tamanho da lista """
print(len(ListaExemplo))
print(ListaExemplo)

""" Fatiamento de Lista - o intervalo vai de X(INCLUSIVE) até Y(EXCLUSIVE), ou seja, 
um intevalo de 2 à 5 exibe os valores de índice 2, 3 e 4. """
mala_de_viagem = ['Camisa', 'Calca', 'Blusa', 'Tenis', 'Bermuda', 'Bone']
print('Fatia1' + str(mala_de_viagem[0:2]))
print('Fatia2' + str(mala_de_viagem[2:3]))
print('Fatia3' + str(mala_de_viagem[4:6]))
print('Fatia4' + str(mala_de_viagem[1:5]))
print('Fatia5' + str(mala_de_viagem[0:4]))


""" O Fatiamento também pode ser feoto em STRING, uma vez que elas nada mais sāo do que
uma lista de caracteres """

#Pegar de um índice até o fim
fatia_string = 'Treinamento Python'
print(fatia_string[12:])

#Pegar do começo até um determinado índice (EXCLUSIVE)
print(fatia_string[:11])

#Pegar um intervalo
print(fatia_string[4:13])

""" Buscando os índices de um determinado item dentro de uma lista (.INDEX) """
mala_de_viagem = ['Camisa', 'Calca', 'Blusa', 'Tenis', 'Bermuda', 'Bone']
print(mala_de_viagem.index('Blusa'))

""" Inserindo um item em um índice específico (.INSERT) """
mala_de_viagem.insert(1, 'Jaqueta')
print(mala_de_viagem[1])


"""
DICIONÁRIO

São listas nas quais não se acessa os valores pelo índice, mas por chaves (KEY)
podendo ser iteiro ou string.

SINTAXE - varável = {'Key1': valor, 'Key2': valor}
"""
pedido = {'Refrigerante': 2, 'X-burguer': 5, 'Batata': 10, 'Sorvete': 1}
print(pedido['Batata'])
x = 'X-burguer'
print(pedido[x])

""" Adicionando novas chaves e atribuindo valores a elas """
menu = {} #Iniciar uma Chave vazia
menu['Salada cesar'] = 10.00
menu['Filet Parmegiana'] = 80.00
menu['Lentrecote'] = 100.00
print('O L\'entrecote custa: ' + str(menu['Lentrecote']))
