import re


class Decoder:
    def __init__(self, code):
        self.code = code

    def first_re(self):
        s = self.code
        pattern = r"\d*[A-z]"
        spisok = re.findall(pattern, s)
        res = ""
        for c in spisok:
            if len(c) == 1:
                res += c
            else:
                res += c[-1] * int(c[:-1])
        return res

    def second_re(self):
        res = re.sub(r"(\d*)([^\W\d])", lambda gr: gr[2] * int(gr[1] if gr[1] else 1), self.code)
        return res

    def first(self):
        n = ""
        for c in self.code:
            if c.isdigit():
                n += c
                continue
            yield int(n or 1), c
            n = ''

    @staticmethod
    def second(self, gen):
        return "".join([(c * n) for n, c in gen])

    def main(self):
        return self.second(self.first())


mt = Decoder("3ab4c2CaB") #input())
print(mt.main())
