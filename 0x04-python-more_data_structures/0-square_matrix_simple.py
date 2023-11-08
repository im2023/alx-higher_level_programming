#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_mtx = [x[:] for x in matrix]

    for index1, x in enumerate(new_mtx):
        for index2, col in enumerate(new_mtx):
            new_mtx[index1][index2] = x[index2] ** 2

    return new_mtx
