class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                if i == 0:
                    dp[i + 1][j + 1] = dp[i + 1][j] + grid[i][j]
                elif j == 0:
                    dp[i + 1][j + 1] = dp[i][j+1] + grid[i][j]
                else:
                    dp[i + 1][j + 1] = min(dp[i][j + 1], dp[i + 1][j]) + grid[i][j]

        return dp[-1][-1]
s=Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))