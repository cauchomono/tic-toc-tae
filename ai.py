def DrawMove(board):
    import random

    computer_move = None
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    condition = True
    while condition:
        computer_move = random.choice(board)
        if computer_move in numbers:
            condition = False
            return computer_move