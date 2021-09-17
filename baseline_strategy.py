from VERSION_5.brain_5 import moves

def baseline_strategy(score, opponent_score):
    return get_best_turn(moves[min(score, 49)][min(opponent_score, 49)])

def get_key(dict, val):
    for i in dict:
        if dict[i] == val:
            return i

def get_best_turn(dict):
    return get_key(dict, max(dict.values()))