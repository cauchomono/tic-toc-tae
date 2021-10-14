from controls import Controls

from controls import Controls
class Ai(Controls):

    def __init__(self,board,letter):
        super(Ai, self).__init__(board, letter)

        


    def enterMove(self):
        import random
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        condition = True
        while condition:
            computer_move = random.choice(numbers)
            if computer_move not in self.board:
                condition = False
                return int(computer_move)


