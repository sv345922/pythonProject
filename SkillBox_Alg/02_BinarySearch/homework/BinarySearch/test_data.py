import random

with open("test_list", "w", encoding="utf-8") as file:
    for _ in range(100):
        number = "8"
        for a in range(10):
            i = random.randrange(0, 10)
            number += str(i)
        file.write(number + "\n")