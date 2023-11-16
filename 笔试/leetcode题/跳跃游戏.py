class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i in range(len(nums) - 1):
            if max_idx < i:
                return False
            if i + nums[i] >= max_idx:
                max_idx = i + nums[i]
        if max_idx >= len(nums) - 1:
            return True
        else:
            return False