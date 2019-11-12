# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import random as rd


class Board:
    """
    This class manage all information about ladders, snakes and
    if the goal has been reached.
    """
    def __init__(self):
        self.ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
        self.snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
        self.board = [x for x in range(1, 91)]
        self.pos = Player().position()

    def goal_reached(self):
        """
        :return: True or False depending if you have reached the goal or not
        """
        if self.pos >= len(self.board):
            return True
        else:
            return False

    def position_adjustment(self):
        """
        :return: value of number of jumps player has skipped if player hits a
        ladder or snake. If player is not on any ladder or snake returns 0.
        """
        for (key1, value1), (key2, value2) in zip(self.ladder.items(),
                                                  self.snakes.items()):
            if self.pos == key1:
                self.pos = value1
                return value1 - key1
            elif self.pos == key2:
                self.pos = value2
                return value2 - key2
            else:
                continue
        return 0


class Player:
    """
    Manages information about a players position, including which board the
    player is on.
    """
    def __init__(self):
        board = Board()
        self.player = Player(board)

    def move(self):
        roll = rd.randint(1, 6)
        self.player += roll

    def position(self):
        return self.player


class ResilientPlayer(Player):
    def __init__(self):
        pass


class LazyPlayer(Player):
    def __init__(self):
        pass


class Simulations:
    def __init__(self):
        pass

    def single_game(self):
        pass

    def run_simulation(self):
        pass

    def get_results(self):
        pass

    def winners_per_type(self):
        pass

    def durations_per_type(self):
        pass

    def players_per_type(self):
        pass
