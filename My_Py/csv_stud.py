import csv
import pprint
from collections import Counter

with open("Crimes.csv", "r") as file:
    data = csv.reader(file)
    data = [i[5] for i in data if '2015' in i[2]]
    data = Counter(data)
print(data.most_common(1))

