import subprocess


def str2brl(string, table):
    '''
    Generates braille unicode characters from input string using character to dot tables
    '''

    p1 = subprocess.Popen(["echo", string], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["lou_translate", "unicode.dis," + table], stdin=p1.stdout,
                          stdout=subprocess.PIPE, universal_newlines=True)
    p1.stdout.close()

    char_lst = p2.communicate()[0].replace(
        ' ', '\\x2800').replace('\\x', '\\u').rstrip('\n')
    char_lst = char_lst.encode().decode('unicode_escape')
    for char in char_lst:
        yield char


def brl2str(brl_chr, table='en-us-compbrl.ctb'):
    '''
    Generates unicode char from backward translation of a braille character using by default a
    standart US computer braille table
    '''
    p1 = subprocess.Popen(["echo", brl_chr], stdout=subprocess.PIPE)
    p2 = subprocess.Popen(["lou_translate", "-b", "unicode.dis,en-us-compbrl.ctb"], stdin=p1.stdout,
                          stdout=subprocess.PIPE, universal_newlines=True)
    p1.stdout.close()

    return p2.communicate()[0]


def byte2brl(byte):
    '''
    Generates unicode braille character from 8 dot byte representation
    '''
    return chr(byte + 0x2800)

if __name__ == "__main__":
    for char in str2brl("Hello world!", "en-GB-g2.ctb"):
        print(char)
        print(brl2str(char))
