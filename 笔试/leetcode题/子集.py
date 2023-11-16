class Solution:
    def subsets(self, nums):
        m = len(nums)
        res = []

        def dfs(n, k, path):
            if len(path) == k:
                res.append(path.copy())
                return
            for i in range(n, m):
                path.append(nums[i])
                dfs(i + 1, k, path)
                path.pop()
            return res

        for j in range(1, m+1):
            dfs(0, j, [])
        res.append([])
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
