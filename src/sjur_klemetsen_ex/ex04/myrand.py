# -*- coding: utf-8 -*-

__author__ = 'Sjur Klemetsen'
__email__ = 'sjkl@nmbu.no'


class LCGRand:

    def __init__(self, seed):
        self.a = 16807
        self.m = 2**31 - 1
        self.seed = seed

    def rand(self):
        while True:
            self.seed = (self.a * self.seed) % self.m
            return self.seed


class ListRand:

    def __init__(self, numbers):
        self.numbers = numbers

    def rand(self):
        for el in self.numbers:
            yield el
