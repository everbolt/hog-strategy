import numpy as np

#rolls random int 1-6 in 1.9579s, shaves 3.44s
for _ in range(1000000): roll = np.random.randint(1, 7)