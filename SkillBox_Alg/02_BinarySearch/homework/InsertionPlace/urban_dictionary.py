from typing import List


class UrbanDictionary:
    def __init__(self) -> None:
        self.new_russian_dictionary: List[str] = ["Контент", "Лутер", "Тренд", "Фиксер", "Фэшн", "Хипстер"]


    def insert_new_word(self, word: str) -> None:
        UrbanDictionary()
        left = 0
        right = len(self.new_russian_dictionary) - 1
        while left < right:
            midlle = (left + right) // 2
            if word > self.new_russian_dictionary[midlle]:
                left = midlle + 1
            else:
                right = midlle
        self.new_russian_dictionary.append('')
        for i in range(len(self.new_russian_dictionary) - 1, left, -1):
            self.new_russian_dictionary[i] = self.new_russian_dictionary[i - 1]
        self.new_russian_dictionary[left] = word



A = UrbanDictionary()
A.insert_new_word('Флудер')
print(A.new_russian_dictionary)