class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        x = m
        y = n
        for i in range(x):
            cur = False
            g = i + 1
            for j in range(x - i):
                if cur:
                    break
                for h in range(y - i):
                    if cur:
                        break
                    little_matrix = True
                    for t in range(j, j + g):
                        if cur:
                            break
                        if not little_matrix:
                            break
                        for u in range(h, h + g):
                            if matrix[t][u] == '0':
                                little_matrix = False
                                break
                            if t == j + g - 1 and u == h + g - 1:
                                cur = True
                                break
            if not cur:
                return i**2
            if i == x - 1 and cur:
                return (i + 1)**2


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
s = Solution()
print(s.maximalSquare(matrix))
