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
