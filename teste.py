notas = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(scores):
    total = 0
    x = 0
    while x < len(scores):
        total += scores[x]
        x += 1
    print(total)
    return total


def grades_average(grades):
    return (grades_sum(grades) / float(len(grades)))

print(grades_average(notas))
