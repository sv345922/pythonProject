from primes import *
import itertools
import datetime as dt

def calc_time(func):
    t1 = dt.datetime.now()
    func()
    print(f'Время выполнения: {dt.datetime.now() - t1}')


def foo():
    print(list(itertools.takewhile(lambda x : x <= 310000, primes())))

calc_time(foo)

