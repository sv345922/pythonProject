from itertools import groupby
class Archiv:
    def __init__(self):
        self._str = input("Ввести строку для обработки")

    @staticmethod
    def marge(lst):
        return "".join(list(map(str, lst)))

    def first(self):
        res = [1, self._str[0]]
        for i in range(1, len(self._str)):
            if self._str[i] == self._str[i - 1]:
                res[-2] += 1
            else:
                if res[-2] == 1:
                    del res[-2]
                res.extend([1, self._str[i]])
        if res[-2] == 1:
            del res[-2]
        return self.marge(res)

    def split_es(self):
        letter = self._str[0]
        n = 0
        for c in self._str:
            if letter == c:
                n += 1
            else:
                yield n, letter
                n = 1
                letter = c
        yield n, letter

    @staticmethod
    def encoder_series(gen):
        res = ""
        for num, letter in gen:
            res = res + (
                    str(num) * (num > 1)    # тоже что и - "" if num == 1 else str(num))
                         ) + letter
        return res

    def whith_iter(self):
        l = [list(gr) for c, gr in groupby(self._str)]
        for a in l:
            print(len(a) if len(a) > 1 else '', a[0], sep='', end='')
        return

mod = Archiv()
#enc = mod.encoder_series(mod.split_es())
enc = mod.whith_iter()
#print(enc)
