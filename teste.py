def product(integers):
    total = 1
    x = 0
    while x < len(integers):
        total *= integers[x]
        x += 1
    return(total)

print(product([5, 5, 2]))
