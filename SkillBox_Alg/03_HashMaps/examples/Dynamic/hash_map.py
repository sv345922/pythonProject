import re
from typing import List, Optional


class KeyValuePair:
    key: str
    value: str

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value


class HashMap:
    def __init__(self):
        self.entries: List[Optional[KeyValuePair[0]]] = [None] * 8
        self.size = 8
        self.number_of_elements = 0

    # хеш на основе индекса UTF каждого символа строки
    def hash_function(self, key: str) -> int:
        hash = 0
        for ch in range(len(key)):
            hash += ord(key[ch]) * 10 ^ ch
        return hash

    def add(self, key: str, value: str) -> None:
        index = self.find_good_index(key)
        self.entries[index] = KeyValuePair(key=key, value=value)
        self.number_of_elements += 1
        if self.number_of_elements == self.size:
            self.resize(self.size * 2)

    def resize(self, new_size: int) -> None:

        # Создать новый массив
        new_entries = [None] * new_size

        # перезаписываем данные класса на новые
        old_size = self.size
        self.size = new_size
        old_entries = self.entries
        self.entries = new_entries

        # Скопировать элементы из старого массива
        for i in range(old_size):
            if old_entries[i] is None:
                continue
            entry = old_entries[i]
            new_index = self.find_good_index(entry.key)
            new_entries[new_index] = old_entries[i]

    def get(self, key: str) -> Optional[str]:
        index = self.find_good_index(key)
        if index == -1:
            return None
        entry = self.entries[index]
        if entry is None:
            return None
        # Так как нет защиты от коллизий,
        # перебираем все элементы, если в ячейку не тот ключ
        if entry.key == key:
            return entry.value

        for i in range(self.size):
            if self.entries[i].key == key:
                return self.entries[index].value
        return None

    def find_good_index(self, key: str) -> int:
        calculated_hash = self.hash_function(key)
        index = calculated_hash % self.size
        for i in range(self.size):
            probing_index = (index + i) % self.size
            entry = self.entries[probing_index]
            if entry is None or entry.key == key:
                return probing_index
        return -1
