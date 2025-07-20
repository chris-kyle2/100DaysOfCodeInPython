# Write a function that calculates the sum and product of all elements in a tuple of numbers.


tuple_1 = (1,2,3,4,5)

def sum_and_product(tuple):
    sum = 0
    product = 1
    for i in tuple:
        sum+=i
        product *=i

    return sum,product

print(sum_and_product(tuple_1))


# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

def element_wise_sum(tuple1,tuple2) -> tuple:
    if len(tuple1) != len(tuple2):
        raise ValueError("Tuples must be of the same length")
    
    return tuple(a+b for a,b in zip(tuple1,tuple2))

print(element_wise_sum((1,2,3),(4,5,6)))


# Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

tuple_2 = (1,2,3,4,5)
value = 0


def insert_at_beginning(tuple,value) -> tuple:
    return (value,)+ tuple

print(insert_at_beginning(tuple_2,value))


# Write a function that takes a tuple of strings and concatenates them, separating each string with a space.

tuple_3 = ("Hello","World","This","Is","A","Test")

def concatenate_str(tuple) -> str:
    result = ""
    for i in tuple:
        result += i + " "
    return result.strip()
print(concatenate_str(tuple_3))

# Strip function is used to remove the leading and trailing whitespace from a string.

def concatenate_str_2(tuple) -> str:
    return " ".join(tuple)

print(concatenate_str_2(tuple_3))
# Join function is used to join the elements of a tuple into a string.


# Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.

tuple_4 = ((1,2,3),(4,5,6),(7,8,9))

def diagonal_elements(tuple_input) -> tuple:
   result = []
   for i in range(len(tuple_input)):
       for j in range(len(tuple_input[i])):
           if i == j:
               result.append(tuple_input[i][j])
   return tuple(result)
 

print(diagonal_elements(tuple_4))


# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple_5 = (1,2,3,4,5)
tuple_6 = (3,4,5,6,7)
def common_elements(tuple_5,tuple_6) -> tuple:
    result = []
    for i in tuple_5:
        for j in tuple_6:
            if i == j:
                result.append(i)
    return tuple(result)

print(common_elements(tuple_5,tuple_6))




