class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = min(m, n)
        x = m + n - 2
        y = c - 1
        a = 1
        b = 1
        for i in range(y):
            a = a * x
            x -= 1
            b = b * y
            y -= 1
        return int(a / b)
