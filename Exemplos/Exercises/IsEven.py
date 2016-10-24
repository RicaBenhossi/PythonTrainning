"""This program recives a number and return if this number is even or odds."""


def is_even(x):
    """Functio defines whether the number(x) is even or odd."""
    if (x % 2 == 0):
        return True
    else:
        return False

result = {True: 'even', False: 'odd'}
num = int(input('Type the number you want to check: '))
print('the number %s is %s.' % (num, result[is_even(num)]))
