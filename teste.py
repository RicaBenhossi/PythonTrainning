
def reverse(text):
    y = len(text)
    for x in text:
        revtext[y] = x
        y -= 1
    return revtext

x = input(str('Type the textbyou want to reverse: '))
print(reverse(x))
