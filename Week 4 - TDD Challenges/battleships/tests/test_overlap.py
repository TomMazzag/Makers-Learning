import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


class TestUserInterface(unittest.TestCase):
    def test_placed_ship_is_removed(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))
        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("Current position is overlapping")

        interface.run()
        interface.next_turn()
        # Within next turn
        # Add a function to user_interface that checks
        # If space to be taken up overlaps current space
        # Take in formatted board and set it to a list
        # Compare if the places where you want to place an S are already equal to S in list

class TestUserInterface(unittest.TestCase):
    def test_placed_ship_is_removed(self):
        io = TerminalInterfaceHelperMock()
        interface = UserInterface(io, Game())
        io.expect_print("Welcome to the game!")
        io.expect_print("Set up your ships first.")
        io.expect_print("You have these ships remaining: 2, 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("2")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("3")
        io.expect_print("Which column?")
        io.provide("2")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "..........",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        io.expect_print("You have these ships remaining: 3, 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("3")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("h")
        io.expect_print("Which row?")
        io.provide("5")
        io.expect_print("Which column?")
        io.provide("5")
        io.expect_print("OK.")
        io.expect_print("This is your board now:")
        io.expect_print("\n".join([
            "..........",
            "..........",
            ".S........",
            ".S........",
            "....SSS...",
            "..........",
            "..........",
            "..........",
            "..........",
            ".........."
        ]))

        io.expect_print("You have these ships remaining: 3, 4, 5")
        io.expect_print("Which do you wish to place?")
        io.provide("5")
        io.expect_print("Vertical or horizontal? [vh]")
        io.provide("v")
        io.expect_print("Which row?")
        io.provide("2")
        io.expect_print("Which column?")
        io.provide("7")
        io.expect_print("OK.")
        io.expect_print("Current position is overlapping")


        interface.run()
        interface.next_turn()
        interface.next_turn()

        #print(interface._format_board())
        #assert 1 == 2

        # ^ Confirm visually, is overlapping