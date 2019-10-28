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

    def limit_walk(self):
        while True:
            if super().get_position() < self.left_limit:
                continue
            elif super().get_position() > self.right_limit:
                continue
            else:
                super().way_home()
            return super().get_steps()


class BoundedSimulation(Simulation):
    def __init__(self, pos, home, seed, left_limit, right_limit):
        super().__init__(self, pos, home, seed)
        self.pos = pos
        self.home = home
        self.seed = seed
        self.left_limit = left_limit
        self.right_limit = right_limit

    def limit_sim(self):
        while True:
            if super().get_position() < self.left_limit:
                continue
            elif super().get_position() > self.right_limit:
                continue
            else:
                super().single_walk()
            return



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
        left_limit : int
            The left boundary of walker movement
        right_limit : int
            The right boundary  of walker movement
        """






if __name__ == "__main__":
    print(f' 20 walks with left boundary 0: '
          f'{[BoundedWalker(0, 20, 0, 20).limit_walk() for i in range(20)]}')
    print(f'20 walks with left boundary -10: '
          f'{[BoundedWalker(0, 20, -10, 20).limit_walk() for i in range(20)]}')
    print(f'20 walks with left boundary -100: '
          f'{[BoundedWalker(0, 20, -100, 20).limit_walk() for i in range(20)]}')
    print(f'20 walks with left boundary -1000: '
          f'{[BoundedWalker(0, 20, -1000, 20).limit_walk() for i in range(20)]}')
    print(f'20 walks with left boundary -10000: '
          f'{[BoundedWalker(0, 20, -10000, 20).limit_walk() for i in range(20)]}')


