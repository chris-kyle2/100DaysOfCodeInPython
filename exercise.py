data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
def fun(m):
    v = m[0][0]
 
    for row in m:
        for element in row:
            if v <element: v = element
 
    return v
print(fun(data[0]))

a=[1,2,3,4,5,6,7,8,9]
a[::2]=10,20,30,40,50
print(a)


fruit_list1 = ["Apple","Berry","Cherry","Papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = "Guava"
fruit_list3[1] = "Kiwi"

print(fruit_list1)
print(fruit_list2)
print(fruit_list3)

sum = 0
for ls in (fruit_list1,fruit_list2,fruit_list3):
    if ls[0] == "Guava":
        sum += 1
    if ls[1] == "Kiwi":
        sum += 20
print(sum)

def f(value,values):
    v = 1
    values[0] = 44

t = 3
v = [1,2,3]
f(t,v)
print(t,v[0])
