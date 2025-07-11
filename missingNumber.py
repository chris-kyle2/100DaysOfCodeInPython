from typing import List
import numpy as np
def missingNumber(n, nums):
        total = (n)*(n+1)//2
        arr_sum=sum(nums)
        missing_num = total - arr_sum
        return missing_num 

print(missingNumber(9, [3,0,1,5,6,2,7,8,9]))  


def twoSum(nums,target):
        found = False
        for i in range(len(nums)):
                for j in range(i+1,len(nums)):
                        if nums[i] == nums[j]:
                                continue
                        elif nums[i] + nums[j] == target:
                                print(i,j)
                                found = True        
        if found == False:
                print("No solution found")
                                

twoSum([2,7,2,15],9)

my_array = np.array([1,2,3,4,5,6,7,8,9,10])

def find_number(array,target):
        found = False
        for i in array:
                if i == target:
                        found = True
                        return found
        if found == False:
                print("Number not found")
                return False

print(find_number(my_array,8))
                        

#Find the maximum product of two integers in an array where all elements are positive.

max_product = np.array([1,2,3,4,5,6,7,8,9,10])


def maximum_product(array):
        max_product_of_two = 0
        for i in range(len(array)):
                for j in range(i+1,len(array)):
                        if array[i]*array[j] > max_product_of_two:
                                max_product_of_two = array[i]*array[j]
        return max_product_of_two

print(maximum_product(max_product))
                        