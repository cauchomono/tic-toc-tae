from controls import Controls

# This AI is a random choice by the machine

class Ai(Controls):

    def __init__(self,board,letter):
        super(Ai, self).__init__(board, letter)



    def enterMove(self):

        import random
        board_elements = []
        for row in self.board:
            for element in row:
                board_elements.append(element)

        numbers = range(1,10)
        condition = True
        while condition:
            computer_move = random.choice(numbers)
            print(self.board)
            if computer_move in board_elements:
                condition = False
                return computer_move


