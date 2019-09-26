def bubble_sort(data):
    datalist = list(data)
    for i in range(1, len(datalist)):
        for k in range(0, len(datalist) - i):
            if datalist[k] > datalist[k + 1]:
                datalist[k], datalist[k + 1] = datalist[k + 1], datalist[k]
    return datalist


if __name__ == "__main__":

    for data in ((),
                 (1,),
                 (1, 3, 8, 12),
                 (12, 8, 3, 1),
                 (8, 3, 12, 1)):
        print('{!s:>15} --> {!s:>15}'.format(data, bubble_sort(data)))
