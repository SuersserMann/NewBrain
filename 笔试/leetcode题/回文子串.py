class Solution:
    def countSubstrings(self, s: str) -> int:
        ## 代码随想录动态规划 dp[i][j]表示子串在[i,j]闭区间内是否为回文子串
        n = len(s)
        dp = [[False] * n  for _ in range(n)]
        res = 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        res += 1
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        res += 1
        return res
