import numpy as np

arr1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]])
for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        print(arr1[i][j],end="\n")


def access_particular_element(array,row_index,column_index):
    if row_index >= len(array) or column_index >=len(array[0]):
        print(f"row_index or column_index is out of range")
    else:
        print(f"The element at row index {row_index} and column index {column_index} is")
        print(array[row_index][column_index]) 

access_particular_element(arr1,1,2)

def find_particular_element(array,element):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j] == element:
                print(f"The element {element} is found at row index {i} and column index {j}")
                return True
    print(f"The element {element} is not found in the array")
    return False

find_particular_element(arr1,200)

def delete_particular_row_and_column(array,row_index,column_index):
    if row_index >= len(array) or column_index >=len(array[0]):
        print(f"row_index or column_index is out of range")
        return array
    else:
        array = np.delete(array,row_index,axis=0)
        array = np.delete(array,column_index,axis=1)
        return array
print(delete_particular_row_and_column(arr1,1,2))


def delete_particular_element(array,row_index,column_index):
    if row_index >= len(array) or column_index >= len(array[0]):
        print(f"row_index or column_index is out of range")
        return array
    else:
        # Create a copy of the original array
        new_array = array.copy()
        # Replace the element with a sentinel value (e.g., -999 or None)
        new_array[row_index][column_index] = 0
        print(f"Element at position ({row_index}, {column_index}) has been replaced with -999")
        return new_array
print(delete_particular_element(arr1,1,2))

def delete_particular_row(array,row_index):
    if row_index >= len(array):
        print(f"The row index {row_index} is out of range")
        return array
    else:
        new_array = np.delete(array,row_index,axis=0)
        return new_array
print(delete_particular_row(arr1,1))


def delete_particular_column(array,column_index):
    if column_index >= len(array[0]):
        print(f"The column index {column_index} is out of range")
        return array
    else: 
        new_array = np.delete(array,column_index,axis=1)
        return new_array
print(delete_particular_column(arr1,2))





