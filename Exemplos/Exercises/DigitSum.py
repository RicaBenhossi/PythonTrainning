"""This program takes a digit and returns the sum of its digits until 1."""


def digit_sum(n):
    """Take the digit informed and returns the sum of its digits until 1."""
    n = str(n)
    y = 0
    for x in range(len(n)):
        y += int(n[x])
    return y

num = int(input('Type the number you want to sum: '))
print('The sum of the digitis of the number %s is %s.' % (num, digit_sum(num)))
