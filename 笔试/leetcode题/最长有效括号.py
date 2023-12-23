class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = []
    #     res = 0
    #     first = True
    #     idx = 0
    #     for i in range(len(s)):
    #         if s[i] == '(' and first:
    #             idx = i
    #             stack.append(i)
    #             first = False
    #         elif s[i] == '(' and not first:
    #             stack.append(i)
    #         else:
    #             if not stack:
    #                 first = True
    #             else:
    #                 stack.pop()
    #                 if not stack:
    #                     res = max(res, i - idx + 1)
    #                 else:
    #                     res = max(res, i - stack[-1])
    #     return res

    # def longestValidParentheses(self, s: str) -> int:
    #     res = 0
    #     n = len(s)
    #     dp = [0 for _ in range(n)]
    #     for i in range(n):
    #         if i > 0 and s[i] == ")":
    #             if s[i - 1] == "(":
    #                 dp[i] = dp[i - 2] + 2
    #             elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
    #                 dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 1 - 1]
    #             if dp[i] > res:
    #                 res = dp[i]
    #
    #     return res

    def longestValidParentheses(self, s: str) -> int:
        res = 0
        n = len(s)
        stack = []
        res = []
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif stack and s[i] == ')':
                j = stack.pop()
                res.append(i)
                res.append(j)
        res.sort()
        if not res:
            return 0
        cur = 1
        final = 0
        for i in range(len(res) - 1):
            if res[i + 1] == res[i] + 1:
                cur += 1
                final = max(final, cur)
            else:
                cur = 1
        return final


s = Solution()
print(s.longestValidParentheses(")()())"))
