import matplotlib.pyplot as plt


def collatz(digit):
    yield digit
    while digit != 1:
        digit = digit * 3 + 1 if digit % 2 else digit // 2
        yield digit


def counter_collatz(digit):
    sm, cnt = 0, 0
    for item in collatz(digit):
        sm += item
        cnt += 1
    return sm / cnt, cnt


table = [(0, 0)]
for i in range(1, 100):
    table.append(counter_collatz(i))

sum_table = [i[0] for i in table]
count_table = [i[1] for i in table]
fig = plt.figure()
graph1 = plt.plot(sum_table, 'g')
graph2 = plt.plot(count_table, 'r')