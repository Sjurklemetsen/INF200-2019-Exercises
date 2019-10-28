# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen'
__email__ = 'sjkl@nmbu.no'

from src.sjur_klemetsen_ex.ex05.walker_sim import Walker, Simulation

class BoundedWalker(Walker):
    def __init__(self, start, home, left_limit, right_limit):

    """
    Initialise the walker

    Arguments
    ---------
    start : int
        The walker's initial position
    home : int
        The walk ends when the walker reaches home
    left_limit : int
        The left boundary of walker movement
    right_limit : int
        The right boundary  of walker movement
    """

class BoundedSimulation:
    def __init__(self, start, home, seed, left_limit, right_limit):
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
