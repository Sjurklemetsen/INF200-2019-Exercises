# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'

import random as rd


class Walker:
    def __init__(self, pos, home):
        """
            Class for a walk home from samfunnet
            :param pos: int, starting position
            :param home: int, end position
        """
        self.pos = pos
        self.home = home
        self.moves = 0

    def move(self):
        """
        Method that lets you move one step forward or behind
        """
        self.moves += 1
        i = rd.randint(1, 2)
        if i == 1:
            self.pos += 1
        else:
            self.pos -= 1

    def is_at_home(self):
        """
        Check if check if you are home.
        :return: True
        """
        if self.pos == self.home:
            return True

    def get_position(self):
        """
        :return: Current position
        """
        return self.pos

    def get_steps(self):
        """
        Method that checks how many moves
        :return: moves
        """
        return self.moves

    def way_home(self):
        """
        Method that let you walk all the way home
        :return: moves
        """
        while not self.is_at_home():
            self.move()
        return self.moves


class Simulation:
    def __init__(self, pos, home, seed):
        """
        This class simulates a 1D walk from pos to home
        :param pos: int, starting position
        :param home: int, end position
        :param seed: seed for the random number generator
        """
        self.pos = pos
        self.home = home
        rd.seed(seed)

    def single_walk(self):
        """Performs a single walk and returns steps taken"""
        return Walker(self.pos, self.home).way_home()

    def run_simulation(self, num_walks):
        """
        :param num_walks: How many simulations you want to run
        :return: List with with number of steps for each walk home
        """
        return [self.single_walk() for _ in range(num_walks)]


if __name__ == "__main__":
    print(f' 20 walks from start 0 to home 10 with seed 12345: '
          f'{Simulation(0, 10, 12345).run_simulation(20)}')
    print(f' 20 walks from start 0 to home 10 with seed 12345: '
          f'{Simulation(0, 10, 12345).run_simulation(20)}')
    print(f' 20 walks from start 10 to home 0 with seed 12345: '
          f'{Simulation(10, 0, 12345).run_simulation(20)}')
    print(f' 20 walks from start 10 to home 0 with seed 12345: '
          f'{Simulation(10, 0, 12345).run_simulation(20)}')
    print(f' 20 walks from start 0 to home 10 with seed 54321: '
          f'{Simulation(0, 10, 54321).run_simulation(20)}')
    print(f' 20 walks from start 10 to home 0 with seed 54321: '
          f'{Simulation(10, 0, 54321).run_simulation(20)}')
