"""
LAÇOS DE REPETIÇÃO

Tipos e modelos de Estruturas de Repetição
"""

###############################################################################
"""
FOR

SINTAXE - for contador in limite:
               comando a cada contador
"""

# Para exibir o conteúdo da LISTA, use a variável de controle
names = ['Adam', 'Alex', 'Mariah', 'Martine', 'Columbus']
for item in names:
    print(item)

###############################################################################
"""
FOR / ELSE

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
WHILE

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
WHILE / ELSE

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
