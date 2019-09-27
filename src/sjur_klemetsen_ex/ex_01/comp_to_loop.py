def squares_by_comp(n):
    return [k**2 for k in range(n) if k % 3 == 1]


def squares_by_loop(n):
    liste = []
    for k in range(n):
        if k % 3 == 1:
            liste.append(k**2)
    return liste


if __name__ == '__main__':
    if squares_by_comp(20) != squares_by_loop(20):
        print('ERROR')
