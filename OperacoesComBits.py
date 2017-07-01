"""
OPERAÇÕES EM NÍVEL DE BITS

Operações no nível dos bits são operações que manipulam diretamente os bits.

O Sistema Numérico de Base 2

Quando contamos, geralmente fazemos isso em base 10. Isso significa que cada posição em um número pode ter um de dez valores, 0-9. Em binário,
contamos em base dois, em que cada posição pode ter um de dois valores: 0 ou 1. O padrão de contagem é o mesmo da base 10, exceto quando você "sobe"
um valor para uma nova coluna; em binário, você deve "subir" o valor sempre que uma casa assume um valor maior do que um (o que acontece quando o
valor excede 9 em base 10). Por exemplo, os números um e zero são iguais em base 10 e em base 2. Mas em base 2, quando você chega ao número 2, você
deve "subir" o um, resultando na representação "10". Somar um novamente resulta em "11" (3), e somar um novamente resulta em "100" (4). Ao contrário
da contagem em base 10, em que cada casa decimal representa uma potência de 10, cada casa em um número binário representa uma potência de dois (ou um
bit). O bit mais à direita é o bit dos 1s (dois elevado a zero), o bit seguinte é o bit dos 2's (dois elevado à primeira potência), depois 4, 8, 16,
32, e assim por diante. O número binário "1010" é 10 na base 2, porque o bit dos 8s e o bit dos 2s estão "ligados":
"""
# Operadores de bits

print(5 >> 4)   # Desloca para a Direita >>
print(5 << 1)   # Desloca para a Esquerda <<
print(8 & 5)    # AND no nível dos bits &
print(9 | 4)    # OR no nível dos bits |
print(12 ^ 42)  # XOR no nível dos bits ^
print(~88)      # NOT no nível dos bits ~

# Transformar um número binário em base 10: 0bnúemrobinário

print(0b1)    # 1
print(0b10)   # 2
print(0b11)   # 3
print(0b100)  # 4
print(0b101)  # 5
print(0b110)  # 6
print(0b111)  # 7

print("******")
print(0b1 + 0b11)
print(0b11 * 0b11)

um = 0b1
dois = 0b10
tres = 0b11
quatro = 0b100
cinco = 0b101
seis = 0b110
sete = 0b111
oito = 0b1000
nove = 0b1001
dez = 0b1010
onze = 0b1011
doze = 0b1100

print(um, dois, tres, quatro, cinco, seis, sete, oito, nove, dez, onze, doze)

"""
Função BIN - esta função mostra a forma binária de um número.

Syntaxe: bin(caracter)
"""

print(bin(12))
print(bin(100))
print(bin(999))
print(bin(2))

print(bin(0b011))
print(bin(0b000110))

"""
Função INT - mesma função que transforma uma string em inteiro e que possui um parâmetro opcional, referente à base que este número está

Syntaxe: int(numero, base_desse_número)
"""

# Transforma o número (string) que está na base 2 (binário).
print(int('11', 2))
print(int('111', 2))
print(int(bin(4), 2))

"""
Deslocamento de bits - Desloc os bits de um número um número designado de posições.

SINTAXE:    variável = numero_binário << posições (desloca para a esquerda).
            variável = numero_binário >> posições (desloca para a direita). 

O deslocamento para a ESQUERDA (<<) equivale a uma DIVISÃO por 2 arredondada para o menor inteiro mais próximo.
O deslocamento para a DIREITA (>>) equivale a uma MULTIPLICAÇÃO por 2 arredondada para o menor inteiro mais próximo

*** Note que você só pode realizar operações no nível dos bits em números inteiros. Outras vriáveis resultarão em saídas estranhas.
"""

shift_right = 0b1100
shift_left = 0b1

shift_right_decimal = int(shift_right)
shift_left_decimal = int(shift_left)

# Deslocamento para a direita Multiplicação
shift_right = shift_right >> 2
# Deslocamento para a esquerda divisão.
shift_left = shift_left << 2

print('Shift_right em base decimal: ' + str(shift_right_decimal))
print('Shift_left em base decimal: ' + str(shift_left_decimal))
print('Shift_right em base binária deslocado 2 casas para a DIREITA: ' + str(bin(shift_right)))
print('Shift_right em base decimal deslocado 2 casas para a DIREITA: ' + str(int(shift_right)))
print('Shift_left em base binária deslocado 2 casas para a ESQUERDA: ' + str(bin(shift_left)))
print('Shift_left em base decimal deslocado 2 casas para a ESQUERDA: ' + str(int(shift_left)))


"""
Operador AND &

O opreador & retorna 1 quando os dois números comparados são IGUAIS a 1.

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
"""

nbin1 = 0b1110
nbin2 = 0b101

print(str(int(nbin1)))
print(str(int(nbin2)))

print(bin(nbin1 & nbin2))
print(str(int(nbin1 & nbin2)))

"""
Operador OR |

O opreador | retorna 1 quando QUALQUER UM DOS DOS números comparados são IGUAIS a 1.

0 | 0 = 0
0 | 1 = 1
1 & 0 = 1
1 & 1 = 1
"""

nbin1 = 0b1110
nbin2 = 0b101

print(str(int(nbin1)))
print(str(int(nbin2)))

print(bin(nbin1 | nbin2))
print(str(int(nbin1 | nbin2)))

"""
Operador XOR ^ ou EXCLUSIVO

O opreador ^ retorna 1 quando APENAS UM DOS DOS números comparados são IGUAIS a 1.

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
"""

nbin1 = 0b1110
nbin2 = 0b101

print(str(int(nbin1)))
print(str(int(nbin2)))

print(bin(nbin1 ^ nbin2))
print(str(int(nbin1 ^ nbin2)))

"""
Operador NOT ~

O opreador ~ simplesmente invrerte os bits em un único número, o que equivale à somar 1 à ele e torná-lo negativo.

~0 = -1
~1 = -2
~10 = -11
~(-9) = 8
-(~9) = 10
"""

print(~10)
print(~(-10))
print(-(~10))