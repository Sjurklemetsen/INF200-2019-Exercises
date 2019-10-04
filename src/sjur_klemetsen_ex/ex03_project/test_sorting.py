# -*- coding: utf-8 -*-

__author__ = "Sjur Spjeld Klemetsen"
__email__ = "sjkl@nmbu.no"


from hypothesis import given, strategies


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


def test_sorted_is_not_original():
    data = [3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data != data


def test_original_unchanged():
    data = [3, 2, 1]
    bubble_sort(data)
    assert data == data


def test_sort_sorted():
    data = [1, 2, 3]
    sorted_data = bubble_sort(data)
    assert sorted_data == data


def test_sorted_reversed():
    data = [4, 3, 2, 1]
    sorted_data = bubble_sort(data)
    assert sorted_data == [1, 2, 3, 4]


def test_sort_all_equal():
    data = [2, 2, 2, 2]
    sorted_data = bubble_sort(data)
    assert sorted_data == [2, 2, 2, 2]


@given(strategies.lists(strategies.integers()))
def test_sorting(int_list):
    sorted_data = bubble_sort(int_list)
    for small, large in zip(sorted_data[:-1], sorted_data[1:]):
        assert small <= large
