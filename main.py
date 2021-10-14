from board import  Board
from controls import Controls
from ai import Ai

tablero = Board()


jugador1 = Controls(tablero.board,"x")
jugador2= Ai(tablero.board,"o")



tablero.DisplayBoard()
jugador1.movement()
jugador2.movement()

tablero.DisplayBoard()


#TODO 1: Hacer tablero
#TODO 2: hacer movimiento jugador
#TODO 3: hacer movimiento ia
#TODO 4: actualizar tablero
#TODO 1:





