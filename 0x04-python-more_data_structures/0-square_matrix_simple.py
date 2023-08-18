#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if not matrix:
        return []
    
    square_matrix = []
    
    for row in matrix:
        square_row = [x ** 2 for x in row]
        square_matrix.append(square_row)
    
    return square_matrix
