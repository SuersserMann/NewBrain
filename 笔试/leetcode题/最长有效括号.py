class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        res = 0
        first = True
        idx = 0
        for i in range(len(s)):
            if s[i] == '(' and first:
                idx = i
                stack.append(i)
                first = False
            elif s[i] == '(' and not first:
                stack.append(i)
            else:
                if not stack:
                    first = True
                else:
                    stack.pop()
                    if not stack:
                        res = max(res, i - idx + 1)
                    else:
                        res = max(res, i - stack[-1])
        return res


s = Solution()
print(s.longestValidParentheses(")()())"))
