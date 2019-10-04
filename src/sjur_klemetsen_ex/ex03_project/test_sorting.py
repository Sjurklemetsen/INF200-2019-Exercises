# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'


def bubble_sort(data):
    datalist = list(data)
    for i in range(1, len(datalist)):
        for k in range(0, len(datalist) - i):
            if datalist[k] > datalist[k + 1]:
                datalist[k], datalist[k + 1] = datalist[k + 1], datalist[k]
    return datalist


def test_empty():
    assert bubble_sort([]) == []


def test_single():
    assert bubble_sort([1]) == [1]
