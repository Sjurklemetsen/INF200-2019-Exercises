# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import random as rd


class Board:
    """
    This class manage all information about ladders, snakes and
    if the goal has been reached.
    """
    def __init__(self, *args, **kwargs):
        self.ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
        self.snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
        self.board = [x for x in range(1, 91)]

    def goal_reached(self, position):
        """
        :return: True or False depending if you have reached the goal or not
        """
        if position >= len(self.board):
            return True
        else:
            return False

    def position_adjustment(self, position):
        """
        :param position: Position on the board
        :return: The number of positions you skip if you land on a certain
        snake or ladder. If position is not on any ladder or snake
        it returns 0.
        """
        for (key1, value1), (key2, value2) in zip(self.ladder.items(),
                                                  self.snakes.items()):
            if position == key1:
                return value1 - key1
            elif position == key2:
                return value2 - key2
            else:
                continue
        return 0


class Player:
    """
    Manages information about a players position, including which board the
    player is on.
    """
    def __init__(self, board):
        self.board = board
        self.pos = 0
        self.num_moves = 0

    def move(self):
        """
        Moves a player with a dice on the board
        :return: Doesnt return anything
        """
        roll = rd.randint(1, 6)
        self.pos += roll
        for (key1, value1), (key2, value2) in zip(Board().ladder.items(),
                                                  Board().snakes.items()):
            if self.pos == key1:
                self.pos = value1
            elif self.pos == key2:
                self.pos = value2
            else:
                continue
        self.num_moves += 1


class ResilientPlayer(Player):
    """

    """
    def __init__(self, board, extra_steps=None):
        super().__init__(board)
        self.extra_steps = extra_steps
        if self.extra_steps is None:
            self.extra_steps = 1
        self.hit_snake = False

    def move(self):
        roll = rd.randint(1, 6)
        self.pos += roll
        if self.hit_snake:
            self.pos += self.extra_steps
            self.hit_snake = False
        for (key1, value1), (key2, value2) in zip(Board().ladder.items(),
                                                  Board().snakes.items()):
            if self.pos == key1:
                self.pos = value1
            elif self.pos == key2:
                self.pos = value2
                self.hit_snake = True
            else:
                continue
        self.num_moves += 1


class LazyPlayer(Player):
    def __init__(self, board, dropped_steps=None):
        super().__init__(board)
        self.drop_steps = dropped_steps
        self.hit_ladder = False
        if self.drop_steps is None:
            self.drop_steps = 1

    def move(self):
        roll = rd.randint(1, 6)
        self.pos += roll

        if self.hit_ladder:
            if roll >= self.drop_steps:
                self.pos -= self.drop_steps
                self.hit_ladder = False
            else:
                self.hit_ladder = False

        for (key1, value1), (key2, value2) in zip(Board().ladder.items(),
                                                  Board().snakes.items()):
            if self.pos == key1:
                self.pos = value1
                self.hit_ladder = True
            elif self.pos == key2:
                self.pos = value2
            else:
                continue
        self.num_moves += 1


class Simulation:
    def __init__(self, player_field, seed=None, randomize_players=False,
                 **kwarg):
        self.list_of_players = player_field
        self.seed = seed
        if randomize_players is True:
            rd.seed(self.seed)
            rd.shuffle(self.list_of_players)
        self.list_of_players = [player(Board()) for player in self.list_of_players]


    def single_game(self):
        while True:
            for player in self.list_of_players:
                player.move()
                if player.board.goal_reached(player.pos):
                    return player.num_moves, type(player).__name__





    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self, k):
        pass

if __name__ == "__main__":
    tester = Simulation([Player, ResilientPlayer, LazyPlayer])
    numa = tester.single_game()
    print(numa)