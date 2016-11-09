"""This program takes a list of numbers and returns only the even numbers."""


def purify(numbers):
    """Return the evens on a list."""
    evens = []
    x = 0
    while x < len(numbers):
        if ((numbers[x] % 2) == 0):
            evens.append(numbers[x])
        x += 1
    return(evens)

print(purify([1, 2, 3, 4, 5, 6, 7, 8, 9]))
