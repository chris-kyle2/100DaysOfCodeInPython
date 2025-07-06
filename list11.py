my_list = ["apple","banana",1,2,3,4,5,6,7,8,9,10]


for i in my_list:
    print(i)
for i in range(len(my_list)):
    print(my_list[i])
for i,j in enumerate(my_list):
    print(f"The index is {i} and the value is {j}")

my_list.append("orange")
print(my_list)

my_list.insert(0,"mango")
print(my_list)