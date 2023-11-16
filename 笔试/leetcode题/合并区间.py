class Solution:
    def merge(self, intervals):
        res = []
        if len(intervals) <= 1:
            return intervals

        intervals = sorted(intervals)
        cur = intervals[0]
        for i in range(len(intervals) - 1):
            if cur[1] >= intervals[i + 1][0]:
                if cur[1] < intervals[i + 1][1]:
                    cur[1] = intervals[i + 1][1]
            else:
                res.append(cur)
                cur = intervals[i + 1]

        res.append(cur)
        return res


s = Solution()
print(s.merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
