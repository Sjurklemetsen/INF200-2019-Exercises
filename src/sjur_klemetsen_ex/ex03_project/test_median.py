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


