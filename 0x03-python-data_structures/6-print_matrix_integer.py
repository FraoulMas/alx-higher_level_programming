#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        l = 1
        for j in x:
            if l == len(x):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
            l = l + 1
        print()
