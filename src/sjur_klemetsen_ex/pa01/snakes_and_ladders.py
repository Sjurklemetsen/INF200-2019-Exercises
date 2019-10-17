# -*- coding: utf-8 -*-

__author__ = "Sjur Spjeld Klemetsen and Ola Flesche Hellenes"
__email__ = "sjkl@nmbu.no and olhellen@nmbu.no"

import random as rd


def single_game(num_players):
    ladder = {1: 40, 8: 10, 36: 52, 43: 62, 49: 79, 65: 82, 68: 85}
    snakes = {24: 5, 33: 3, 42: 30, 56: 37, 64: 27, 74: 12, 87: 70}
    board = [x for x in range(1, 91)]

    pos = [0] * num_players
    num_moves = 0
    winner = False
    while not winner:
        for player in range(num_players):
            roll = rd.randint(1, 6)
            pos[player] += roll

            for (key1, value1), (key2, value2) in zip(ladder.items(),
                                                      snakes.items()):
                if pos[player] == key1:
                    pos[player] = value1
                elif pos[player] == key2:
                    pos[player] = value2
                else:
                    continue
            if pos[player] >= len(board):
                winner = True
        num_moves += 1
    return num_moves


# def multiple_games(num_games, num_players):


# def multi_game_experiment(num_games, num_players, seed):


if __name__ == "__main__":
    game = single_game(4)
    print(game)
