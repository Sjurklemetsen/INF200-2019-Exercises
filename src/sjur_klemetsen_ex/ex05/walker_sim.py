# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'

import random as rd


class Walker:
    def __init__(self, pos, home):
        self.pos = pos
        self.home = home
        self.moves = 0

    def move(self):
        self.moves += 1
        i = rd.randint(1, 2)
        if i == 1:
            self.pos += 1
        else:
            self.pos -= 1

    def is_at_home(self):
        if self.pos == self.home:
            return True

    def get_position(self):
        return self.pos

    def get_steps(self):
        return self.moves

    def way_home(self):
        while not self.is_at_home():
            self.move()
        return self.moves


class Simulation:

    def __init__(self, start, home, seed):

        self.start = start
        self.home = home
        self.seed = seed

        """
        Initialise the simulation

        Arguments
        ---------
        start : int
            The walker's initial position
        home : int
            The walk ends when the walker reaches home
        seed : int
            Random generator seed
        """

    def single_walk(self):
        """
                Simulate single walk from start to home, returning number of steps.

                Returns
                -------
                int
                    The number of steps taken
                """
        return Walker(0, 1).way_home()


    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        Arguments
        ---------
        num_walks : int
            The number of walks to simulate

        Returns
        -------
        list[int]
            List with the number of steps per walk
        """
        return [Walker(0, 1).way_home() for i in range(num_walks)]




if __name__ == "__main__":
    print(f' Distance : 1 -> Path lengths : '
          f'{[Walker(0, 1).way_home() for i in range(5)]}')
    print(f' Distance : 2 -> Path lengths :'
          f' {[Walker(1, 2).way_home() for i in range(5)]}')
    print(f' Distance : 5 -> Path lengths :'
          f' {[Walker(1, 5).way_home() for i in range(5)]}')
    print(f' Distance : 10 -> Path lengths :'
          f' {[Walker(1, 10).way_home() for i in range(5)]}')
    print(f' Distance : 10 -> Path lengths :'
          f' {[Walker(1, 20).way_home() for i in range(5)]}')
    print(f' Distance : 10 -> Path lengths :'
          f' {[Walker(1, 50).way_home() for i in range(5)]}')
    print(f' Distance : 10 -> Path lengths :'
          f' {[Walker(1, 100).way_home() for i in range(6)]}')

