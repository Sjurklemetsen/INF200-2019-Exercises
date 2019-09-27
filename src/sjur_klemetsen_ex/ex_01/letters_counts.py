def letter_freq(txt):
    symboler = [item.lower() for item in txt]
    symboler.sort()
    count = []
    for i in symboler:
        a = symboler.count(i)
        count.append(a)
    dicti = dict(zip(symboler, count))
    return dicti


if __name__ == '__main__':
    text = input('Please enter text to analyse: ')

    frequencies = letter_freq(text)
    for letter, count in frequencies.items():
        print('{:3}{:10}'.format(letter, count))
