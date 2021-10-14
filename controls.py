class Controls:

    def __init__(self, board):
        self.board = board

    def EnterMove(self,):

        move = int(input("What is your move?"))

        if move in range(1,10):
            if move == 1:
                self.board[0][0] = "O"
            elif move == 2:
                self.board[0][1] = "O"
            elif move == 3:
                self.board[0][2] = "O"
            elif move == 4:
                self.board[1][0] = "O"
            elif move == 5:
                self.board[1][1] = "O"
            elif move == 6:
                self.board[1][2] = "O"
            elif move == 7:
                self.board[2][0] = "O"
            elif move == 8:
                self.board[2][1] = "O"
            elif move == 9:
                self.board[2][2] = "O"

        else:
            print("Ingrese un valor valido")



        return self.board


