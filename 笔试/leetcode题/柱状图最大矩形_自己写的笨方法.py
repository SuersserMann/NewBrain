class Solution:
    def largestRectangleArea(self, heights):
        m = len(heights)
        list_heights = list(set(sorted(heights)))
        res = 0
        for i in list_heights:
            cur = 0
            count = 0
            for j in range(m):
                if j != m - 1:
                    if heights[j] >= i:
                        count += 1
                        cur = max(cur, count * i)
                    else:
                        count = 0
                else:
                    if heights[j] >= i:
                        count += 1
                        cur = max(cur, count * i)
            res = max(res, cur)
        return res


s = Solution()
print(s.largestRectangleArea([1,1]))
