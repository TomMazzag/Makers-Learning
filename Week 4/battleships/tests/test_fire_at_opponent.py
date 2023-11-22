import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from tests.user_and_opponent import *

class TestUserInterface(unittest.TestCase):
    def test_opponent_board_returned(self):
        result = opponent_full_turn(True)
        assert result == ("\n".join([
        "..........",
        ".........S",
        ".S.......S",
        ".S.......S",
        "....SSS..S",
        ".........S",
        "..........",
        "..SSSS....",
        "..........",
        "...SSS...."
        ]))
        return result
    
class TestUserInterface(unittest.TestCase):
    def test_full_go(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        user_full_turn(io, interface)
        interface.opponent_board(opponent_full_turn(True))
        io.expect_print("Where would you like to fire on opponent board [Row Column]")
        io.provide("4 2")
        io.expect_print("Hit")
        interface.fire_at_opponent()