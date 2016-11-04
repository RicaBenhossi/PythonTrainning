"""This program counts how many times a caracter show on a list."""


def count(sequence, item):
    """Search the list sequence looking for the content of item."""
    quantities_of_item = 0
    x = 0
    while (x < len(sequence)):
        if (sequence[x] == item):
            quantities_of_item += 1
        x += 1
    return quantities_of_item

print(count([1, 2, 3, 4, 1, 5, 1, 1], 1))
