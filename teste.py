def is_prime(x):
    x = float(x)
    y = x
    while (y > 2):
        if (x % (y - 1) == 0):
            return False
            break
        y -= 1
    else:
        return True

resultado = {True: 'e', False: 'nao e'}
num = 0
while (num < 1):
    num = int(input('Digite o numero: '))
    if (num == 0):
        print('Digite um numero maior que 0.')
else:
    print('O numero %s %s primo.' % (num, resultado[is_prime(num)]))
