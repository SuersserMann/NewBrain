class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        res = min(height[right], height[left]) * (right - left)
        while left < right:
            if height[right] < height[left]:
                while height[right - 1] < height[right]:
                    if right > left:
                        right -= 1
                    else:
                        break
                right -= 1
                cur = min(height[right], height[left]) * (right - left)
                if cur >= res:
                    res = cur
            else:
                while height[left + 1] < height[left]:
                    if left < right:
                        left += 1
                    else:
                        break
                left += 1
                cur = min(height[right], height[left]) * (right - left)
                if cur >= res:
                    res = cur
        return res


s = Solution()
print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
