"""This program shows a text in a reverse mode."""


def reverse(text):
    """Recive a text and return its reverse."""
    y = len(text)
    revtext = ''
    while (y > 0):
        y -= 1
        revtext = revtext + text[y]
    return revtext.upper()

txt = input(str('Type the text you want to reverse: '))
print('The reverse form of %s is %s' % (txt.upper(), reverse(txt)))
