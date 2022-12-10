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
    def finder(left, right, direction=1):
        """возвращает обновленные границы диапазона и значение индекса если соответсвие найдено, иначе None"""
        while direction * left <= direction * right:
            middle = (left + right) // 2
            tmp = sorted_phone_numbers[middle]
            if tmp < search:
                left = middle + direction
            elif tmp > search:
                right = middle - direction
            else:
                return middle
        return -1


    if sorted_phone_numbers[0] < sorted_phone_numbers[-1]:
        left = 0
        right = len(sorted_phone_numbers) - 1
        return finder(left, right, 1)


    else:
        left = len(sorted_phone_numbers) - 1
        right = 0
        return finder(left, right, -1)


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


#for i in map(int, "71 74 75 76 77 80 93 95 96 97 97 99 102 104 106 111 117 121 135 136".split()):
#    man = DatingUser(iq=i, name=str(i) + "man")
#    peoples.append(man)


def test(n):
    """тестировщик поиска номера"""
    # Генерация списка номеров
    search = random.randrange(80000000000, 90000000000)
    numbers = [search]
    for _ in range(100):
        number = "8"
        for a in range(10):
            i = random.randrange(0, 10)
            number += str(i)
        numbers.append(int(number))
    direct = random.choice([False, True])
    print(direct, end=" ")
    numbers.sort(reverse=direct)
    ind = find_phone_number(numbers, search)
    if numbers.index(search) == ind:
        print(f"test {n} - ок")
    else:
        print(f"test {n} - faild")

for n in range(50):
    test(n)

#lst = []
#with open("test_list", "r") as file:
#    for line in file:
#        lst.append(line.strip())

#search = lst[5]
#lst.sort(reverse=False)

#print(find_phone_number(lst, search))

