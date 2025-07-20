# Define a function to count the frequency of words in a given list of words.
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']


def count_frequency(list):
    frequency = {}    # -----------------> O(1)
    for word in list: # -----------------> O(n)
        if word in frequency: # -----------------> O(1)
            frequency[word] += 1 # -----------------> O(1)
        else:
            frequency[word] = 1 # -----------------> O(1)
    return frequency # -----------------> O(1)
    

print(count_frequency(words))

#Time Complexity: O(n)
#Space Complexity: O(n)



# Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}




def merge_dict(dict1,dict2):
    merged_dict = dict1.copy()
    for key,value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value
        else:
            merged_dict[key] = value
    return merged_dict

print(merge_dict(dict1,dict2))

#Time Complexity: O(n + m)
#Space Complexity: O(n + m)
 


# Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
my_dict = {'a': 5, 'b': 9, 'c': 2}




def highest_value_key(dict):
    max_value = max(dict.values())
    for key,value in dict.items():
        if value == max_value:
            return key

print(highest_value_key(my_dict))

#Time Complexity: O(n)
#Space Complexity: O(1)


# Define a function which takes as a parameter dictionary and returns a dictionary in which everse the key-value pairs are reversed.
my_dict1 = {'a': 1, 'b': 2, 'c': 3}


def reverse_dict(dict):
    reversed_dict = {}
    for key,value in dict.items():
        # reversed_dict[value] = key
        temp = key
        key = value
        value = temp
        reversed_dict[key] = value
    return reversed_dict

print(reverse_dict(my_dict1))

#Time Complexity: O(n)
#Space Complexity: O(n)


# Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.

my_dict2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

def filter_dict(dict,condition):
    filtered_dict = {key:value for key,value in dict.items() if condition(key,value)}
    return filtered_dict

print(filter_dict(my_dict2,lambda key,value: value > 3))

#Time Complexity: O(n)
#Space Complexity: O(n)


# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]


def same_frequency(list1,list2)->bool:
    dict1 = {item:list1.count(item) for item in list1}
    dict2 = {item:list2.count(item) for item in list2}

    return dict1 == dict2

print(same_frequency(list1,list2))

#Time Complexity: O(n)
#Space Complexity: O(n)

