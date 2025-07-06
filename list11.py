my_list = ["apple","banana",1,2,3,4,5,6,7,8,9,10]
def traverse_list(list):
    for i,j in enumerate(list):
        print(f"The index is {i} and the value is {j}")
traverse_list(my_list)

def search_element(list,element):
    for i,j in enumerate(list):
        if list[i] == element:
            print(f"The given element {element} is found at index {i}")
            return True
    
    print(f"The given element {element} is not found in the list")
    return False
search_element(my_list,4)

list2 = [1,2,3,4,5,6,7,8,9,10]
def average(list):
    sum = 0
    for i in list:
        sum += i
    average = sum/len(list)
    print(f"The average of the list is {average}")
average(list2)

def average_using_sum(list):
    
    average = sum(list)/len(list)
    return average
print(f"The average of the list is {average_using_sum(list2)}")
list3 = [0,1,1,2,3,4,5,6,7,8,9,10,10,11,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
def find_max(list):
    max = list[0]
    for i in list:
        if i >= max:
            max = i
    return max
print(f"The maximum element in the list is {find_max(list3)}")

def find_min(list):
    min = list[0]
    for i in list:
        if i <= min:
            min = i
    return min
print(f"The minimum element in the list is {find_min(list3)}")

def find_no_of_occurences(list,element):
    count = 0
    for i in list:
        if i == element:
            count +=1
    return count
print(f"The number of occurences of the element 10 in the list is {find_no_of_occurences(list3,1)}")

myList = list()
while(True):
    inp = input("Enter the number : ")
    if inp.lower() == "done": break
    number = int(inp)
    myList.append(number)
    
print(myList)
average = sum(myList)/len(myList)
print(f"The average of the list is {average}")
