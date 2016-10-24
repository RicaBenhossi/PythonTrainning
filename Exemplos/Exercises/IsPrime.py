"""This program recives a number and says if this number is prime or not."""


def is_prime(x):
    """Define wheter the number (x) is prime."""
    y = (x - 1)
    if (y > 1):
        while (y > 1):
            if ((x % y) == 0):
                return False
                break
            y -= 1
        else:
            return True
    elif (x == 2):
        return True
    else:
        return False
result = {True: 'is', False: 'is not'}
num = int(input('Type the number you want ro checko: '))
print('The number %s %s prime.' % (num, resultado[is_prime(num)]))
