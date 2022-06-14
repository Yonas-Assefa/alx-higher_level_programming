#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for elm in matrix:
        for i in elm:
            print("{:d}".format(i), end = " ")
        print()
