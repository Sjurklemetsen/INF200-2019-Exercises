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

    def single_walk(self):
        rd.seed(self.seed)
        return self.seed(Walker(self.start, self.home).way_home())

    def run_simulation(self, num_walks):
        rd.seed(self.seed)
        return [Walker(self.start, self.home).way_home()
                for i in range(num_walks)]


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
