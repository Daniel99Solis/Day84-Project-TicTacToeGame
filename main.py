# ----------------------------- Tic Tac Toe Game ------------------------------------ #
# This is game is pretty easy to understand, because in Mexico this game is known as
# "Gato". So I already know the rules and all of that
from board import Board
from icon import header
import random

board = Board()  # Object to manage the board

# Variables to use in the logic of the game
available_pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
valid_pos = False
current_player = random.randint(1, 2)
game_on = True
continue_game = True


print(header)
if current_player == 1:
    print(f"Player {current_player} starts with 'X'")
    next_player = 2
else:
    print(f"Player {current_player} starts with 'O'")
    next_player = 1
board.show()


while game_on:
    while not valid_pos:
        select_pos = int(input("Select the position you want: "))
        if select_pos in available_pos:
            valid_pos = True
            available_pos.remove(select_pos)
            board.update(current_player, select_pos)
            print("")
            print("")
            board.show()
            continue_game = board.check(len(available_pos))
        else:
            board.show()
            print("The option is not valid please check the board")

    if continue_game:
        # This part is to switch between turn of player
        auxiliary_player = current_player
        current_player = next_player
        next_player = auxiliary_player
        valid_pos = False
        print(f"Now it is turn of Player {current_player}")
    else:
        game_on = False
        if len(available_pos) == 0:
            print("")
            print("Draw")
        else:
            print("")
            print(f"The winner is Player {current_player}")




