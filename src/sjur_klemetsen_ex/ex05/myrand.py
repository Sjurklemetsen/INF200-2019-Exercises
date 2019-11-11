# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'


class LCGRand:
    def __init__(self, seed):
        """
        A random dumber generator
        :param seed:
        """
        self.a = 16807
        self.m = 2 ** 31 - 1
        self.seed = seed

    def rand(self):
        self.seed = (self.a * self.seed) % self.m
        return self.seed

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        """
        :return: RandIter with the length - 1
        """
        return RandIter(self, -1)


class RandIter:
    def __init__(self, random_number_generator, length):
        """
        Class that uses a random generator to generate numbers and check
        for error
        :param random_number_generator: which generator to use
        :param length: How many numbers to generate
        """
        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initiate the generator and raise error if iter is run twice on same
        object
        :return
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError
        self.num_generated_numbers = -1
        return self

    def __next__(self):
        """
        Generate the next number
        """
        self.num_generated_numbers += 1
        if self.num_generated_numbers is None:
            raise RuntimeError
        if self.num_generated_numbers == self.length:
            raise StopIteration
        return self.generator.rand()


if __name__ == "__main__":
    random_number_generator = LCGRand(1)
    for rand in random_number_generator.random_sequence(10):
        print(rand)

    for i, rand in \
            enumerate(random_number_generator.infinite_random_sequence()):
        print(f'The {i}-th random number is {rand}')
        if i > 100:
            break
