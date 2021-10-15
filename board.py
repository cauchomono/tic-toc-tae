class Board:

    def __init__(self):
        board = [[(i + (n * 3)) + 1 for i in range(3)] for n in range(3)]
        self.board = board

    def DisplayBoard(self,):
    #Matrix board elements

        center_1 = str(self.board[0][0])
        center_2 = str(self.board[0][1])
        center_3 = str(self.board[0][2])
        center_4 = str(self.board[1][0])
        center_5 = str(self.board[1][1])
        center_6 = str(self.board[1][2])
        center_7 = str(self.board[2][0])
        center_8 = str(self.board[2][1])
        center_9 = str(self.board[2][2])

    # Draws the board

        esp = 7  # number of spaces between walls
        espm = (esp - 1) // 2  # number of spaces between center and walls
        floor = ("+" + "-" * esp) * 3 + "+"  # horizontal delimitations
        wall = ("|" + " " * esp) * 3 + "|"  # vertical delimitations

        mid_1 = ("|" + " " * espm + center_1 + " " * espm) + ("|" + " " * espm + center_2 + " " * espm) + (
                    "|" + " " * espm + center_3 + " " * espm + "|")  # vertical delimitation including center
        mid_2 = ("|" + " " * espm + center_4 + " " * espm) + ("|" + " " * espm + center_5 + " " * espm) + (
                    "|" + " " * espm + center_6 + " " * espm + "|")
        mid_3 = ("|" + " " * espm + center_7 + " " * espm) + ("|" + " " * espm + center_8 + " " * espm) + (
                    "|" + " " * espm + center_9 + " " * espm + "|")

        fila_1 = f"{floor}\n{wall}\n{mid_1}\n{wall}\n{floor}"
        fila_2 = f"\n{wall}\n{mid_2}\n{wall}\n{floor}"
        fila_3 = f"\n{wall}\n{mid_3}\n{wall}\n{floor}"

        board_image = fila_1 + fila_2 + fila_3  # board structure
        print(board_image)