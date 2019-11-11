# -*- coding: utf-8 -*-

__author__ = 'Sjur Klemetsen'
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
