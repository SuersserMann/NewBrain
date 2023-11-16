class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return False
        stack = []
        dict = {'}': '{', ']': '[', ')': '('}
        for i in range(len(s)):
            if s[i] not in dict:
                stack.append(s[i])
            else:
                if stack == [] or dict[s[i]] != stack.pop():
                    return False
        return not stack
