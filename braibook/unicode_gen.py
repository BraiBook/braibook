import subprocess


def braille_unicode_gen(string):
    '''
    Generates braille unicode characters using character to dot tables
    '''

    p1 = subprocess.Popen(["echo", string], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["lou_translate", "unicode.dis,en-GB-g2.ctb"], stdin=p1.stdout,
                          stdout=subprocess.PIPE, universal_newlines=True)
    p1.stdout.close()

    char_lst = p2.communicate()[0].replace(
        ' ', '\\x2800').replace('\\x', '\\u').rstrip('\n')
    char_lst = char_lst.encode().decode('unicode_escape')
    for char in char_lst:
        yield char

if __name__ == "__main__":
    for char in braille_unicode_gen("Hello world!"):
        print(char)
