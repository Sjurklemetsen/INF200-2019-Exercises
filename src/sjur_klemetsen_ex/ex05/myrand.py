# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        self.a = 16807
        self.m = 2**31 - 1
        self.seed = seed

    def rand(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed
