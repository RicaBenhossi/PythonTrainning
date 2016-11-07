
def purify(numbers):
    evens = []
    for x in enumerate(numbers):
        if ((numbers[x] % 2) == 0):
            evens.append(numbers[x])
        x += 1
    return(evens)

print(purify([1, 2, 3, 4, 5, 6, 7, 8, 9]))