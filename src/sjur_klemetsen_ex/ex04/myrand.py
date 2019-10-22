# -*- coding: utf-8 -*-

__author__ = 'Sjur Klemetsen'
__email__ = 'sjkl@nmbu.no'


class LCGRand:

    def _init__(self, seed):
        self.a = 16807
        self.m = 2 ^ 31 - 1
        self.seed = None

    def rand(self):
        r = self.seed
        while True:
            r = (self.a * r % self.m)
            yield r

class ListRand:
# #def __init__(self):

if __main__