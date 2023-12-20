import numpy as np


class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        dp = [0] * n
        stack = []
        for i in range(n):
            if not stack:
                stack.append((i, temperatures[i]))
            else:
                while temperatures[i] > stack[-1][1]:
                    dp[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                    if not stack:
                        break
                stack.append((i, temperatures[i]))
        return dp

s = Solution()
print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
