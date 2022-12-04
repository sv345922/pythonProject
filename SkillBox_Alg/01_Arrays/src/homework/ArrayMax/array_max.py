from typing import List

# Task #1
def find_smallest_transaction(transactions: List[int]) -> int:
    """Возвращает максимальный элемент в списке transaction"""
    res = transactions[0]
    for element in transactions[1:]:
        if element > res:
            res = element
    return res


# Task #2
def find_best_student_mistakes(students: List[int]) -> int:
    """Возвращает минимальное значение в списке students"""
    res = students[0]
    for mistakes in students[1:]:
        if mistakes < res:
            res = mistakes
    return res


# Task #3
def find_average_time(times: List[int]) -> float:
    """Возвращает среднее значение из списка times"""
    res = sum(times) / len(times)
    return res


# Task #4
def find_most_profitable_client(income: List[List[int]]) -> int:
    """Возвращает индекс подмассива с максимальной суммой элементов массива income"""
    res = 0
    tmp = sum(income[0])
    for i in range(1, len(income)):
        if sum(income[i]) > tmp:
            res = i
    return res

