class Solution:
    def removeInvalidParentheses(self, s: str):
        stack = []
        res = []

        def check():
            for i in range(len(s)):
                if s[i] == '(':
                    stack.append(i)
                elif s[i] == ')':
                    if stack:
                        stack.pop()
                    else:
                        return i

        # def dfs(idx):
        #
        #
        # state=check()
        # while state:


s = "()())()"
x = Solution()
print(x.removeInvalidParentheses(s))
