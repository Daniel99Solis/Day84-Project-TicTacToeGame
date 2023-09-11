# This class will be to create the board for the Cat game and also to perform
# the logic of the game
class Board:
    def __init__(self):
        self.array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    def show(self):
        for index, row in enumerate(self.array):
            auxiliary_row = ""
            for index2, element in enumerate(row):
                if index2 != len(row) - 1:
                    auxiliary_row = auxiliary_row + (" " + str(element) + " |")
                else:
                    auxiliary_row = auxiliary_row + (" " + str(element))
            if index != len(self.array) - 1:
                print(auxiliary_row)
                print("------------")
            else:
                print(auxiliary_row)

    def update(self, player, pos):
        if player == 1:
            value = "X"
        else:
            value = "O"
        if 1 <= pos <= 3:
            self.array[0][pos - 1] = value
        elif 4 <= pos <= 6:
            self.array[1][pos - 4] = value
        else:
            self.array[2][pos - 7] = value

    def check(self, free_positions):
        continue_game = True
        # Check for draw
        if free_positions == 0:
            continue_game = False
        # Check winner by diagonals
        elif self.array[0][0] == self.array[1][1] == self.array[2][2]:
            continue_game = False
        elif self.array[0][2] == self.array[1][1] == self.array[2][0]:
            continue_game = False
        else:
            # Check winner by row
            for row in self.array:
                if row[0] == row[1] == row[2]:
                    continue_game = False
            # Check winner by column
            if continue_game:
                for i in range(0, 3):
                    if self.array[0][i] == self.array[1][i] == self.array[2][i]:
                        continue_game = False
                        return continue_game
                    else:
                        continue_game = True
        return continue_game
