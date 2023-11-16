a = input().split()
a = [int(i) for i in a]
n = len(a)


def test(a0, a1, a2, a3):
    for i in range(n - 3):
        if a[i + 2] != a0 + a1 * a[i+1] + a2 * a[i] + a3 * a[i] * a[i + 1]:
            return 1
        else:
            return int(a0 + a1 * x + a2 * x1 + a3 * x * x1)


if 1 < n <= 2:
    a2 = a3 = 0
    x = a[-1]
    x1 = a[-2]
    while 1:
        a1 = a2 = a3 = 0
        a0 = x - a1 * x1
        result = a0 + a1 * x
        print(result)
        break

if n > 2:
    x = a[-1]
    x1 = a[-2]
    x2 = a[-3]
    cc = 1

    a1 = a2 = a3 = 0
    a0 = x - a1 * x1 - a2 * x2 - a3 * x1 * x2
    if test(a0, a1, a2, a3) != 1:
        print(test(a0, a1, a2, a3))
        cc = 2

    a0 = a2 = a3 = 0
    if (x - a0 - a2 * x2 - a3 * x1 * x2) % (x1) == 0:
        a1 = (x - a0 - a2 * x2 - a3 * x1 * x2) % (x1)
        if test(a0, a1, a2, a3) != 1:
            print(test(a0, a1, a2, a3))
            cc = 2

    a0 = a1 = a3 = 0
    if (x - a0 - a1 * x1 - a3 * x1 * x2) % (x2) == 0:
        a2 = (x - a0 - a1 * x1 - a3 * x1 * x2) % (x2)
        if test(a0, a1, a2, a3) != 1:
            print(test(a0, a1, a2, a3))
            cc = 2

    a0 = a1 = a2 = 0
    if (x - a0 - a1 * x1 - a2 * x2) % (x1 * x2) == 0:
        a3 = (x - a0 - a1 * x1 - a2 * x2) % (x1 * x2)
        if test(a0, a1, a2, a3) != 1:
            print(test(a0, a1, a2, a3))
            cc = 2

    a2 = a3 = 0
    a1 = (x - x1) / (x1 - x2)
    a0 = x - a1 * x1 - a2 * x2 - a3 * x1 * x2
    if test(a0, a1, a2, a3) != 1:
        print(test(a0, a1, a2, a3))
        cc = 2

    # a0 = a3 = 0
    # a1 = (x-a2 * x2)/x1
    # a2 = (x-a1 * x1)/x2
    # a1 = (x - x1) / (x1 - x2)
    # a0 = x - a1 * x1 - a2 * x2 - a3 * x1 * x2
    # if test(a0, a1, a2, a3) != 1:
    #     print(test(a0, a1, a2, a3))
    #     cc = 2

    if cc == 1:
        print('wrong')
