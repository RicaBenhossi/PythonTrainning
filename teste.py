


def censor(text, word):
    x = '*' * len(word)
    text.split(' ')
    for word in text:
        text.index(word)
    print(' '.join(text))

phrase = str(input('Type the phrase: '))
substword = str(input('Type the word you want to hide: '))
censor(phrase, substword)


