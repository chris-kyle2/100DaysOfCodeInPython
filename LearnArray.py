from array import *


# arr1 = array('i',[])
# n = int(input("Enter the length of the array: "))
# for i in range(n):
#     x = int(input(f"Enter thet value of element {i}:"))
#     arr1.append(x)

# for i in range(len(arr1)):
#     print(arr1[i], end = "\n")
# arr1.append(10)
values = [6,7,8,9]
print(type(values))
arr1 = array('i',[1,2,3,4,5])

arr1.append(10)

arr1.insert(0,11)
arr1.extend([12,13,14]) #extend is used to add multiple elements to the array
arr1.fromlist(values)
arr1.remove(12)
print(len(arr1))
arr1.pop()
arr1.reverse()
print(arr1.buffer_info())
print(arr1)
arr1.append(10)
print(arr1.count(10))
print(arr1.tolist())
print(arr1.tobytes())















