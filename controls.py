class controls:

    def EnterMove(board):

        board_elements = []
        for n in range(3):
            for i in range(3):
                board_elements.append(board[n][i])

        move = int(input("Cual va a ser su jugada?"))
        print(board_elements)

        if move in board_elements:
            if move == 1:
                board[0][0] = "O"
            elif move == 2:
                board[0][1] = "O"
            elif move == 3:
                board[0][2] = "O"
            elif move == 4:
                board[1][0] = "O"
            elif move == 5:
                board[1][1] = "O"
            elif move == 6:
                board[1][2] = "O"
            elif move == 7:
                board[2][0] = "O"
            elif move == 8:
                board[2][1] = "O"
            elif move == 9:
                board[2][2] = "O"

        else:
            print("Ingrese un valor valido")

        return board

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
