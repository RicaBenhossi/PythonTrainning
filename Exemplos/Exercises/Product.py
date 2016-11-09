"""This program retuns the product of a itens on a list."""


def product(integers):
    """Return the product."""
    total = 1
    x = 0
    while x < len(integers):
        total *= integers[x]
        x += 1
    return(total)

print(product([5, 5, 2]))