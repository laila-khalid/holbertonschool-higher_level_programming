#!/usr/bin/python3
"""
Module 2-matrix_divided
Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Returns a new matrix with results rounded to 2 decimal places.
    """
    err_type = "matrix must be a matrix (list of lists) of integers/floats"
    err_size = "Each row of the matrix must have the same size"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(err_type)
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(err_type)
        for item in row:
            if type(item) not in (int, float):
                raise TypeError(err_type)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError(err_size)
    return [[round(item / div, 2) for item in row] for row in matrix]
