# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'

from src.sjur_klemetsen_ex.ex05.walker_sim import Walker, Simulation


class BoundedWalker(Walker):
    def __init__(self, pos, home, left_limit, right_limit):
        super().__init__(pos, home)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def way_home(self):
        while not self.is_at_home():
            self.move()
            if self.get_position() < self.left_limit:
                self.pos = self.left_limit
                self.moves -= 1
            elif self.get_position() > self.right_limit:
                self.pos = self.right_limit
                self.moves -= 1
        return self.get_steps()


class BoundedSimulation(Simulation):
    def __init__(self, pos, home, seed, left_limit, right_limit):
        super().__init__(pos, home, seed)
        self.left_limit = left_limit
        self.right_limit = right_limit

    def single_walk(self):
        walker = BoundedWalker(self.pos, self.home, self.left_limit,
                               self.right_limit)
        return walker.way_home()


if __name__ == "__main__":
    seed = 12345
    print(f'The list for left boundary 0:'
          f'{BoundedSimulation(0, 20, seed, 0, 20).run_simulation(20)}')
    print(f'The list for left boundary -10:'
          f'{BoundedSimulation(0, 20, seed, -10, 20).run_simulation(20)}')
    print(f'The list for left boundary -100:'
          f'{BoundedSimulation(0, 20, seed, -100, 20).run_simulation(20)}')
    print(f'The list for left boundary -1000:'
          f'{BoundedSimulation(0, 20, seed, -1000, 20).run_simulation(20)}')
    print(f'The list for left boundary -10000:'
          f'{BoundedSimulation(0, 20, seed, -10000, 20).run_simulation(20)}')
