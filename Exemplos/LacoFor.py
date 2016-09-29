""" Laço de Repetição FOR

SINTAXE - for contador in limite: 
               comando a cada contador 
"""

""" Laços de Repetição com Dicionários e Listas """
# Para exibir o conteúdo da LISTA, use a variável de controle
names = ['Adam', 'Alex', 'Mariah', 'Martine', 'Columbus']
for item in names:
    print(item)

# Para exibir o conteúdo do DICIONÁRIO, use a variável de controle como CHAVE.
nefil = {'João': 11, 'Maria': 6, 'Lara': 1}
for age in nefil:
    print(nefil[age])

""" Os laços podem conter várias instruções e podems estar dentro de funções """
def fizz_count(x):
    count = 0
    for y in x:
        if (y == 'fizz'):
            count += 1
    return count
print(fizz_count(['fizz', 'cat', 'fizz', 'dog', 'monkey', 'fizz', 'fizzz']))

""" Percorrendo um String """
def count_E(sentence):
    count = 0
    for letterE in sentence:
        if (letterE == 'e'):
            count += 1
    return count
print('The number of letters E on the sentence: \
\'This is the most interesting exemple of counting letter E on the sentence\' is:')
print(count_E('This is the most interesting exemple of counting letter E on the sentence'))