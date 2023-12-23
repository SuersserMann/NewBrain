class Solution:
    # def combinationSum(self, candidates, target):
    #     res = []
    #
    #     def dfs(amount, path):
    #         for i in candidates:
    #             if amount == target:
    #                 a = sorted(path)
    #                 if a not in res:
    #                     res.append(a)
    #                 return
    #             elif amount > target:
    #                 return
    #             else:
    #                 path.append(i)
    #                 dfs(amount + i, path)
    #                 path.remove(i)
    #
    #     dfs(0, [])
    #     return res

    def combinationSum(self, candidates, target):
        res = []
        n = len(candidates)

        def dfs(amount, path):
            if amount == target:
                xx = path.copy()
                xx.sort()
                if xx not in res:
                    res.append(xx)
                    return
                else:
                    return
            elif amount > target:
                return

            for i in range(n):
                # if candidates[i] not in path:
                path.append(candidates[i])
                dfs(amount + candidates[i], path)
                path.remove(candidates[i])

        dfs(0, [])
        return res


nums = list(range(1, 10))
s = Solution()
print(s.combinationSum(nums, 6))
