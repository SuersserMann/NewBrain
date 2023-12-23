class Solution:
    def subsets(self, nums):
        m = len(nums)
        res = []

        def dfs(length, path):
            if len(path) == length:

                res.append(path.copy())
                return
            for i in range(m):
                if nums[i] not in path:
                    path.append(nums[i])
                    dfs(length, path)
                    path.pop()
            return res

        for j in range(m + 1):
            dfs(j, [])

        return res


s = Solution()
print(s.subsets([1, 2, 3]))
