from VERSION_0.brain_0 import moves

def baseline_strategy(score, opponent_score):
    return moves[min(score, 49)][min(opponent_score, 49)]