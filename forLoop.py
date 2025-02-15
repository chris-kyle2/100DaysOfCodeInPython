###### Understanding for loop
for i in range(6):
    print(i,sum(range(i+1)))

# sum of numbers 1 to 9
sum=0
for i in range(1,10,1):
    sum+=i
print(sum)


### Sum of odd numbers  1 tto 9
oddSum=0
for i in range(1,10,2):
    oddSum+=i

print(oddSum)


### Sum of even numbers 1 to 9
evenSum=0
for i in range(1,10,2):
    evenSum +=i

print(evenSum)



