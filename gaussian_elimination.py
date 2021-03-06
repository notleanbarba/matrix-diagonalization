import elemental_operations as elem
import numpy as np
import scipy.io as scio

# Inputs
matrix = [[8, 4, 2, 64, 16, 4, 343, 49, 7, 1, 15],
          [27, 9, 3, 125, 25, 5, 512, 64, 8, 1, 5],
          [64, 16, 4, 216, 36, 6, 729, 81, 9, 1, 6],
          [125, 25, 5, 343, 49, 7, 1000, 100, 10, 1, 20],
          [216, 36, 6, 512, 64, 8, 1331, 121, 11, 1, 11],
          [343, 49, 7, 729, 81, 9, 1728, 144, 12, 1, 7],
          [512, 64, 8, 1000, 100, 10, 2197, 169, 13, 1, 15],
          [729, 81, 9, 1331, 121, 11, 2744, 196, 14, 1, 17],
          [1000, 100, 10, 1728, 144, 12, 3375, 225, 15, 1, 20],
          [1331, 121, 11, 2197, 169, 13, 4096, 256, 16, 1, 7]]

# matrix = scio.mmread("../../../Downloads/nnc261.mtx.gz").toarray().tolist()

round_number = 2


def Gaussian_elimination(matrix, round_number):
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
    return matrix_diagonalized


print(Gaussian_elimination(Gaussian_elimination(matrix, round_number=6), 2))
