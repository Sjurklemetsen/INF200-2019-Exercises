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
    import math
    t = letter_freq(message)
    n = sum(t.values())
    result = 0
    char_occ = {}
    for key, value in t.items():
        char_occ[key] = value / n
    for value in char_occ.values():
        result += (value * math.log2(value)) * - 1
    return result


if __name__ == "__main__":
    for msg in '', 'aaaa', 'aaba', 'abcd', 'This is a short text.':
        print('{:25}: {:8.3f} bits'.format(msg, entropy(msg)))
