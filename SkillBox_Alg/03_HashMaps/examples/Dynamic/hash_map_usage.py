from hash_map import HashMap


def search_and_print(key: str) -> None:
    print("Поиск по ключу", key, ", найдено =", hashmap.get(key))


hashmap = HashMap()

# Заполняем данными
hashmap.add("1", "11")
hashmap.add("2", "22")
hashmap.add("3", "33")
hashmap.add("4", "44")
hashmap.add("5", "55")
hashmap.add("6", "66")
hashmap.add("7", "77")

# Контроль поиска элемента
print("Количество ячеек массива HashMap:", hashmap.size)
print("Количество элементов массива HashMap:", hashmap.number_of_elements)
search_and_print("4")

hashmap.add("14", "1414")
hashmap.add("15", "1515")
hashmap.add("16", "1616")

print("===")
print("Количество ячеек массива HashMap:", hashmap.size)
print("Количество элементов массива HashMap:", hashmap.number_of_elements)
# Проверка после ресайза HashMap
search_and_print("4")
search_and_print("3")
search_and_print("1")
search_and_print("14")
search_and_print("15")
search_and_print("16")
# Такого ключа нет
search_and_print("100")
