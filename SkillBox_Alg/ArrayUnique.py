from typing import List


def letters_learned_today(word: str) -> str:
    """возвращает список уникальных элементов"""
    res = ""
    for letter in (word):
        if letter not in res:
            res += letter
    return res


def avoid_jail_due_to_tax_fraud(report: List[List[int]]) -> int:
    """возвращает первую запись, имеющую повторения в двумерном массиве, иначе вернет -1"""
    tmp = []
    for row in report:
        for elem in row:
            if elem in tmp:
                return elem
            tmp.append(elem)
    return -1

word = "АААФФФФФФФЖЫЫЫЫБЫРВАААААЛГГГХЫХЫБЛИА"
#print(letters_learned_today(word))
report = [
  [12391203, 3828382, 334934939],
  [45345345, 5341312, 55345345],
  [3349349309, 1234122, 657657],
]
print(avoid_jail_due_to_tax_fraud(report))