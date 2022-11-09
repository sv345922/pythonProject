from collections import Counter


class Find_mult:
    def __init__(self):
        self.nums = list(map(int, input().split()))

    def whith_counter(self):
        a = Counter(self.nums)
        res = [key for key, vol in a.items() if vol > 1]
        return res

    def whith_set(self):
        res = set([i for i in self.nums if self.nums.count(i) > 1])
        return res

    def whith_sort(self):
        self.nums.sort()
        res = set()
        for i in range(1, len(self.nums)):
            if self.nums[i] == self.nums[i - 1]:
                res.add(self.nums[i])
        return res


ob = Find_mult()
res = ob.whith_sort()
print(*res)