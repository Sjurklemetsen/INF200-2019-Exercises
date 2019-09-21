def char_counts(textfilename):
    with open(textfilename, 'r') as file:
        string = file.read()
        counts = []
        utf8_list = []
        for i in string:
            utf8_list.append(ord(i))
        for j in range(256):
            counts.append(utf8_list.count(j))
    return counts


if __name__ == '__main__':

    filename = 'file_stats.py'
    frequencies = char_counts(filename)
    for code in range(256):
        if frequencies[code] > 0:
            character = ''
            if code >= 32:
                character = chr(code)

            print(
                '{:3}{:>4}{:6}'.format(
                    code, character, frequencies[code]
                )
            )
