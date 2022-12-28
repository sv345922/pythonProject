import os
import re
import pprint


res = []

for elem in os.walk("main"):
    for file in elem[2]:
        if file.endswith(".py"):
            res.append(elem[0])
            break

res = sorted(list(res))
for i in range(len(res)):
    res[i] = res[i].replace("\\", "/")

pprint.pprint(res)
#with open("res.txt", "w") as file:
#    for i in res:
#        file.write(i + "\n")