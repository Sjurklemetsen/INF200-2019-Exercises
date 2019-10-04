# -*- coding: utf-8 -*-

__author__ = "Sjur Spjeld Klemetsen"
__email__ = "sjkl@nmbu.no"


def median(data):
    sdata = sorted(data)
    n = len(sdata)
    return (sdata[n // 2] if n % 2 == 1
            else 0.5 * (sdata[n // 2 - 1] + sdata[n // 2]))


def test_median_single():
    assert median([4]) == 4


def test_median_odd_numbers():
    odd_numbers = [1, 9, 5, 3, 7]
    assert median(odd_numbers) == 5


def test_median_even_numbers():
    even_numbers = [1, 3, 2, 5, 4, 6]
    assert median(even_numbers) == 3.5


def test_ordered():
    ordered_list = [1, 2, 3, 4, 5]
    assert median(ordered_list) == 3


def test_reversed_ordered():
    reversed_list = [4, 3, 2, 1]
    assert median(reversed_list) == 2.5


def test_unordered():
    unordered_list = [2, 5, 3, 1]
    assert median(unordered_list) == 2.5