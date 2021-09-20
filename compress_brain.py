from VERSION_10.brain_10 import moves

file_name = "brain_10_compressed"

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

storage_file = open(file_name + ".txt", "w")
storage_file.write("\n".join(str(i) for i in compressed_moves))
storage_file.close()