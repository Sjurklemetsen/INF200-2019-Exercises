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

class RandIter(LCGRand):
    def __init__(self, random_number_generator, length):
        super().__init__(self.seed)
        self.random_number_generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        self.num_generated_numbers = self.random_number_generator
        if self.num_generated_numbers
        return self.num_generated_numbers




    def __next__(self):
        for i in range(self.length):
            self




if __name__ == "__main__":
