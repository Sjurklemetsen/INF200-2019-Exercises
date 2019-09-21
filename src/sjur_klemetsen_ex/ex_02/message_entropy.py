def letter_freq(txt):
    symboler = [item.lower() for item in txt]
    symboler.sort()
    count = []
    for i in symboler:
        a = symboler.count(i)
        count.append(a)
    dicti = dict(zip(symboler, count))
    return dicti


def entropy(message):
    t = letter_freq(message)
    n = sum(t.values())
    n_i = sum(t.keys())
    p_i = n_i / n







if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))