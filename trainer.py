import numpy as np
from gekko import GEKKO

#moves[(player_score * 50) + opponent_score]
#Determine access move based on player and opponent score

PLAYER_MAX_SCORE = 50 #Score player needs to win
OPPONENT_MAX_SCORE = 50 #Score opponent needs to win

def objective(): #Function to be minimized
    return 1

m = GEKKO()

m.options.SOLVER = 3

moves = m.Array(m.Var, (PLAYER_MAX_SCORE, OPPONENT_MAX_SCORE), value=1, lb=0, ub=10, integer=True)

m.Obj(objective(moves))

m.solve(disp=True)
