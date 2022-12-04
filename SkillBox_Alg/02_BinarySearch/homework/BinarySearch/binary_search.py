import random

from typing import List


class DatingUser:
    def __init__(self, iq: int, name: str):
        self.iq = iq
        self.name = name


def do_i_know_this_language(languages: List[str], search: str) -> bool:
    for lang in languages:
        if search == lang:
            return True
    return False

def find_phone_number(sorted_phone_numbers: List[int], search: int) -> int:
    """Возвращает индекс найденного телефона в списке sorted_phone_numbers или -1 если номаре в списке нет"""
    if sorted_phone_numbers[0] < sorted_phone_numbers[-1]:
        left = 0
        right = len(sorted_phone_numbers) - 1
        while left <= right:
            middle = (left + right) // 2
            tmp = sorted_phone_numbers[middle]
            if tmp < search:
                left = middle + 1
            elif tmp > search:
                right = middle - 1
            else:
                return middle
    else

    return -1

def find_users(users_sorted_by_iq: List[DatingUser], lower_iq_bound: int, professor_iq: int) -> List[str]:
    """Возвращает список имен из списка users_sorted_by_iq у которых iq в пределах от lower_iq_bound до professor_iq
    включительно"""
#    res = []
#    for user in users_sorted_by_iq:
#        if lower_iq_bound <= user.iq <= professor_iq:
#            res.append(user.name)
    def find_border(users_sorted_by_iq, iq_t):
        """Возвращает индекс первого значения, соответствующего iq_t"""
        right_index = len(users_sorted_by_iq) - 1
        left_index = 0
        while left_index <= right_index:
            middle_index = (right_index + left_index) // 2
            tmp = users_sorted_by_iq[middle_index].iq
            if tmp >= iq_t:
                right_index = middle_index - 1
            elif tmp < iq_t:
                left_index = middle_index + 1
        return left_index

    min_index = find_border(users_sorted_by_iq, lower_iq_bound)
    max_index = find_border(users_sorted_by_iq, professor_iq + 1)

    res = [user.name for user in users_sorted_by_iq[min_index:max_index]]
    return res


peoples = []
#for i in map(int, "71 74 75 76 77 80 93 95 96 97 97 99 102 104 106 111 117 121 135 136".split()):
#    man = DatingUser(iq=i, name=str(i) + "man")
#    peoples.append(man)
for _ in range(100):
    i = random.randrange(70, 140)
    man = DatingUser(iq=i, name='men'+str(i))
    peoples.append(man)
peoples.sort(key=lambda x: x.iq)

for elem in peoples:
    print(elem.iq, end=" ")
print()
print(find_users(peoples, 90, 105))
