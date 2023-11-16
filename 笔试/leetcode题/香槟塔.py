class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        n = query_row
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = poured
        for i in range(n):
            for j in range(n + 1):
                if dp[i][j] > 1:
                    dp[i + 1][j] += (dp[i][j] - 1) / 2
                    dp[i + 1][j + 1] += (dp[i][j] - 1) / 2
                    dp[i][j] = 1
        # 不要忘记和1取min
        return min(1, dp[query_row][query_glass])
