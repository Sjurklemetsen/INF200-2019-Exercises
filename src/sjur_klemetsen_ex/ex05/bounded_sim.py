# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'

from src.sjur_klemetsen_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, pos, home, left_limit, right_limit):
        super().__init__(pos, home)
        self.pos = pos
        self.home = home
        self.left_limit = left_limit
        self.right_limit = right_limit

    def check_limit(self):
        while True:
            if super().get_position() < self.left_limit:
                continue
            elif super().get_position() > self.right_limit:
                continue
            else:
                super().way_home()


if __name__ == "__main__":
    print(f' 20 walks from start 0 to home 10 with seed 12345: '
          f'{[BoundedWalker(0, 20, 0, 20).check_limit() for i in range(20)]}')

