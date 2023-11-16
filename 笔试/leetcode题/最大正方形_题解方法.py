class Solution:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        matrix = [[int(j) for j in i] for i in matrix]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if dp[i + 1][j] != 0 and dp[i][j + 1] != 0:
                        dp[i + 1][j + 1] = min(dp[i][j],dp[i + 1][j],dp[i][j + 1]) + 1
                    else:
                        dp[i + 1][j + 1] = 1
        res = 0
        for i in range(m+1):
            cur = max(dp[i])
            res = max(res, cur)
        return res**2
s=Solution()
print(s.maximalSquare([["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]))