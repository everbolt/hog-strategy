from numcompress import compress, decompress
from Compression.box import box_raw

doubler = lambda x, y: x + y + 1 + y * 11

box_processed = []

while len(box_raw) != 0:
    box_processed.append(doubler(box_raw.pop(0), box_raw.pop(0)))

compressed_box = compress(box_processed)

print(compressed_box)

uncompressed_box = decompress(box_processed)

#print(uncompressed_box)