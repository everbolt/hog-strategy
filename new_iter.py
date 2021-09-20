box = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

dim = 4

for it_len in range(dim - 1, -1, -1):
    for zed in range(it_len, -1, -1):
        if box[it_len][zed]: print("ERROR")
        else: box[it_len][zed] = 1
        print(box)
        if it_len != zed:
            if box[zed][it_len]: print("ERROR")
            else: box[zed][it_len] = 1
            print(box)