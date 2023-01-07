from typing import List
import json
import datetime


class HashMapsAreFast:


    def get_unique_numbers(self, input_array: List[int]) -> List[int]:
        """Возвращает новый список, к котором ключи соотносятся с хеш-функцией элемента"""

        def hash_func(num_in):
            """Возвращает хеш числа по произведению его цифр, если цифра 0, используется 1"""
            # return num_in # использовать само число как хеш, работает намного быстрее
            hash_num = 1
            tmp = num_in
            while tmp > 0:
                num = tmp % 10
                hash_num *= num if num != 0 else 1
                tmp //= 10
            return hash_num

        def find_index(array, num):
            """Возвращает свободный индекс массива array в зависимости от значения хеша числа num, а также проверяет
            на повтор числа num, если число повторяется, то возвращает None"""
            l = len(array)
            result = hash_func(num) % l
            while array[result]:
                if array[result] == num:
                    return
                result = (result + 1) % l
            return result

        hashed_list = [0] * (len(input_array))
        for element in input_array:
            hash_ind = find_index(hashed_list, element)
            if hash_ind:
                hashed_list[hash_ind] = element
        return hashed_list

    def are_there_two_numbers(self, numbers: List[int], x: int) -> bool:
        def find_index(array, num, x):
            l = len(array)
            indx = num % l # вместо хэш функции используется само число
            if array[(x - num) % l] == x - num:
                return
            while array[indx]:
                indx = (indx + 1) % l
            return indx

        hash_map = [0] * len(numbers)
        for num in numbers:
            hash_ind = find_index(hash_map, num, x)
            if hash_ind != None:
                hash_map[hash_ind] = num
            else:
                return True
        return False


if __name__ == "__main__":
#    t_0 = datetime.datetime.now()
    test_array = []
    with open("test.json", "r") as file:
        test_array = json.load(file)
    t_00 = datetime.datetime.now()
    x = 1
#    print(f"Чтения из файла: {t_00 - t_0}")
    array = HashMapsAreFast()
    #result = array.get_unique_numbers(test_array)
    result = array.are_there_two_numbers(test_array, x)
    t_1 = datetime.datetime.now()
    print(result)
    print(f"Поиск через хеш-мап: {t_1 - t_00}")


    def simple_find(test_array, x):
        for i in range(len(test_array)):
            for j in range(i + 1, len(test_array)):
                if test_array[i] + test_array[j] == x:
                    return True
        return False

    print(simple_find(test_array, x))
    t_2 = datetime.datetime.now()
    print(f"Поиск обычный: {t_2 - t_1}")
    #st = set(test_array)

    #print(len(st), len(set(result)) - 1)

