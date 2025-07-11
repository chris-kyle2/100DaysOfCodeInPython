# Find the two maximum numbers in an array containing positive numbers
import numpy as np
def findTwoMaxNumbers(array):
    first_max = float('-inf')
    second_max = float('-inf')
    for num in array:
        if num > first_max:
            second_max= first_max
            first_max = num
        elif num > second_max:
            second_max = num
    return first_max*second_max

my_array = np.array([-4,-2,2,3,4,5,6,7,8,9,10])
print(findTwoMaxNumbers(my_array))