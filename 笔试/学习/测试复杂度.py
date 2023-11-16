from timeit import Timer
from functools import lru_cache


def test1():
    list = []
    for i in range(1000):
        list.append(i)
    return list


def test2():
    list = []
    for i in range(1000):
        list = list + [i]
    return list


def test3():
    list = [i for i in range(1000)]
    return list


def test4():
    x = list(range(1000))
    return x


timer1 = Timer(stmt='test1()', setup='from __main__ import test1')
t1 = timer1.timeit(100)
print(t1)

timer2 = Timer(stmt='test2()', setup='from __main__ import test2')
t2 = timer2.timeit(100)
print(t2)

timer3 = Timer(stmt='test3()', setup='from __main__ import test3')
t3 = timer3.timeit(100)
print(t3)

timer4 = Timer(stmt='test4()', setup='from __main__ import test4')
t4 = timer4.timeit(100)
print(t4)
@lru_cache
def test5(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return test5(n - 2) + test5(n - 1)


timer5 = Timer(stmt='test5(500)', setup='from __main__ import test5')
t5 = timer5.timeit(100)
print(t5)
