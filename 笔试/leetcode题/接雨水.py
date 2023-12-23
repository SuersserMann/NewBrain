# 从左往右找最大值
# 从右往左找最大值
# 之后遍历，比较两个列表最小值与当前高度的差
class Solution:
    def trap(self, height):
        res = 0
        dp1 = [0] * len(height)
        for i in range(len(height)):
            res = max(res, height[i])
            dp1[i] = res
        res = 0
        dp2 = [0] * len(height)
        for i in range(len(height) - 1, -1, -1):
            res = max(res, height[i])
            dp2[i] = res

        res = 0
        for i in range(len(height)):
            if min(dp1[i], dp2[i]) > height[i]:
                res += min(dp1[i], dp2[i]) - height[i]
        return res


s = Solution()
print(s.trap([4, 2, 0, 3, 2, 5]))
