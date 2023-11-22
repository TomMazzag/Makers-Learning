import unittest

from lib.user_interface import UserInterface
from lib.game import Game
from tests.terminal_interface_helper_mock import TerminalInterfaceHelperMock


def user_full_turn(io, interface):


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
    io.provide("4")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("h")
    io.expect_print("Which row?")
    io.provide("8")
    io.expect_print("Which column?")
    io.provide("3")
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
        "..SSSS....",
        "..........",
        ".........."
    ]))

    io.expect_print("You have these ships remaining: 3, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("5")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("2")
    io.expect_print("Which column?")
    io.provide("10")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")
    io.expect_print("\n".join([
        "..........",
        ".........S",
        ".S.......S",
        ".S.......S",
        "....SSS..S",
        ".........S",
        "..........",
        "..SSSS....",
        "..........",
        ".........."
    ]))

    io.expect_print("You have these ships remaining: 3")
    io.expect_print("Which do you wish to place?")
    io.provide("3")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("h")
    io.expect_print("Which row?")
    io.provide("10")
    io.expect_print("Which column?")
    io.provide("4")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")
    io.expect_print("\n".join([
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

    interface.run()
    interface.next_turn()
    interface.next_turn()
    interface.next_turn()
    interface.next_turn()

def opponent_full_turn(returnGrid = False):

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
    io.provide("4")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("h")
    io.expect_print("Which row?")
    io.provide("8")
    io.expect_print("Which column?")
    io.provide("3")
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
        "..SSSS....",
        "..........",
        ".........."
    ]))

    io.expect_print("You have these ships remaining: 3, 5")
    io.expect_print("Which do you wish to place?")
    io.provide("5")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("v")
    io.expect_print("Which row?")
    io.provide("2")
    io.expect_print("Which column?")
    io.provide("10")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")
    io.expect_print("\n".join([
        "..........",
        ".........S",
        ".S.......S",
        ".S.......S",
        "....SSS..S",
        ".........S",
        "..........",
        "..SSSS....",
        "..........",
        ".........."
    ]))

    io.expect_print("You have these ships remaining: 3")
    io.expect_print("Which do you wish to place?")
    io.provide("3")
    io.expect_print("Vertical or horizontal? [vh]")
    io.provide("h")
    io.expect_print("Which row?")
    io.provide("10")
    io.expect_print("Which column?")
    io.provide("4")
    io.expect_print("OK.")
    io.expect_print("This is your board now:")
    io.expect_print("\n".join([
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

    interface.run()
    interface.next_turn()
    interface.next_turn()
    interface.next_turn()
    interface.next_turn()

    if returnGrid == True:
        return interface.board()