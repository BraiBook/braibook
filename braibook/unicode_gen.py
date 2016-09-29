from .tables import LATIN


def braille_unicode_gen(string):
    '''
    Generates braille unicode characters using character to dot tables
    '''

    for char in string:
        dot_binary = 0
        for dot in range(1, 9):
            if str(dot) in str(LATIN[char]):
                dot_binary += (1 << dot - 1)
        yield chr(0x2800 + dot_binary)
