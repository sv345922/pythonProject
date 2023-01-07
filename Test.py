import random
import json

def gen_num_list(n, start, end):
    """Cохраняет в файле test.txt сгенерированный список чисел в количестве n в диапазоне от start до end"""
    with open("test.txt", "w") as file:
        for _ in range(n): # количество элементов
            file.write(str(random.randrange(start, end)) + "\n") # диапазон значений

def gen_list_to_json(n, start, end):
    result = []
    for _ in range(n):
        result.append(random.randrange(start, end))
    with open("SkillBox_Alg/03_HashMaps/homework/HashMapsAreFast/test.json", "w") as file:
        json.dump(result, file)
    return result


n = 100_000
start = 0
end = 100_001
#gen_num_list(n, start, end)
gen_list_to_json(n, start, end)
print("Done")