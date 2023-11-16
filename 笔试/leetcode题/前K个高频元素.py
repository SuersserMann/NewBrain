import numpy as np


class Solution:
    def topKFrequent(self, nums, k: int):
        if not nums:
            return 0
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        a = []
        b = []
        res = []
        for key, val in dict.items():
            a.append(key)
            b.append(val)
        idx = np.argsort(b)[::-1]
        for j in range(k):
            res.append(a[idx[j]])
        return res


s = Solution()
print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
