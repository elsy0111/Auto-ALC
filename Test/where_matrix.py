import numpy as np
a = [[[i,i,i] for _ in range(3)] for i in range(1,5)]
idx = a.index([[3,3,3] for _ in range(3)])
print(idx)