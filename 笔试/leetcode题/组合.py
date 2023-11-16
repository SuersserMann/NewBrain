class Solution:
    def combine(self, n, k):
        res = []

        def dfs(m, path):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(m, n+1):
                path.append(i)
                dfs(i + 1, path)
                path.pop()

        dfs(1, [])
        return res


s = Solution()
print(s.combine(4, 2))
