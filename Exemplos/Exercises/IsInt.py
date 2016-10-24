"""This program recives a number and return if this number is integer or not."""


def is_int(x):
    """Function is_int defines if the number (x) is integer."""
    y = int(x)
    if (x - y != 0):
        return False
    else:
        return True

result = {True: 'is', False: 'is not'}
num = float(input('Type the number to check: '))
print('The number %s %s integer' % (num, result[is_int(num)]))
