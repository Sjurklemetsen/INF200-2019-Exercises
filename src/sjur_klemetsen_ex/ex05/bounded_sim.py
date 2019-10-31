# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'

from src.sjur_klemetsen_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, pos, home, left_limit, right_limit):
        super().__init__(pos, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def lim_walk(self):
        while not self.is_at_home():
            super().move()
            if super().get_position() < self.left_limit:
                self.pos = self.left_limit
                self.moves -= 1
            elif super().get_position() > self.right_limit:
                self.pos = self.right_limit
                self.moves -= 1
        return super().get_steps()


class BoundedSimulation(Simulation):
    def __init__(self, pos, home, seed, left_limit, right_limit):
        super().__init__(pos, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def lim_sim(self):
        sim_walker = BoundedWalker(self.pos, self.home,
                                   self.left_limit, self.right_limit)
        return sim_walker.way_home()


if __name__ == "__main__":
    print(f'The list for left boundary 0:'
          f'{[BoundedSimulation(0, 20, 12, 0, 20).lim_sim() for _ in range(20)]}')
    print(f'The list for left boundary 0:'
          f'{[BoundedSimulation(0, 20, 12, -10, 20).lim_sim() for _ in range(20)]}')
    print(f'The list for left boundary 0:'
          f'{[BoundedSimulation(0, 20, 12, -100, 20).lim_sim()for _ in range(20)]}')
    print(f'The list for left boundary 0:'
          f'{[BoundedSimulation(0, 20, 12, -1000, 20).lim_sim() for _ in range(20)]}')
    print(f'The list for left boundary 0:'
          f'{[BoundedSimulation(0,20, 12, -10000, 20).lim_sim() for _ in range(20)]}')
