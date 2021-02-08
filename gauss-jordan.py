import elemental_operations as elem
import numpy as np
import scipy.io as scio

# Inputs
matrix = [[1, 1, 2, 8],
          [-1, -2, 3, 1],
          [3, -7, 4, 10]]

matrix = scio.mmread("../../../Downloads/nnc261.mtx.gz").toarray().tolist()

round_number = 2

# Algorithm start
col_nonzero = 0
matrix_diagonalized = []
pivots = []

for row in range(np.shape(matrix)[0]-1):
    # Find first column from left non zero
    matrix_inv = np.transpose(matrix)

    for col in range(len(matrix[0])):
        if np.sum(np.abs(matrix_inv)[col]) != 0:
            col_nonzero = col
            break

    # Replace a row if the first element is zero with a row without a zero
    if matrix_inv[col_nonzero][row] == 0 and np.sum(np.abs(matrix)) != 0:
        i = 0
        while matrix_inv[col_nonzero][i] == 0:
            i += 1
        elem.el_exchange(matrix, 0, i)
    matrix_invlen = np.shape(np.transpose(matrix))[1]

    # Make first element 1
    elem.el_staggering(matrix, 0, matrix[0][col_nonzero])

    # Make
