#Given a list, write a function to get first, second best scores from the list.

from typing import List

def best_score(list):
    first_best_score = 0
    second_best_score = 0

    for score in list:
        if score > first_best_score:
            second_best_score = first_best_score
            first_best_score = score

        elif score > second_best_score:
            second_best_score = score
    return first_best_score,second_best_score

print(best_score([1,2,2,4,5,3,4,5,6,7,8,9,10]))