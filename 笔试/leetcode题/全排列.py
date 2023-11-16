class Solution:
    def permute(self, nums):
        res = []

        def dfs(n, path):
            if n == len(nums):
                res.append(path.copy())
                return
            for i in nums:
                if i not in path:
                    path.append(i)
                    dfs(n + 1, path)
                    path.remove(i)

        dfs(0, [])

        return res


s = Solution()
print(s.permute([1, 2, 3]))
