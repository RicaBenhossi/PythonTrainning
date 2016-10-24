"""This program recives a number and return if this number is even or odds."""


def factorial(x):
    """Functio defines whether the number(x) is even or odd."""
    y = x
    while x > 1:
        y = y * (x - 1)
        x -= 1
    else:
        return y

num = int(input('Type the number you want to see the factorial: '))
print('The factorial of the number %s is %s.' % (num, factorial(num)))
