box_start = [
    [0,  5,  6,  6,  6,  6,  7,  1,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2,  2],
    [0,  5,  6,  6,  6,  6,  7,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [6,  5,  6,  6,  6,  6,  7, 10,  4,  5,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6],
    [0,  5,  6,  5, 10,  5,  5,  6,  4,  5,  7,  7,  7,  7,  7,  7,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  7,  7,  7],
    [5,  4,  5,  6,  5, 10,  5,  6,  3,  5,  0,  7,  3,  7,  3,  3,  0,  3, 10,  2,  10, 10, 0, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  0, 10, 10,  2],
    [5,  4,  5,  5,  5,  5, 10,  6,  4,  5,  6,  3,  0,  3,  4,  5,  6,  3,  3,  3,  6,  5,  5,  5,  5,  5,  5,  5,  6,  6,  6,  6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [5,  4,  5,  5,  0,  5,  0, 10,  3,  5,  6,  0,  3,  6,  3,  5,  6,  3,  3,  3,  3,  6,  3,  5,  5,  5,  5,  5,  5,  5,  5,  6,  6,  6,  6,  6,  6,  6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  6],
    [9,  8,  9,  9,  9,  9,  5,  5,  9,  5,  6,  6,  3,  3,  3,  5,  6, 10,  3,  3, 10,  6, 10, 10, 10,  5,  5,  5,  5,  5,  5,  6,  6,  6,  6,  6,  6,  7, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10,  6],
    [2,  3,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4, 10,  4, 10, 10, 10, 10, 10, 10, 10],
    [2,  3,  4,  5,  0,  5,  5,  5,  3,  4,  5,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  0,  5, 10,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5, 10, 10,  5, 10,  5, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  6,  7,  6,  4,  5,  4,  6,  6,  6,  0,  6,  6,  6,  7,  6,  6,  6,  6,  6,  0, 10, 10, 10, 10, 10, 10, 10,  6,  6,  6,  6,  7,  7,  7,  7,  7,  7,  7, 10, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  3,  3,  6,  4,  5,  6,  4, 10,  4,  3,  6,  7,  6,  0, 10,  7,  6, 10,  7, 10, 10, 10,  6, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  3,  3,  3,  4,  5,  6,  3,  0, 10,  4,  5,  6,  0, 10, 10,  0, 10, 10, 10, 10, 10, 3,  10, 0,  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  3,  3,  3,  4,  5,  6,  4,  4,  4,  4,  0,  6,  6,  7, 10, 10, 10, 6,  10, 10, 10, 10, 10, 3,  10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  4,  3,  3,  4,  3,  4,  3,  4,  4,  5,  9,  7,  6,  7,  9,  1,  9,  0, 10, 10, 10, 10, 10,  4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  5,  5,  5,  4,  5,  6,  6,  5,  5,  4,  4,  6,  6,  7,  9,  7,  9,  5,  9,  9,  9,  2,  3,  0,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    [2,  6,  4,  7,  0,  6,  6,  7,  3,  5,  6,  7,  6,  6,  7,  6,  8,  6,  6,  9,  0,  5,  9,  6,  6,  6,  6,  9,  6,  7,  0,  9,  4,  9,  9,  9,  9,  9,  9,  9, 10, 10, 10, 10, 10, 10, 10, 10, 10,  9],
    [2,  6,  4,  7,  0,  6,  6,  6,  4,  5,  6,  7,  6,  6,  6,  6,  6,  0,  9,  7,  6,  9,  6,  7,  0,  6,  6,  6,  6,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9],
    [2,  6,  4,  7,  0,  6,  6,  6,  4,  5,  7,  6,  7,  4,  7,  7,  6,  6,  0,  9,  7,  7,  7,  0,  7,  7,  7,  7,  7,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9],
    [2,  6,  4,  7,  0,  3,  6,  6,  4,  5,  6,  6,  7,  6,  4,  5,  6,  7,  7,  8,  9,  0,  8,  8,  7,  1,  8,  2,  0,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9],
    [2,  6,  4,  7,  0,  6,  5,  6,  4,  5,  6,  7,  6,  6,  7,  6,  6,  6,  7,  6,  0,  5,  6,  8,  8,  7,  1,  8,  0,  8,  7,  8,  8,  8,  8,  8,  9,  9,  8,  9,  9,  9,  9,  9,  9,  9,  9,  9,  9,  8],
    [2,  6,  4,  7,  0,  5,  7,  6,  4,  5,  6,  5,  6,  5,  7,  6,  6,  7,  7,  7,  5,  8,  7,  7,  7,  7,  7,  1,  7,  7,  7,  7,  7,  7,  0,  7,  7,  7,  7,  7,  7,  8,  8,  8,  8,  8,  8,  8,  8,  8],
    [2,  6,  4,  7,  0,  5,  6,  5,  4,  5,  7,  6,  5,  7,  7,  5,  6,  5,  7,  7,  6,  6,  7,  7,  7,  7,  0,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  8,  8,  8,  8,  8,  7,  8,  8,  8,  7,  7,  7,  8],
    [2,  6,  4,  7,  0,  5,  5,  6,  4,  5,  6,  6,  6,  6,  6,  6,  5,  7,  5,  6,  6,  6,  5,  0,  7,  7,  7,  7,  7,  7,  0,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7],
    [2,  6,  4,  7,  0,  5,  5,  6,  4,  5,  6,  6,  6,  5,  6,  6,  6,  5,  7,  6,  5,  7,  7,  7,  0,  0,  7,  7,  7,  0,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7],
    [2,  6,  4,  7,  0,  6,  5,  6,  4,  5,  6,  6,  6,  6,  6,  6,  6,  6,  7,  6,  6,  5,  0,  5,  5,  7, 10,  0,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7],
    [2,  6,  4,  7,  0,  5,  5,  5,  4,  5,  6,  6,  5,  6,  6,  6,  6,  6,  6,  7,  6,  6,  5,  7,  7,  7,  0, 10,  7,  7,  7,  7,  7,  7,  0,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7],
    [2,  6,  4,  7,  0,  5,  5,  6,  4,  5,  6,  6,  7,  6,  6,  6,  6,  6,  7,  5,  0,  6,  6,  6,  6,  6,  5,  6, 10,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7,  7],
    [2,  6,  4,  7,  0,  6,  5,  6,  4,  5,  6,  6,  6,  6,  4,  5,  5,  6,  6,  6,  5,  6,  6,  6,  0,  6,  6,  6,  6, 10,  6,  7,  0,  7,  7,  7,  7,  7,  7,  6,  7,  7,  7,  7,  7,  7,  7,  7,  7,  6],
    [2,  6,  4,  7,  0,  6,  6,  6,  4,  5,  6,  6,  6,  6,  6,  6,  7,  6,  6,  6,  6,  6,  0,  0,  5,  6,  6,  6,  5,  6,  9,  7,  6,  7,  7,  7,  0,  7,  7,  7,  6,  7,  6,  7,  6,  6,  6,  6,  6,  6],
    [2,  6,  4,  7,  0,  6,  5,  5,  4,  5,  6,  6,  6,  6,  6,  5,  6,  6,  6,  6,  5,  6,  5,  5,  5,  6,  5,  6,  5,  7,  6,  0,  7,  7,  6,  0,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6],
    [2,  6,  4,  7,  0,  6,  6,  5,  4,  5,  6,  5,  5,  5,  5,  6,  6,  6,  5,  5,  6,  5,  5,  5,  7,  5,  5,  5,  5,  5,  5,  5,  9,  0,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6,  6],
    [2,  6,  4,  7,  0,  6,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  8,  5,  5,  5,  5,  5,  5,  0,  6,  5,  6,  6,  5,  5,  5,  5,  5],
    [2,  6,  4,  7,  0,  3,  5,  5,  4,  5,  6,  5,  5,  5,  4,  5,  6,  5,  7,  5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  5,  5,  5,  8,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5],
    [2,  6,  4,  7,  0,  3,  4,  5,  4,  5,  6,  5,  4,  4,  4,  4,  6,  4,  5,  4,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  4,  5,  5,  5,  5,  8,  5,  5,  0,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5,  5],
    [2,  6,  4,  7,  0,  3,  4,  4,  4,  5,  0,  4,  4,  4,  4,  4,  0,  4,  4,  4,  4,  4,  0,  4,  4,  5,  4,  4,  0,  4,  5,  5,  5,  5,  0,  5,  7,  5,  5,  5,  5,  5,  0,  5,  5,  5,  5,  5,  5,  4],
    [2,  6,  4,  4,  0,  3,  4,  4,  4,  5,  0,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  0,  5,  4,  4,  0,  5,  5,  5,  5,  5,  4,  4,  4],
    [2,  6,  4,  7,  0,  3,  4,  3,  4,  5,  0,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  7,  0,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4],
    [2,  6,  4,  3,  0,  3,  3,  3,  4,  5,  0,  4,  3,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  4,  6,  4,  4,  4,  4,  4,  4,  0,  4,  4,  4],
    [2,  6,  4,  7,  0,  3,  3,  3,  4,  3,  0,  3,  3,  3,  4,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  4,  3,  4,  4,  4,  3,  4,  6,  4,  4,  4,  4,  4,  4,  4,  4,  4],
    [2,  6,  4,  7,  0,  3,  3,  3,  4,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  5,  3,  3,  0,  3,  3,  3,  3,  3],
    [2,  6,  4,  7,  2,  3,  3,  3,  4,  3,  0,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  3,  5,  3,  3,  3,  3,  3,  0,  3],
    [2,  6,  4,  3,  0,  3,  3,  3,  4,  3,  0,  3,  3,  3,  3,  3,  0,  3,  3,  3,  3,  3,  0,  3,  3,  3,  3,  3,  0,  3,  3,  3,  3,  3,  0,  3,  3,  3,  3,  3,  0,  3,  3,  0,  3,  3,  0,  0,  3,  3],
    [0,  6,  4,  7,  0,  3,  0,  3,  4,  3,  0,  3,  0,  3,  2,  2,  0,  3,  0,  3,  3,  3,  0,  3,  0,  3,  3,  3,  0,  3,  0,  3,  3,  3,  0,  3,  0,  3,  3,  3,  0,  3,  0,  3,  4,  0,  0,  3,  0,  2],
    [0,  6,  4,  2,  0,  3,  0,  2,  2,  2,  0,  2,  0,  2,  2,  2,  0,  2,  0,  2,  2,  2,  0,  2,  0,  2,  2,  2,  0,  2,  0,  2,  2,  2,  0,  2,  0,  2,  2,  2,  0,  2,  0,  2,  2,  3,  0,  3,  0,  2],
    [0,  3,  4,  7,  0,  0,  0,  2,  4,  2,  0,  0,  0,  2,  2,  2,  0,  0,  0,  2,  2,  2,  0,  0,  0,  2,  2,  2,  0,  0,  0,  2,  2,  2,  0,  0,  0,  2,  2,  2,  0,  0,  0,  2,  2,  2,  0,  0,  0,  2],
    [0,  3,  0,  7,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2],
    [0,  3,  0,  7,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  1,  0,  0,  0,  2,  0,  1,  0,  0,  0,  2,  0,  2,  0,  0,  0,  2,  0,  2,  0,  0,  0,  1,  0,  1,  0,  0,  0,  1,  0,  2,  0,  0,  0,  1],
    [0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0,  0,  0],
    [0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0]
]
# 32 - 153
# 32 - 99 represent normal
# 100-110 represents 10 and X, left is 10, right goes from 0 to 10
# 111-119 represents X and 10, right is 10, left goes from 1 to 10
# 152 represents 0 and 10

# NEW
# 128 - 152 is broken
# 191 - 220 will replace

#Convert 2D to 1D
box_raw = []
for row in box_start:
    for col in row:
        box_raw.append(col)

def shift_ref(x):
    return x + 64

#Compress
compress_ref = {
    (0, 0): 120,
    (0, 1): 121,
    (0, 2): 122,
    (0, 3): 123,
    (0, 4): 124,
    (0, 5): 125,
    (0, 6): 126,
    (0, 7): shift_ref(127),
    (0, 8): shift_ref(128),
    (0, 9): shift_ref(129),
    (0, 10): shift_ref(152),
    (1, 0): shift_ref(130),
    (1, 1): shift_ref(131),
    (1, 2): shift_ref(132),
    (1, 3): shift_ref(133),
    (1, 4): shift_ref(134),
    (1, 5): shift_ref(135),
    (1, 6): shift_ref(136),
    (1, 7): shift_ref(137),
    (1, 8): shift_ref(138),
    (1, 9): shift_ref(139),
    (1, 10): 111,
    (2, 0): shift_ref(140),
    (2, 1): shift_ref(141),
    (2, 2): shift_ref(142),
    (2, 3): shift_ref(143),
    (2, 4): shift_ref(144),
    (2, 5): shift_ref(145),
    (2, 6): shift_ref(146),
    (2, 7): shift_ref(147),
    (2, 8): shift_ref(148),
    (2, 9): shift_ref(149),
    (2, 10): 112,
    (3, 0): shift_ref(150),
    (3, 1): shift_ref(151),
    (3, 2): 32,
    (3, 3): 33,
    (3, 4): 34,
    (3, 5): 35,
    (3, 6): 36,
    (3, 7): 37,
    (3, 8): 38,
    (3, 9): 39,
    (3, 10): 113,
    (4, 0): 40,
    (4, 1): 41,
    (4, 2): 42,
    (4, 3): 43,
    (4, 4): 44,
    (4, 5): 45,
    (4, 6): 46,
    (4, 7): 47,
    (4, 8): 48,
    (4, 9): 49,
    (4, 10): 114,
    (5, 0): 50,
    (5, 1): 51,
    (5, 2): 52,
    (5, 3): 53,
    (5, 4): 54,
    (5, 5): 55,
    (5, 6): 56,
    (5, 7): 57,
    (5, 8): 58,
    (5, 9): 59,
    (5, 10): 115,
    (6, 0): 60,
    (6, 1): 61,
    (6, 2): 62,
    (6, 3): 63,
    (6, 4): 64,
    (6, 5): 65,
    (6, 6): 66,
    (6, 7): 67,
    (6, 8): 68,
    (6, 9): 69,
    (6, 10): 116,
    (7, 0): 70,
    (7, 1): 71,
    (7, 2): 72,
    (7, 3): 73,
    (7, 4): 74,
    (7, 5): 75,
    (7, 6): 76,
    (7, 7): 77,
    (7, 8): 78,
    (7, 9): 79,
    (7, 10): 117,
    (8, 0): 80,
    (8, 1): 81,
    (8, 2): 82,
    (8, 3): 83,
    (8, 4): 84,
    (8, 5): 85,
    (8, 6): 86,
    (8, 7): 87,
    (8, 8): 88,
    (8, 9): 89,
    (8, 10): 118,
    (9, 0): 90,
    (9, 1): 91,
    (9, 2): 92,
    (9, 3): 93,
    (9, 4): 94,
    (9, 5): 95,
    (9, 6): 96,
    (9, 7): 97,
    (9, 8): 98,
    (9, 9): 99,
    (9, 10): 119,
    (10, 0): 100,
    (10, 1): 101,
    (10, 2): 102,
    (10, 3): 103,
    (10, 4): 104,
    (10, 5): 105,
    (10, 6): 106,
    (10, 7): 107,
    (10, 8): 108,
    (10, 9): 109,
    (10, 10): 110,
}
box_c = ""
for i in range(0, len(box_raw), 2):
    current_char = chr(compress_ref[(box_raw[i], box_raw[i + 1])])
    box_c += current_char

print(box_c)

#Decompress
r=[]
for c in box_c:
 b=ord(c)
 f=None
 s=None
 if b>190:
     b-=64
 if 31<b<100:
  f=b//10
  s=b%10
 if 99<b<111:
  f=10
  s=b%100
 if 110<b<120:
  f=b%10
  s=10
 if 119<b<152:
  f=b//10-12
  s=b%10
 if b==152:
  f=0
  s=10

 if f == None or s == None:
  print("ERROR")
  print(c)
  print(ord(c))

 r.append(f)
 r.append(s)

print("????", r==box_raw)

equal = True
for i in range(0, 300):
    for j in range(0, 300):
        compressed_move = r[min(i,49)*50+min(j,49)]
        uncompressed_move = box_start[min(i,49)][min(j,49)]
        if compressed_move != uncompressed_move:
            equal = False

print(equal)