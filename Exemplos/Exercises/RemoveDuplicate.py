"""This program removes duplication in a list."""


def remove_duplicates(numbers):
    """Remove the duplicate."""
    x = 0
    while (x < len(numbers)):
        y = x + 1
        while (y < len(numbers)):
            if (numbers[x] == numbers[y]):
                numbers.pop(y)
            else:
                y += 1
        x += 1
    return(numbers)

print(remove_duplicates([5, 5, 2, 3, 1, 3, 5]))
