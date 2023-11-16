x = -597


def reverse(x):
    if x >= 0:
        c = x
        d = []
        result = 0
        while c != 0:
            a = c % 10
            c = c // 10
            d.append(a)
        for i in range(len(d)):
            result += d[i] * 10 ** (len(d)-i-1)
        if result<=2**31-1:

            return result
        else:
            return 0
    else:
        c = -x
        d = []
        result = 0
        while c != 0:
            a = c % 10
            c = c // 10
            d.append(a)
        for i in range(len(d)):
            result += d[i] * 10 ** (len(d) - i - 1)
        if result <= 2 ** 31:
            return -result
        else:
            return 0


print(reverse(x))
