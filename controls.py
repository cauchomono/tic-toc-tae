from victoryCondition import StatusGame

class Controls(StatusGame):


    def __init__(self, board, letter):
        super(Controls, self).__init__(board,letter)


    def enterMove(self):
        asking = True
        while asking:
            move = int(input("What is your move?"))
            if move in range(1, 10):
                return move
            else:
                print("Ingrese un valor valido")

    def movement(self,):
        move = self.enterMove()
        if move == 1:
            self.board[0][0] = self.letter
        elif move == 2:
            self.board[0][1] = self.letter
        elif move == 3:
            self.board[0][2] = self.letter
        elif move == 4:
            self.board[1][0] = self.letter
        elif move == 5:
            self.board[1][1] = self.letter
        elif move == 6:
            self.board[1][2] = self.letter
        elif move == 7:
            self.board[2][0] = self.letter
        elif move == 8:
            self.board[2][1] = self.letter
        elif move == 9:
            self.board[2][2] = self.letter

        return self.board


