import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock
from tests.user_and_opponent import *

class TestUserInterface(unittest.TestCase):
    def test_full_go(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        user_full_turn(io, interface)

class TestUserInterface(unittest.TestCase):
    def test_full_go_opponent(self):
        opponent_full_turn()