class Solution:
    def decodeString(self, s: str) -> str:

        def dfs(path):
            cur = []
            if not path:
                return
            stack = []
            j = 0
            number = []
            while j < len(path):
                if path[j].isdigit():
                    number.append(path[j])
                    j += 1
                elif path[j] == '[':
                    stack.append('[')
                    for g in range(j + 1, len(path)):
                        if path[g] == ']':
                            stack.pop()
                            if not stack:
                                cur.append(int(''.join(number)) * dfs(path[j + 1:g]))
                                number = []
                                j = g + 1
                                break
                        if path[g] == '[':
                            stack.append('[')
                else:
                    cur.append(path[j])
                    j += 1
            return ''.join(cur)

        return ''.join(dfs(s))


s = Solution()
print(s.decodeString(s="3[a]2[bc]"))
