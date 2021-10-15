class StatusGame:

    def __init__(self,board, letter):
        self.board = board
        self.letter = letter

    def rowWinner(self):
        condition = []  # Contains items to verify
        # Check that the rows contain the same value to win
        n =0
        while (n != 3):
            condition.clear()  # clear the list of conditions for a new iteration
            for i in range(3):
                condition.append(self.board[n][i])
            if condition[0] == condition[1] == condition[2]:  # If the elements of the row are equals,
                # so returns Victory True and breaks the cycle
                victory = True
                return condition[0]
            else:  # If not are equal, pass to other row and repeat the process
                n += 1
        return False


    # Check that the columns contain the same value to win
    def columnWinner(self):
        condition = []
        i = 0
        while (i != 3):
            condition.clear()
            for n in range(3):
                condition.append(self.board[n][i])
            if condition[0] == condition[1] == condition[2]:
                return condition[0]
            else:
                i += 1
        return False


    def diagonalWinner(self):
        if self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][0]
        return False

    def is_draw_game(self):
        is_draw= True
        for row in self.board:
            for element in row:
                if element in range(1,10):
                    is_draw = False
                    return is_draw
        return is_draw



    def VictoryFor(self) :
        stop_game = False
        if self.rowWinner() or self.columnWinner() or self.diagonalWinner():
            print(f"The winner is the letter {self.letter}")
            stop_game = True
            return stop_game
        elif self.is_draw_game():
            stop_game = True
            print("Draw Game")
            return stop_game
        else:
            return stop_game