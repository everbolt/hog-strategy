import numpy as np
from gekko import GEKKO
from dependencies import take_turn
from test_model import test_model as objective

PLAYER_MAX_SCORE = 50 #Score player needs to win
OPPONENT_MAX_SCORE = 50 #Score opponent needs to win

#The opponent's current strategy (always roll 4 dice)
OPPONENT_MOVE = 4

m = GEKKO()
m.options.SOLVER = 3

"""
moves is a 2-d array where:
    the row represents player's current score
    the column represents opponent's current score
    the element represents the optimal move for the above game state
"""
player_moves = m.Array(m.Var, (PLAYER_MAX_SCORE, OPPONENT_MAX_SCORE), value=3, lb=0, ub=10, integer=True)

m.Obj(objective(player_moves, OPPONENT_MOVE, PLAYER_MAX_SCORE, OPPONENT_MAX_SCORE, 100))

m.solve(disp=False)

print(moves)