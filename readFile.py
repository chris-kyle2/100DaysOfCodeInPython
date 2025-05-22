path = "/Users/adarshpandey/Desktop/100DaysCode/textfile.txt"
f = open(path,"r")

value =f.read(60)
print(type(value))
print(value)
print(len(value))
individualValues = value.split()
print(individualValues)
sum =0
for x in individualValues:
    sum += int(x)
print(sum)


f.close()



