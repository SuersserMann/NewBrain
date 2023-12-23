class Solution:
    # def merge(self, intervals):
    #     res = []
    #     if len(intervals) <= 1:
    #         return intervals
    #
    #     intervals = sorted(intervals)
    #     cur = intervals[0]
    #     for i in range(len(intervals) - 1):
    #         if cur[1] >= intervals[i + 1][0]:
    #             if cur[1] < intervals[i + 1][1]:
    #                 cur[1] = intervals[i + 1][1]
    #         else:
    #             res.append(cur)
    #             cur = intervals[i + 1]
    #
    #     res.append(cur)
    #     return res
    def merge(self, intervals):
        if len(intervals) <= 1:
            return intervals
        res = []
        cur = sorted(intervals)
        ans = [cur[0]]
        for i in range(1, len(intervals)):
            if ans[-1][1] < cur[i][0]:
                ans.append(cur[i])
            else:
                ans[-1][1] = max(ans[-1][1], cur[i][1])
        return ans


s = Solution()
print(s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]))
