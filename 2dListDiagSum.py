import numpy as np

my_twod_array = np.array([[1,2,3],[4,5,6],[7,8,9]])

def diagonal_sum(array):
    sum =0
    for i in range(len(array)):
        for j in range(len(array[i])):
            if i == j:
                sum += array[i][j]
    return sum