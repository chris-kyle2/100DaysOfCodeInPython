#Write a function called middle that takes a list and returns a new list that contains all but the first and last elements.

from typing import List
my_list = [1,2,3,4,5,6,7,8,9,10]
new_list = []
def middle(list):
    for i in range(1,len(list)-1):
        new_list.append(list[i])
    return new_list

print(middle(my_list))

def middle_using_slicing(list):
    return list[1:-1]

print(middle_using_slicing(my_list))