

def pair_sum(array,target):
    
    Output = []
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] == array[j]:
                continue
            elif array[i] + array[j] == target:
                
                Output.append((str(array[i])+ "+" + str(array[j])))
                
    return Output


print(pair_sum([1,2,3,4,5,6,7,8,9,10],5))