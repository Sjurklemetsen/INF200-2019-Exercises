# -*- coding: utf-8 -*-

__author__ = 'Sjur Klemetsen'
__email__ = 'sjkl@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.a = 16807
        self.m = 2**31 - 1
        self.seed = seed

    def rand(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed


class ListRand:
    def __init__(self, numbers):
        self.numbers = numbers
        self.counter = -1

    def rand(self):
        if self.counter >= len(self.numbers) - 1:
            raise RuntimeError
        else:
            self.counter += 1
        return self.numbers[self.counter]


if __name__ == "__main__":
    x = LCGRand(346)
    print(x.rand())
    print(x.rand())

    y = ListRand([2, 6, 7, 8])
    print(y.rand())
    print(y.rand())
