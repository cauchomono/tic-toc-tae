class Data:

    def MakeListOfFreeFields(board):
        lista_de_tuplas = []
        for n in range(3):
            for i in range(3):
                if board[n][i] != "O" and board[n][i] != "X":
                    tup = (n, i)
                    lista_de_tuplas.append(tup)
        return lista_de_tuplas