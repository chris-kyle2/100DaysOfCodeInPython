myList = []

inValue = int(input("Enter a number: "))
sum=0
while(inValue!=-1):
    myList.append(inValue)
    sum+=inValue
    inValue= int(input())
for x in myList:
    print(x)
print(sum/len(myList))


