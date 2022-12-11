from typing import List
import random
from sorted_check import is_sorted


def my_is_sorted(array: List[int]) -> bool:
    flag = True
    for i in range(len(array) - 1):
        if array[i] > array[i+1]:
            return False
    return True


def random_sort(array: List[int]) -> None:
    k = 0
    while not my_is_sorted(array):
        n, m = random.sample(range(len(array)), 2)
        array[n], array[m] = array[m], array[n]
        k += 1
    print(k)


test = list(range(10))
random.shuffle(test)
print(test)
random_sort(test)
print(test)