def median(numbers):
    numbers = sorted(numbers)
    position = int(len(numbers) / 2)
    if ((position % 2) != 0):
        return((numbers[position] + numbers[position - 1]) / 2)
    else:
        return(numbers[position])

print(median([7, 12, 3, 1, 6]))