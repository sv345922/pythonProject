# Modify sys.path to import modules from examples dir
import os, sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from typing import List

from examples.Dynamic.hash_map import HashMap


class DynamicHashMap(HashMap):
    def delete_key(self, key: str) -> None:
        index = self.find_good_index(key)
        entry = self.entries[index]
        del self.entries[index]
        self.number_of_elements -= 1
        if self.number_of_elements == self.size * 0.25:
            self.resize(self.size // 2)

    def get_all_keys(self) -> List[str]:
        result = []
        for element in self.entries:
            if element:
                result.append(element.key)
        return result

    def get_all_values(self) -> List[str]:
        result = []
        for element in self.entries:
            if element:
                result.append(element.value)
        return result

if __name__ == "__main__":
    test = DynamicHashMap()
    for key, value in enumerate('abcdefghijklmnopqrstuvwxyz', 1):
        test.add(str(key), value)
    test.delete_key("10")
    print(sorted(list(zip(test.get_all_keys(), test.get_all_values())), key=lambda x: int(x[0])))