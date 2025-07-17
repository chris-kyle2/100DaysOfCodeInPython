# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def contains_duplicate(array):
    found = False
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] == array[j]:
                found = True
    return found

def rotateMatrix(matrix):
    n = len(matrix)

    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):  # Note: start from i to avoid re-swapping
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row
    for row in matrix:
        row.reverse()

    return matrix
