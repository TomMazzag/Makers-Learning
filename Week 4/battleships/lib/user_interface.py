from lib.ship import *

class UserInterface:
    def __init__(self, io, game):
        self.io = io
        self.game = game
        self.chosen_ship = ''
        self.placed_ship_count = 0
        self.opponent = ''

    def run(self):
        self._show("Welcome to the game!")
        self._show("Set up your ships first.")
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message()))
        self._prompt_for_ship_placement()
        self._show("OK.")
        self._show("This is your board now:")
        self._show(self._format_board())
        self.placed_ship_count += int(self.chosen_ship)

    def next_turn(self):
        self.ships_remaining()
        self._prompt_for_ship_placement()
        self._show("OK.")
        self.placed_ship_count += int(self.chosen_ship)
        if self.check_for_overlap() == True:
            self._show("Current position is overlapping")
        else:
            self._show("This is your board now:")
            self._show(self._format_board())

    def opponent_board(self, board=''):
        self.opponent = board

    def fire_at_opponent(self):
        fireAt = self._prompt("Where would you like to fire on opponent board [Row Column]")
        row = int(fireAt.split()[0]) - 1
        col = int(fireAt.split()[1]) - 1
        opponent_indexes = self.opponent.split("\n")
        val = opponent_indexes[row][col]
        if val == '.':
            self._show("Miss")
        self._show("Hit")

    def _show(self, message):
        self.io.write(message + "\n")

    def _prompt(self, message):
        self.io.write(message + "\n")
        return self.io.readline().strip()

    def _ships_unplaced_message(self):
        ship_lengths = [str(ship.length) for ship in self.game.unplaced_ships()]
        return ", ".join(ship_lengths)

    def _prompt_for_ship_placement(self):
        ship_length = self._prompt("Which do you wish to place?")
        ship_orientation = self._prompt("Vertical or horizontal? [vh]")
        ship_row = self._prompt("Which row?")
        if int(ship_row) > self.game.rows:
            ship_row = self._prompt("Out of range, which row?")
        ship_col = self._prompt("Which column?")
        if int(ship_col) > self.game.cols:
            ship_col = self._prompt("Out of range, which column?")
        
        place = self.game.place_ship(
            length=int(ship_length),
            orientation={"v": "vertical", "h": "horizontal"}[ship_orientation],
            row=int(ship_row),
            col=int(ship_col),
        )

        self.chosen_ship = ship_length
        while place == 'Outside the board':
            self._show(f'--{place}')
            self._prompt_for_ship_placement()
            break
        

    def _format_board(self):
        rows = []
        for row in range(1, self.game.rows + 1):
            row_cells = []
            for col in range(1, self.game.cols + 1):
                if self.game.ship_at(row, col):
                    #Add space after S for better board - will fail tests though
                    row_cells.append("S")
                else:
                    #Add space after . for better board - will fail tests though
                    row_cells.append(".")
            rows.append("".join(row_cells))
        return "\n".join(rows)
    
    def check_for_overlap(self):
        boardCount = self._format_board().count('S')
        if self.placed_ship_count != boardCount:
            return True

    
    def ships_remaining(self):
        self.game.remove_ship(int(self.chosen_ship))
        self._show("You have these ships remaining: {}".format(
            self._ships_unplaced_message()))
        pass

    def board(self):
        return self._format_board()

