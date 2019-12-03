# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

import random as rd


class Board:
    def __init__(self, *args, **kwargs):
        self.board = args
        self.ladder = kwargs
        self.snakes = kwargs
        if len(args) == 0:
            self.board = [x for x in range(1, 91)]
        else:
            self.board = args
        if len(kwargs) == 0:
            self.ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82,
                           68: 85}
            self.snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12,
                           87: 70}

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

    def get_position(self):
        """
        :return: current position
        """
        return self.pos


class ResilientPlayer(Player):
    """
    A resilient player will take extra steps in the next move
    """
    def __init__(self, board, extra_steps=None):
        """
        :param extra_steps: define number of extra steps
        """
        super().__init__(board)
        self.extra_steps = extra_steps
        if self.extra_steps is None:
            self.extra_steps = 1
        self.hit_snake = False

    def move(self):
        """
        Move of a resilient player
        :return:
        """
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
    """
    A lazy player drops a given number of steps when hitting a ladder and does
    not fall down when hitting snakes
    """
    def __init__(self, board, dropped_steps=None):
        """
        :param dropped_steps: Steps dropped when hitting ladders
        """
        super().__init__(board)
        self.drop_steps = dropped_steps
        self.hit_ladder = False
        if self.drop_steps is None:
            self.drop_steps = 1

    def move(self):
        """
        A lazy players moving behaviour
        :return:
        """
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
    """
    Simulates many games and gives certain analysis
    """
    def __init__(self, player_field, seed=None, randomize_players=False,
                 **kwarg):
        """
        :param player_field: a list of different player types
        :param seed: random seed
        :param randomize_players: randomize player field or not
        """
        self.list_of_players = player_field
        self.seed = seed
        if randomize_players is True:
            rd.seed(self.seed)
            rd.shuffle(self.list_of_players)
        self.sim_results = []
        print(self.list_of_players)

    def single_game(self):
        """
        Simulates a single game of chutes and ladders
        :return: a tuple consisting of the winner type and number of moves
        """
        self.list_of_players = [player(Board()) for player in
                                self.list_of_players]
        print(self.list_of_players)
        while True:
            for player in self.list_of_players:
                player.move()
                if player.board.goal_reached(player.pos):
                    return player.num_moves, type(player).__name__

    def run_simulation(self, n):
        """
        Run n single games
        :param n: amount of games played
        :return:
        """
        for i in range(n):
            self.sim_results.append(
                Simulation(self.list_of_players).single_game()
            )

    def get_results(self):
        """
        :return: a list of all winners and number of moves made
        """
        return self.sim_results

    def winners_per_type(self):
        """
        Counts number of wins in a simulation for each player type
        :return: dictionary
        """
        winner_type = {}
        winner = []
        for i in self.sim_results:
            winner.append(i[1])
        for i in winner:
            winner_type[i] = winner.count(i)
        return winner_type

    def durations_per_type(self):
        """
        Number of moves made in a set of simulations each player type has
        :return: dictionary with a list of moves and winner as key
        """
        win_dict = {}
        play_steps = []
        res_steps = []
        laz_steps = []
        for k in self.sim_results:
            if k[1] == 'ResilientPlayer':
                res_steps.append(k[0])
            elif k[1] == 'LazyPlayer':
                laz_steps.append(k[0])
            else:
                play_steps.append(k[0])
        win_dict['Player'] = play_steps
        win_dict['ResilientPlayer'] = res_steps
        win_dict['LazyPlayer'] = laz_steps
        return win_dict

    def players_per_type(self):
        """
        How many players participating for each type
        :return: A dictionary with number of players participating
        """
        players_type = {'Player': self.list_of_players.count(Player),
                        'ResilientPlayer': self.list_of_players.count(
                            ResilientPlayer),
                        'LazyPlayer': self.list_of_players.count(LazyPlayer)}
        return players_type
