from itertools import cycle
import elemental_operations as elem
import numpy as np

# Inputs
matrix = [[1, -1, 2, -1, -1],
          [2, 1, -2, -2, -2],
          [-1, 2, -4, 1, 1],
          [3, 0, 0, -3, -3]]

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

    # Replace a row if the first element is cero with a row without a zero
    if matrix_inv[col_nonzero][0] == 0 and np.sum(np.abs(matrix)) != 0:
        i = 0
        while matrix_inv[col_nonzero][i] == 0:
            i += 1
        elem.el_exchange(matrix, 0, i)
    matrix_invlen = np.shape(np.transpose(matrix))[1]

    # Get zeros under the front element
    if matrix[0][col_nonzero] != 0:
        for x in range(1, matrix_invlen):
            elem.el_elimination(
                matrix, x, 0, -matrix[x][col_nonzero]/matrix[0][col_nonzero])

    # Hide first row

    matrix_diagonalized.append(matrix[0])
    matrix = np.delete(matrix, 0, axis=0).tolist()

matrix_diagonalized.append(matrix[0])

# Find pivots

for i in range(np.shape(matrix_diagonalized)[0]):
    for j in range(np.shape(matrix_diagonalized)[1]):
        if matrix_diagonalized[i][j] != 0:
            pivots.append(j)
            break
        if j == np.shape(matrix_diagonalized)[1]-1:
            pivots.append(None)

# Reduction of the matrix

for row in range(np.shape(matrix_diagonalized)[0]-1, -1, -1):
    if pivots[row] != None and matrix_diagonalized[row][pivots[row]] != 0:
        elem.el_staggering(matrix_diagonalized, row,
                           1/matrix_diagonalized[row][pivots[row]])
    if row != 0:
        if pivots[row] != None and matrix_diagonalized[row][pivots[row]] != 0:
            for up_row in range(row):
                elem.el_elimination(matrix_diagonalized, up_row, row, -
                                    matrix_diagonalized[up_row][pivots[row]]/matrix_diagonalized[row][pivots[row]])

# Algorithm finish

# Cleaning of the matrix
for i in range(np.shape(matrix_diagonalized)[0]):
    for j in range(np.shape(matrix_diagonalized)[1]):
        if matrix_diagonalized[i][j] == 1:
            matrix_diagonalized[i][j] = 1
        if matrix_diagonalized[i][j] == 0:
            matrix_diagonalized[i][j] = 0
        if matrix_diagonalized[i][j] != 0 and matrix_diagonalized[i][j] != 1:
            matrix_diagonalized[i][j] = round(
                matrix_diagonalized[i][j], round_number)

# Return data

print(matrix_diagonalized)
