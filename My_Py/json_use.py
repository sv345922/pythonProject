import json


def counter_children(data, parent):
    children = data[parent]
    tmp = set()
    if len(children) == 1:
        return children
    for child in children:
        if child != parent:
            tmp |= counter_children(data, child)
    return children | tmp


data = json.loads(input())
result_all = {}

# формируем первичный словарь - имя: непосредственные потомки
result = {}
for elem in data:
    result.setdefault(elem['name'], {elem['name']})
    for parent in elem["parents"]:
        result[parent] = result.get(parent, {parent}) | {elem["name"]}

# формирование множества всех потомков для каждого родителя
for parent in result.keys():
    result_all[parent] = counter_children(result, parent)

for key, value in sorted(result_all.items()):
    print(f"{key} : {len(value)}")

# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]