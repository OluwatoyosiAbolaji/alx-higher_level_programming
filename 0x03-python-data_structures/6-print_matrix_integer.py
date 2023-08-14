#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix[0]:
        print()
    for element in matrix:
        for element2 in element:
            if element.index(element2) == len(element) - 1:
                print("{:d}".format(element2))
            else:
                print("{:d}".format(element2), end=" ")
