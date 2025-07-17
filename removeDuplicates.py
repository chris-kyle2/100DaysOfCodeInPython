# Write a function to remove the duplicate numbers on given integer array/list.


def remove_duplicates(list):
    new_list = []
    for i in list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicates([1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10]))