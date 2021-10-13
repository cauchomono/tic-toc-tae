class Board:

    def __init__(self):
        board = [[(i + (n * 3)) + 1 for i in range(3)] for n in range(3)]
        self.board = board

    def DisplayBoard(self,):
    #Matriz de elementos del tablero

        center_1 = str(self.board[0][0])
        center_2 = str(self.board[0][1])
        center_3 = str(self.board[0][2])
        center_4 = str(self.board[1][0])
        center_5 = str(self.board[1][1])
        center_6 = str(self.board[1][2])
        center_7 = str(self.board[2][0])
        center_8 = str(self.board[2][1])
        center_9 = str(self.board[2][2])

    # Tablero

        esp = 7  # cantidad de espacios entre paredes
        espm = (esp - 1) // 2  # cantidad de espacioos entre la pared y el centro
        floor = ("+" + "-" * esp) * 3 + "+"  # delimitaciones horizonales  del tablero
        wall = ("|" + " " * esp) * 3 + "|"  # delimitaciones verticales

        mid_1 = ("|" + " " * espm + center_1 + " " * espm) + ("|" + " " * espm + center_2 + " " * espm) + (
                    "|" + " " * espm + center_3 + " " * espm + "|")  # delimitacion vertical incluyendo el centro
        mid_2 = ("|" + " " * espm + center_4 + " " * espm) + ("|" + " " * espm + center_5 + " " * espm) + (
                    "|" + " " * espm + center_6 + " " * espm + "|")
        mid_3 = ("|" + " " * espm + center_7 + " " * espm) + ("|" + " " * espm + center_8 + " " * espm) + (
                    "|" + " " * espm + center_9 + " " * espm + "|")

        fila_1 = f"{floor}\n{wall}\n{mid_1}\n{wall}\n{floor}"
        fila_2 = f"\n{wall}\n{mid_2}\n{wall}\n{floor}"
        fila_3 = f"\n{wall}\n{mid_3}\n{wall}\n{floor}"

        board_image = fila_1 + fila_2 + fila_3  # Estructura del tablero
        return board_image