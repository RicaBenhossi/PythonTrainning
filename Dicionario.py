"""
DICIONÁRIO

Comandos e funções referentes a dicionários.
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

# Exibindo Um Dicionário

my_dict = {
    "Name": "Natalia",
    "Age": 31,
    "BDFL": True
}

# Exibe todos os items do Dicionário
print(my_dict.items())

# Exibe somente as CHAVES ou ÍNDICES do Dicionário
print(my_dict.keys())

# EXibe apenas os VALORES das chaves do dicionário
print(my_dict.values())

# Exibe os valores e as chaves com espaço entre eles. A "," separa os valores
for key in my_dict:
    print(key, my_dict[key])