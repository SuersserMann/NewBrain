class Solution:
    def longestPalindrome(self, s):
        ## 代码随想录动态规划 dp[i][j]表示子串在[i,j]闭区间内是否为回文子串
        ## 首先只有dp[i]==dp[j]才会考虑能不能用，其次，考虑两种情况，分别是间距一以内的和大于等于2的
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0
        a, b = 0, 0
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1:
                        dp[i][j] = True
                        if j - i + 1 > res:
                            res = j - i + 1
                            a, b = i, j
                    elif dp[i + 1][j - 1]:
                        dp[i][j] = True
                        if j - i + 1 > res:
                            res = j - i + 1
                            a, b = i, j
        return s[a:b + 1]
