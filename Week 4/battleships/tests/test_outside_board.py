from lib.user_interface import *
from lib.game import *
from tests.terminal_interface_helper_mock import *
import unittest
from unittest.mock import patch

def test_ship_overflowing_board_horizontally():

    game = Game()
    #place_ship(length, orientation, row, col)
    result = game.place_ship(3, 'horizontal', 1, 8)
    assert result == 'Outside the board'

def test_ship_overflowing_board_vertically():

    game = Game()
    #place_ship(length, orientation, row, col)
    result = game.place_ship(5, 'vertical', 7, 1)
    assert result == 'Outside the board'

def test_ship_not_overflowing():

    game = Game()
    #place_ship(length, orientation, row, col)
    result = game.place_ship(5, 'vertical', 1, 8)
    assert result == None

def test_ship_not_overflowing():

    game = Mock_game()
    result = game.prompt_for_ship_placement(1, 11)
    assert result == "Out of range, which row?"


class Mock_game():
    def prompt_for_ship_placement(self, row, col):
        #ship_length = 3
        #ship_orientation = 'vertical'
        ship_row = row
        if int(ship_row) > 10:
            return "Out of range, which row?"
        ship_col = col
        if int(ship_col) > 10:
            return "Out of range, which row?"




