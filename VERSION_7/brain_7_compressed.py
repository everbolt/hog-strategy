from brain_7 import moves

def get_key(dict, val):
    for i in dict:
        if dict[i] == val:
            return i

def get_best_turn(dict):
    return get_key(dict, max(dict.values()))

compressed_moves = [[] for _ in range(50)]
for rows in range(len(moves)):
    for cols in range(len(moves[0])):
        compressed_moves[rows].append(get_best_turn(moves[rows][cols]))
        #print(moves[rows][cols])

print(compressed_moves)