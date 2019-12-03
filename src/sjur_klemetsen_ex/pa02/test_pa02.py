# -*- coding: utf-8 -*-

__author__ = 'Sjur Spjeld Klemetsen, Ola Flesche Hellenes'
__email__ = 'sjkl@nmbu.no, olhellen@nmbu.no'

from src.sjur_klemetsen_ex.pa02 import snakes_simulations as cs


def test_position_adj():
    """
    testin position adjustments give the right results
    :return:
    """
    a = cs.Board().position_adjustment(8)
    assert a == 2


def test_if_move_method_moves_you():
    """
    Test if the player moves a step
     when the move method is called.
    :return:
    """
    a = cs.Board
    b = cs.Player(a)
    b.move()
    d = b.get_position()
    b.move()
    e = b.get_position()
    assert d != e
