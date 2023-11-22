import sys
from lib.game import Game
from lib.user_interface import UserInterface


class TerminalIO:
    def readline(self):
        return sys.stdin.readline()

    def write(self, message):
        sys.stdout.write(message)

opponent = ("\n".join([
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


io = TerminalIO()
game = Game()
user_interface = UserInterface(io, game)
user_interface.run()
user_interface.next_turn()
user_interface.next_turn()
user_interface.next_turn()
user_interface.next_turn()
user_interface.opponent_board(opponent)
user_interface.fire_at_opponent()
