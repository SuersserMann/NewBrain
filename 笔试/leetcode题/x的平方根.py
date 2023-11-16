x = 5

x = 3


def mySqrt(x):
    if x == 0:
        return 0
    if 0 < x <= 3:
        return 1
    left, right = 1, x // 2
    while left <= right:
        mid = left + (right - left) // 2
        if mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1
    return left - 1


print(mySqrt(x))
