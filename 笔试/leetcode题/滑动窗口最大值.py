from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        q = deque()
        for i, j in enumerate(nums):
            while q and j > nums[q[-1]]:
                q.pop()
            q.append(i)

            if i - q[0] >= k:
                q.popleft()

            if i >=k-1:
                res.append(nums[q[0]])
        return res
s=Solution()
print(s.maxSlidingWindow([7,2,4],2))