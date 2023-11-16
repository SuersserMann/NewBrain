class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s) + 1, len(p) + 1
        dp = [[False] * n for _ in range(m)]
        dp[0][0] = True
        # 初始化首行
        for j in range(2, n, 2):
            if dp[0][j - 2] is True and p[j - 1] == '*':
                dp[0][j] = True
            else:
                dp[0][j] = False

            # 首先判断dp第一行，如何两个数字前为True,且上一个数字为*，则之前的数字都是匹配的，由于第一行是匹配空值，那么必须是%前接一个数字才合法

            # 状态转移
        for i in range(1, m):
            for j in range(1, n):
                if p[j - 1] == '*':
                    if dp[i][j - 2]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j] and s[i - 1] == p[j - 2]:
                        dp[i][j] = True  # 2.
                    elif dp[i - 1][j] and p[j - 2] == '.':
                        dp[i][j] = True  # 3.
                else:
                    if dp[i - 1][j - 1] and s[i - 1] == p[j - 1]:
                        dp[i][j] = True  # 1.
                    elif dp[i - 1][j - 1] and p[j - 1] == '.':
                        dp[i][j] = True  # 2.
        return dp[-1][-1]


s = Solution()
a = 'a'
b = 'ab*'
print(s.isMatch(a, b))
