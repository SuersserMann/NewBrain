x = -2147483648


def reverse(x):
    fu = False
    z = str(x)
    if z[0] == '-':
        n = len(z) - 1
        fu = True
    else:
        n = len(z)
    if fu:
        d = "-"
        for i in range(n):
            d += z[-1 - i]
        d = int(d)
        if -(2 ** 31) <= d <= 2 ** 31 - 1:
            return d
        else:
            return 0
    else:
        d = ""
        for i in range(n):
            d += z[-1 - i]
        d = int(d)
        if -(2 ** 31) <= d <= 2 ** 31 - 1:
            return d
        else:
            return 0


print(reverse(x))
