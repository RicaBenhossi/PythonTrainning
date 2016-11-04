"""This program take a phrase and hide under * the word you choose."""


def censor(text, word):
    """Change the word you choos for * in the phrase."""
    x = '*' * len(word)
    text = text.split(' ')
    while word in text:
        text[text.index(word)] = x
    print(' '.join(text))

phrase = str(input('Type the phrase: '))
substword = str(input('Type the word you want to hide: '))
censor(phrase, substword)
