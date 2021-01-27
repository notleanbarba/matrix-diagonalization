import numpy as np


def el_exchange(array, row1, row2):
    temp = array[row1]
    array[row1] = array[row2]
    array[row2] = temp
    return array


def el_staggering(array, row, mult):
    array[row] = np.multiply(array[row], mult).tolist()
    return array


def el_elimination(array, rowj, rowi, mult):
    array[rowj] = np.add(array[rowj], np.multiply(array[rowi], mult)).tolist()
    return array
