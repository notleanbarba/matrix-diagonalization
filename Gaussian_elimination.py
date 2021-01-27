import elemental_operations as elem
import numpy as np

matrix = [[5, 3, 4, 4], [7, 1, 9, 6], [5, 4, 3, 1]]
col_nonzero = 0

for col in range(len(matrix[1])):
    if np.sum(np.abs(np.transpose(matrix))[col]) != 0:
        col_nonzero = col
        break
    col += 1

if matrix[col][0] == 0:
    elem.el_exchange(matrix, 0)
