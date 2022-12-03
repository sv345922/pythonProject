from typing import List


def find_max_under_boundary(input_array: List[int], top_boundary: int, direction='max') -> int:
    # Найдем текущий максимум
    current = float('-inf') if direction == 'max' else float('inf')
    i_lim = 0
    for i in range(len(input_array)):
        if direction == 'max':
            if input_array[i] > current:
                current = input_array[i]
                i_lim = i
        elif direction == 'min':
            if input_array[i] < current:
                current = input_array[i]
                i_lim = i
    input_array.pop(i_lim)

    return current


def find_top_elements(input_array: List[int], number_of_elements: int) -> List[int]:
    # проверка аргументов
    if number_of_elements < 0 or number_of_elements > len(input_array):
        raise Exception()
    array_in = input_array[:]
    # Создадим массив для результата
    top_elements = []
    # Нам требуется знать предыдущее значение максимума,
    # По-умолчанию мы положим туда максимальное значение для типа float
    previous_max = float('inf')

    # Выполним цикл столько раз, сколько максимумов нам нужно найти
    for i in range(number_of_elements):
        # Найдем текущий максимум
        current_max = find_max_under_boundary(array_in, previous_max)

        # Обновим значение "предыдущего" максимума
        previous_max = current_max

        # Положим результат в выходной массив
        top_elements.append(current_max)

    return top_elements


def find_bottom_elements(input_array: List[int], number_of_elements: int) -> List[int]:
    # проверка аргументов
    if number_of_elements < 0 or number_of_elements > len(input_array):
        raise Exception()

    # список в результат
    res = []
    previous_min = float('-inf')
    for i in range(number_of_elements):
        current_min = find_max_under_boundary(input_array, previous_min, direction='min')
        previous_min = current_min
        res.append(current_min)
    return res


if __name__ == '__main__':
    array = [10, 66, 4, 16, 99, 35, 11, 123]

    top5 = find_top_elements(array, 3)
    print("Top 5:", top5)

    top8 = find_top_elements(array, 8)
    print("Top 8:", top8)