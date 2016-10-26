"""This program takes out the vowel of you string."""


def anti_vowel(text):
    """Function takes out thr vowels of a word."""
    x = 0
    NoVowel = ''
    while (x < len(text)):
        if (text[x] not in 'aeiouAEIOU'):
            NoVowel = NoVowel + text[x]
        x += 1
    else:
        return NoVowel

x = str(input('Type the text you want to take the vowels out: '))
print('The result is %s.' % (anti_vowel(x)))
    