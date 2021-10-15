import random

from board import  Board
from controls import Controls
from ai import Ai

game_board = Board()

how_many_players = input("do you want a 1 or 2 players?\n"
                         "press 1 for 1 player, any number for 2 players: ")


player1_letter = input("Select your piece player 1: ")
player1 = Controls(game_board.board, player1_letter)
if how_many_players == "1":
    if player1_letter == "O":
        player2_letter = "X"
    else:
        player2_letter = "O"

    player2 = Ai(game_board.board, player2_letter)

else:
    player2_letter = input("Select your piece player 2: ")
    player2= Controls(game_board.board, player2_letter)

continue_game= False

while not(player1.VictoryFor() or player2.VictoryFor()):
    game_board.DisplayBoard()
    player1.movement()
    player2.movement()



    game_board.DisplayBoard()








