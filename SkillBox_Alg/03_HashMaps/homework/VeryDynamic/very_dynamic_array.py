# Modify sys.path to import modules from examples dir
import os, sys
import random

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from examples.Dynamic.dynamic_array import DynamicArray


class VeryDynamicArray(DynamicArray):
    def delete_element_at(self, index: int) -> None:
        """Удаляет элемент по индексу и сдвигает оставшуюся часть массива"""
        if index < self.size:
            self.values[index] = None
            for i in range(index, self.size - 1):
                self.values[i] = self.values[i + 1]
            self.size -= 1
            self.current_index -= 1


test = VeryDynamicArray()
for _ in range(15):
    test.add(random.randrange(1, 100))
print(test.values)
test.delete_element_at(7)
print(test.values)